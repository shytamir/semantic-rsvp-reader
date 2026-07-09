import re

from semantic_rsvp.text.normalize import normalize_text

_DOT_TOKEN = "<DOT>"
_ELLIPSIS_TOKEN = "<ELLIPSIS>"
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

    protected = _protect_abbreviations(normalized)
    protected = protected.replace("...", _ELLIPSIS_TOKEN)

    pieces = re.findall(
        rf".+?(?:{re.escape(_ELLIPSIS_TOKEN)}|[.!?]+)(?=\s+|$)|.+$",
        protected,
        flags=re.DOTALL,
    )

    sentences = []
    for piece in pieces:
        restored = _restore_tokens(piece).strip()
        if restored:
            sentences.append(restored)
    return sentences


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
