"""Synthetic source fixture for the illustrative LARA example."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def import_order(order: dict[str, Any], processed_directory: Path) -> str:
    """Materialize an order once in a sequential, single-process fixture."""
    order_id = order.get("order_id")
    if not isinstance(order_id, str) or not order_id:
        raise ValueError("order_id is required")

    destination = processed_directory / f"{order_id}.json"
    if destination.exists():
        return "duplicate"

    processed_directory.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(order, sort_keys=True), encoding="utf-8")
    return "imported"
