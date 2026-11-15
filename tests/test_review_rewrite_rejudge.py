"""Offline receipt binding, tamper rejection, and blind extraction-review artifacts."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from _support import load_script
from test_rewrite_rejudge import build_baseline, fake_invoke

review = load_script("scripts/review_rewrite_rejudge.py")
rr = review.rr


def save_response(attempt: Path, model: str, prompt: str, text: str) -> tuple[str, dict]:
    provider = "claude" if model.startswith("claude-") else "openai"
    response_id = rr.sb.sha(model + prompt)
    if provider == "openai":
        raw = json.dumps({"result": {"model": model, "responseId": response_id, "stopReason": "stop",
            "content": [{"type": "text", "text": text}], "usage": {"cost": {"total": 0.01}}}})
    else:
        raw = "\n".join(json.dumps(e) for e in [
            {"type": "assistant", "message": {"id": response_id, "content": [{"type": "text", "text": text}]}},
            {"type": "result", "subtype": "success", "is_error": False, "num_turns": 1,
             "permission_denials": [], "modelUsage": {model: {}}, "usage": {},
             "total_cost_usd": 0.02, "result": text}])
    (attempt / "stdout.txt").write_text(raw)
    (attempt / "prompt.txt").write_text(prompt)
    rr.sb.dump(attempt / "request.json", {"model": model, "provider": provider,
        "prompt_sha256": rr.sb.sha(prompt), "returncode": 0, "tools": [], "effort": "medium",
        "system_prompt": "You are a helpful assistant.",
        "started": 100.0, "seconds": 1.0})
    return rr.sb.audit_response(provider, raw, model)


class Receipts(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.slot = self.root / "slot"
        attempt = self.slot / "attempt-1"
        attempt.mkdir(parents=True)
        _, usage = save_response(attempt, "gpt-6.1-sol", "prompt", '{"value": 7}')
        rr.sb.dump(self.slot / "complete.json", {"value": 7, "attempt": 1, "usage": usage,
            "input_sha256": rr.sb.sha("gpt-6.1-sol\nprompt")})

    def selected(self):
        return review.selected(self.slot, "gpt-6.1-sol", "prompt", lambda result: result)

    def test_exact_request_raw_response_and_record_pass(self) -> None:
        receipt = self.selected()
        self.assertEqual(receipt["returned_list_price_equivalent_usd"], 0.01)
        self.assertEqual(receipt["response_id"], rr.sb.sha("gpt-6.1-solprompt"))
        self.assertEqual(receipt["model"], "gpt-6.1-sol")

    def test_changed_complete_record_is_rejected(self) -> None:
        path = self.slot / "complete.json"
        rr.sb.dump(path, rr.sb.read_json(path) | {"value": 8})
        with self.assertRaisesRegex(ValueError, "differs from raw"):
            self.selected()

    def test_changed_prompt_is_rejected(self) -> None:
        (self.slot / "attempt-1" / "prompt.txt").write_text("different prompt")
        with self.assertRaisesRegex(ValueError, "request differs"):
            self.selected()

    def test_model_substitution_is_rejected(self) -> None:
        path = self.slot / "attempt-1" / "stdout.txt"
        raw = rr.sb.read_json(path)
        raw["result"]["model"] = "other-model"
        rr.sb.dump(path, raw)
        with self.assertRaisesRegex(ValueError, "unexpected model"):
            self.selected()

    def test_json_whitespace_near_miss_preserves_the_selected_value(self) -> None:
        path = self.slot / "attempt-1" / "stdout.txt"
        raw = rr.sb.read_json(path)
        raw["result"]["content"][0]["text"] = '{\n "value" : 7\n}'
        rr.sb.dump(path, raw)
        self.assertEqual(self.selected()["returned_list_price_equivalent_usd"], 0.01)

    def test_checksum_paths_cannot_escape_the_publication(self) -> None:
        rr.sb.dump(self.root / "checksums.json", {"../outside": "ignored"})
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            review.verify(self.root)


class Packet(unittest.TestCase):
    def test_checkpoint_replays_raw_receipts_and_keeps_audit_verdicts_out_of_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            baseline = build_baseline(root / "baseline", families=1)
            runtime = root / "runtime"
            manifest = rr.prepare(baseline, runtime)
            (runtime / "registration-commit.txt").write_text("registration-before-calls\n")
            original_invoke = rr.sb.invoke
            fake = fake_invoke()
            def invoke(model, prompt, effort, attempt):
                text, _ = fake(model, prompt, effort, attempt)
                if prompt.startswith("Audit an extraction"):
                    result = json.loads(text)
                    result["checks"][0]["pass"] = False
                    result["checks"][0]["evidence"] = "MODEL_ONLY_FLAG_EVIDENCE"
                    text = json.dumps(result)
                return save_response(attempt, model, prompt, text)
            rr.sb.invoke = invoke
            try:
                rr.extract(baseline, runtime, 2)
                rr.audit(baseline, runtime, 2)
            finally:
                rr.sb.invoke = original_invoke
            target = root / "published"
            target.mkdir()
            review.generate(baseline, runtime, target)
            summary = rr.sb.read_json(target / "checkpoint.json")
            self.assertEqual(summary["status"], "blocked before judging")
            self.assertEqual(summary["flagged_outputs"], len(manifest["outputs"]))
            self.assertEqual(summary["writing_judgments"], 0)
            self.assertEqual(summary["unique_returned_provider_response_ids"], 25)
            packet = (target / "REVIEW-PACKET.md").read_text()
            self.assertNotIn("MODEL_ONLY_FLAG_EVIDENCE", packet)
            self.assertNotIn("no-skill", packet)
            self.assertNotIn("gpt-6.1-sol", packet)
            key = rr.sb.read_json(target / "REVIEW-PRIVATE-KEY.json")
            answers = rr.sb.read_json(target / "REVIEW-ANSWERS.template.json")
            self.assertEqual(len(key), 12)
            self.assertEqual({r["id"] for r in key}, {r["id"] for r in answers["items"]})
            self.assertTrue(all(c["pass"] is None for r in answers["items"] for c in r["checks"]))
            again = root / "again"
            again.mkdir()
            review.generate(baseline, runtime, again)
            for name in review.GENERATED:
                self.assertEqual((target / name).read_bytes(), (again / name).read_bytes())
            source = next(runtime.glob("extract/sol/*/attempt-1"))
            historical = baseline / "judge/sol/history/attempt-1"
            historical.mkdir(parents=True)
            for name in ("request.json", "stdout.txt"):
                (historical / name).write_bytes((source / name).read_bytes())
            rr.sb.dump(historical.parent / "complete.json", {"attempt": 1})
            with self.assertRaisesRegex(ValueError, "overlaps baseline"):
                review.inspect(baseline, runtime)


if __name__ == "__main__":
    unittest.main()
