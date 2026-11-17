import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RecordChecks(unittest.TestCase):
    def test_cli_exit_status(self):
        cases = {"valid": 0, "domain-invalid": 1, "wrong-type": 1, "missing-field": 1}
        for fixture, expected in cases.items():
            with self.subTest(fixture=fixture):
                result = subprocess.run(
                    [sys.executable, "scripts/check_record.py", f"examples/record.{fixture}.json"],
                    cwd=ROOT, capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, expected, result.stderr)
                if expected:
                    self.assertTrue(result.stderr.strip())
