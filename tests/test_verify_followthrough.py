"""Offline artifact accounting rejects corruption and preserves unknown usage."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from _support import load_script

verify = load_script("scripts/verify_followthrough.py")


class OfflineVerification(unittest.TestCase):
    def test_deduplicates_trace_copies_but_does_not_zero_fill_unknown_costs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def trace(name, data):
                folder = root / name
                folder.mkdir()
                (folder / "stdout.jsonl").write_text(json.dumps(data) + "\n")
            result = {"type": "result", "messages": [{"role": "assistant", "responseId": "response-A", "usage": {"cost": {"total": 0.25}}}]}
            trace("original", result)
            trace("copy", result)
            report = verify.usage("activation", root)
            self.assertEqual(report["distinct_raw_traces"], 1)
            self.assertEqual(report["unique_returned_provider_response_ids"], 1)
            self.assertEqual(report["returned_list_price_equivalent_usd"], 0.25)
            trace("unknown", {"type": "result", "messages": [{"role": "assistant", "responseId": "response-B"}]})
            trace("known-zero", {"type": "result", "messages": [{"role": "assistant", "responseId": "response-C", "usage": {"cost": {"total": 0}}}]})
            report = verify.usage("activation", root)
            self.assertEqual(report["traces_without_complete_cost_counters"], 1)
            self.assertEqual(report["unique_returned_provider_response_ids"], 3)
            self.assertEqual(report["returned_list_price_equivalent_usd"], 0.25)

    def test_inventory_is_exact_and_corruption_blocks_before_archive_access(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.json").write_text("original")
            (root / "reproduction.json").write_text("not self-hashed")
            verify.inventory(root)
            self.assertEqual(json.loads((root / "checksums.json").read_text()), {"source.json": verify.digest(root / "source.json")})
            (root / "source.json").write_text("corrupted")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                verify.verify("activation", root)


if __name__ == "__main__":
    unittest.main()
