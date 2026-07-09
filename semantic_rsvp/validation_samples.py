from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_PATH = PROJECT_ROOT / "docs" / "validation" / "corpus.md"


def load_validation_samples(corpus_path: Path | None = None) -> list[dict[str, str]]:
    path = corpus_path or DEFAULT_CORPUS_PATH
    if not path.exists():
        return []

    sections = path.read_text(encoding="utf-8").split("\n## Sample ")
    samples = []
    for section in sections[1:]:
        sample = _parse_sample_section(section)
        if sample:
            samples.append(sample)
    return samples


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
