"""Registered study construction and aggregation; synthetic tests, never model trials."""
from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from _support import load_script

study = load_script("scripts/candidate_studies.py")
base = study.base


class CandidateStudies(unittest.TestCase):
    def test_packages_reject_tampering_unknown_arms_and_no_skill_exposure(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            (dest / "current.txt").write_text("current")
            (dest / "candidate.txt").write_text("candidate")
            manifest = {
                "slots": [{"arm": "current"}, {"arm": "candidate"}, {"arm": "no-skill"}],
                "arm_packages": {
                    "no-skill": None,
                    "current": {"file": "current.txt", "sha256": base.sha("current")},
                    "candidate": {"file": "candidate.txt", "sha256": base.sha("candidate")},
                },
            }
            self.assertEqual(base.load_packages(dest, manifest), {
                "no-skill": "", "current": "current", "candidate": "candidate",
            })
            for mutate in (
                lambda m: m["arm_packages"].__setitem__("no-skill", {"file": "current.txt"}),
                lambda m: m["slots"].append({"arm": "unknown"}),
                lambda m: m["arm_packages"]["candidate"].__setitem__("file", "../candidate.txt"),
                lambda m: m["arm_packages"]["candidate"].__setitem__("sha256", base.sha("other")),
            ):
                bad = copy.deepcopy(manifest)
                mutate(bad)
                with self.subTest(bad=bad), self.assertRaises(ValueError):
                    base.load_packages(dest, bad)
            (dest / "candidate.txt").write_text("changed")
            with self.assertRaisesRegex(ValueError, "frozen candidate package changed"):
                base.load_packages(dest, manifest)

    def test_mean_scores_reject_missing_extra_and_duplicate_trials(self):
        slots = [{"id": str(i), "case_id": "c", "arm": "current", "model": "sonnet", "trial": i + 1} for i in range(3)]
        records = [{"id": str(i), "primary_dimensions": [{"name": n, "score": i + 3, "evidence": "source"} for n in base.PRIMARY]} for i in range(3)]
        means = study.mean_scores(slots, records)
        self.assertEqual(means[("c", "sonnet", "current")]["factual_fidelity"], 0.75)
        self.assertAlmostEqual(means[("c", "sonnet", "current")]["unsupported"], 1 / 3)
        for bad in (records[:-1], records + [records[0]], records + [{**records[0], "id": "extra"}]):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                study.mean_scores(slots, bad)

    def test_fact_twins_and_repeats_cannot_multiply_the_target_family(self):
        rows = [{"id": str(i), "split": "holdout", "pair_id": "one-pair", "family": "one-scaffold", "before": 0.25, "after": 0.75} for i in range(6)]
        result = base.stats(rows, "family")
        self.assertEqual(result["clusters"], 1)
        self.assertEqual(result["verdict"], "UNDERPOWERED")
        self.assertEqual(result["sign_flip_p"], 1.0)

    def test_candidate_sources_do_not_change_the_installed_skill(self):
        files = study.installed_files()
        variants = study.candidates(files)
        self.assertEqual(variants["current"], files)
        self.assertEqual(files, study.installed_files())
        self.assertIn("Do not invent a definition", variants["compound"]["SKILL.md"])
        self.assertNotIn("Do not invent a definition", files["SKILL.md"])
        self.assertIn("Forward-pointing teasers:", variants["teaser"]["SKILL.md"])
        self.assertNotIn("Forward-pointing teasers:", variants["compound"]["SKILL.md"])
        for name in ("compound", "teaser"):
            self.assertEqual({p: t for p, t in variants[name].items() if p != "SKILL.md"}, {p: t for p, t in files.items() if p != "SKILL.md"})


if __name__ == "__main__":
    unittest.main()
