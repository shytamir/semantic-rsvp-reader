from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_ROOT = REPO_ROOT / "evaluation" / "parser_assisted_chunking"
MANIFEST_DIR = EXPERIMENT_ROOT / "manifests"
BASELINE_DIR = EXPERIMENT_ROOT / "baseline"
BASELINE_OUTPUT_PATH = BASELINE_DIR / "rule_based_baseline.json"
MANIFEST_HASH_PATH = BASELINE_DIR / "manifest_hashes.json"
VISIBLE_CORPORA = ("development", "regression", "generalization")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_path(corpus: str) -> Path:
    return MANIFEST_DIR / f"{corpus}.jsonl"


def manifest_hashes() -> dict[str, str]:
    return {
        corpus: sha256_file(manifest_path(corpus))
        for corpus in VISIBLE_CORPORA
    }


def load_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for corpus in VISIBLE_CORPORA:
        path = manifest_path(corpus)
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    case = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
                case["_manifest"] = str(path.relative_to(REPO_ROOT))
                case["_line_number"] = line_number
                cases.append(case)
    return cases


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
