"""Behavioral evidence for the synthetic order-import fixture."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

EXAMPLE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXAMPLE_ROOT / "source"))

from import_orders import import_order  # noqa: E402


class ImportOrderTests(unittest.TestCase):
    def test_sequential_duplicate_preserves_first_payload(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)

            self.assertEqual(
                "imported",
                import_order({"order_id": "demo-001", "amount": 10}, output),
            )
            self.assertEqual(
                "duplicate",
                import_order({"order_id": "demo-001", "amount": 99}, output),
            )

            stored = json.loads((output / "demo-001.json").read_text(encoding="utf-8"))
            self.assertEqual(10, stored["amount"])


if __name__ == "__main__":
    unittest.main()
