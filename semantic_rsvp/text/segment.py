import re

from semantic_rsvp.text.normalize import normalize_text

_DOT_TOKEN = "<DOT>"
_ELLIPSIS_TOKEN = "<ELLIPSIS>"
_MONTHS = {
    "jan",
    "january",
    "feb",
    "february",
    "mar",
    "march",
    "apr",
    "april",
    "may",
    "jun",
    "june",
    "jul",
    "july",
    "aug",
    "august",
    "sep",
    "sept",
    "september",
    "oct",
    "october",
    "nov",
    "november",
    "dec",
    "december",
}
_WEEKDAYS = {
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
}
_ABBREVIATIONS = (
    "Mr.",
    "Mrs.",
    "Ms.",
    "Dr.",
    "Prof.",
    "a.m.",
    "p.m.",
    "U.S.",
    "E.U.",
    "e.g.",
    "i.e.",
    "etc.",
)


def split_sentences(text: str) -> list[str]:
    normalized = normalize_text(text)
    if not normalized:
        return []

    structured_sentences = _split_structural_lines(normalized)
    if structured_sentences is not None:
        return structured_sentences

    return _split_sentence_like_text(normalized)


def _split_sentence_like_text(text: str) -> list[str]:
    protected = _protect_abbreviations(text)
    protected = protected.replace("...", _ELLIPSIS_TOKEN)

    pieces = re.findall(
        rf".+?(?:{re.escape(_ELLIPSIS_TOKEN)}|[.!?]+)[\"'\u201d)\]]*(?=\s+|$)|.+$",
        protected,
        flags=re.DOTALL,
    )

    sentences = []
    for piece in pieces:
        restored = _restore_tokens(piece).strip()
        if restored:
            sentences.append(restored)
    return sentences


def _split_structural_lines(text: str) -> list[str] | None:
    lines = text.split("\n")
    if len(lines) == 1:
        return None

    sentences: list[str] = []
    prose_buffer: list[str] = []

    def flush_prose() -> None:
        if not prose_buffer:
            return
        sentences.extend(_split_sentence_like_text(" ".join(prose_buffer)))
        prose_buffer.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_prose()
            continue
        if _is_structural_boundary_line(stripped):
            flush_prose()
            sentences.append(stripped)
            continue
        prose_buffer.append(stripped)

    flush_prose()
    return sentences


def _is_structural_boundary_line(line: str) -> bool:
    if line.startswith("# ") or line.startswith("## "):
        return True
    if _is_long_form_date(line):
        return True
    if _looks_like_byline(line):
        return True
    if _looks_like_title_or_source_line(line):
        return True
    return False


def _is_long_form_date(line: str) -> bool:
    words = _line_words(line)
    lowered = [word.lower().rstrip(".") for word in words]
    if len(lowered) in {2, 3, 4} and lowered[0].rstrip(",") in _WEEKDAYS:
        lowered = lowered[1:]
    if len(lowered) == 3 and lowered[0] in _MONTHS and _is_day(lowered[1]) and _is_year(lowered[2]):
        return True
    if len(lowered) == 3 and _is_day(lowered[0]) and lowered[1] in _MONTHS and _is_year(lowered[2]):
        return True
    if len(lowered) == 2 and lowered[0] in _MONTHS and _is_year(lowered[1]):
        return True
    return False


def _looks_like_byline(line: str) -> bool:
    words = _line_words(line)
    if len(words) == 1:
        return _is_titlecase(words[0])
    if 2 <= len(words) <= 4 and line.lower().startswith(("by ", "analysis by ")):
        return True
    return False


def _looks_like_title_or_source_line(line: str) -> bool:
    if re.search(r"[.!?;:]$", line):
        return False
    words = _line_words(line)
    if not 2 <= len(words) <= 10:
        return False
    title_like = sum(1 for word in words if _is_titlecase(word) or word.lower() in {"of", "the", "and", "on", "in", "to", "a", "an"})
    return title_like >= max(2, len(words) - 1)


def _line_words(line: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+(?:[-'\u2019][A-Za-z0-9]+)?", line)


def _is_day(word: str) -> bool:
    stripped = word.rstrip(",")
    return stripped.isdigit() and 1 <= int(stripped) <= 31


def _is_year(word: str) -> bool:
    stripped = word.rstrip(",")
    return stripped.isdigit() and 1900 <= int(stripped) <= 2200


def _is_titlecase(word: str) -> bool:
    stripped = word.strip("\"'.,;:!?()[]")
    return bool(stripped) and stripped[0].isupper()


def _protect_abbreviations(text: str) -> str:
    protected = text
    for abbreviation in _ABBREVIATIONS:
        pattern = re.compile(re.escape(abbreviation), flags=re.IGNORECASE)
        protected = pattern.sub(
            lambda match: match.group(0).replace(".", _DOT_TOKEN),
            protected,
        )
    return protected


def _restore_tokens(text: str) -> str:
    return text.replace(_ELLIPSIS_TOKEN, "...").replace(_DOT_TOKEN, ".")
