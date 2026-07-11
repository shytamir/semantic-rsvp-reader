import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_PATH = PROJECT_ROOT / "docs" / "validation" / "corpus.md"
DEFAULT_MANIFEST_PATHS = (
    PROJECT_ROOT / "evaluation" / "parser_assisted_chunking" / "manifests" / "development.jsonl",
    PROJECT_ROOT / "evaluation" / "parser_assisted_chunking" / "manifests" / "regression.jsonl",
    PROJECT_ROOT / "evaluation" / "parser_assisted_chunking" / "manifests" / "generalization.jsonl",
)
S030_CASE_IDS = (
    "dev-names-0001",
    "dev-date-0002",
    "dev-negation-0003",
    "dev-source-0005",
    "dev-width-0006",
    "dev-quote-0007",
    "dev-parenthetical-0008",
    "reg-air-force-0003",
    "reg-khamenei-0004",
    "reg-phrasal-0005",
    "reg-qualifier-0006",
    "reg-coordinated-0007",
    "gen-synthetic-0003",
    "gen-synthetic-0005",
)
LONG_FORM_COLLECTION = "general_long_form"
S030_COLLECTION = "s030_semantic_structural"


def load_validation_samples(
    corpus_path: Path | None = None,
    manifest_paths: tuple[Path, ...] | None = None,
) -> list[dict[str, str]]:
    path = corpus_path or DEFAULT_CORPUS_PATH
    samples = []
    if path.exists():
        sections = path.read_text(encoding="utf-8").split("\n## Sample ")
        for section in sections[1:]:
            sample = _parse_sample_section(section)
            if sample:
                sample.update(
                    collection=LONG_FORM_COLLECTION,
                    collection_label="General long-form validation corpus",
                    source=_display_path(path),
                )
                samples.append(sample)
    samples.extend(_load_s030_samples(manifest_paths or DEFAULT_MANIFEST_PATHS))
    return samples


def _load_s030_samples(manifest_paths: tuple[Path, ...]) -> list[dict[str, str]]:
    records: dict[str, tuple[dict, Path]] = {}
    duplicates = set()
    for path in manifest_paths:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            case_id = record.get("case_id")
            if case_id not in S030_CASE_IDS:
                continue
            if case_id in records:
                duplicates.add(case_id)
            records[case_id] = (record, path)
    if duplicates:
        raise ValueError(f"Duplicate S-030 validation case IDs: {', '.join(sorted(duplicates))}")
    missing = [case_id for case_id in S030_CASE_IDS if case_id not in records]
    if missing:
        raise ValueError(f"Missing S-030 validation case IDs: {', '.join(missing)}")

    samples = []
    for case_id in S030_CASE_IDS:
        record, path = records[case_id]
        text = record.get("text")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"S-030 validation case has empty text: {case_id}")
        samples.append(
            {
                "id": case_id,
                "category": record.get("document_role", ""),
                "purpose": ", ".join(record.get("notes", [])),
                "expected_difficulty": "Focused semantic/structural case",
                "text": text,
                "collection": S030_COLLECTION,
                "collection_label": "S-030 semantic and structural cases",
                "source": _display_path(path),
            }
        )
    return samples


def _display_path(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def _parse_sample_section(section: str) -> dict[str, str] | None:
    fields = {}
    current_field = None
    current_lines: list[str] = []

    for line in section.splitlines():
        if _is_field_line(line):
            if current_field:
                fields[current_field] = "\n".join(current_lines).strip()
            key, value = line.split(":", 1)
            current_field = _field_key(key)
            current_lines = [value.strip()] if value.strip() else []
            continue

        if current_field:
            current_lines.append(line)

    if current_field:
        fields[current_field] = "\n".join(current_lines).strip()

    sample_id = fields.get("sample_id")
    text = fields.get("text")
    if not sample_id or not text:
        return None

    return {
        "id": sample_id,
        "category": fields.get("category", ""),
        "purpose": fields.get("purpose", ""),
        "expected_difficulty": fields.get("expected_difficulty", ""),
        "text": text,
    }


def _is_field_line(line: str) -> bool:
    return any(
        line.startswith(prefix)
        for prefix in (
            "Sample ID:",
            "Category:",
            "Purpose:",
            "Expected difficulty:",
            "Text:",
        )
    )


def _field_key(label: str) -> str:
    return label.strip().lower().replace(" ", "_")
