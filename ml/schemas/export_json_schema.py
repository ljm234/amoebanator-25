"""Export VignetteSchema to JSON Schema for external consumers.

Run: python -m ml.schemas.export_json_schema
Output: schemas/vignette_schema_v2.0.json (UTF-8, indent=2)
"""
from __future__ import annotations

import json
from pathlib import Path

from ml.schemas.vignette import VignetteSchema


def export_json_schema(output_path: Path) -> dict:
    """Generate JSON Schema and write to disk. Returns schema dict for inspection."""
    schema = VignetteSchema.model_json_schema()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False))
    return schema


if __name__ == "__main__":
    out = (
        Path(__file__).resolve().parent.parent.parent
        / "schemas"
        / "vignette_schema_v2.0.json"
    )
    schema = export_json_schema(out)
    print(f"Exported to: {out}")
    print(f"Schema keys: {list(schema.keys())}")
    print(f"Top-level properties: {len(schema.get('properties', {}))}")
    print(f"Definitions ($defs): {len(schema.get('$defs', {}))}")
    print(f"File size: {out.stat().st_size:,} bytes")
