import re
import unicodedata


def normalize_text(raw_text: str) -> str:
    if not isinstance(raw_text, str):
        raise TypeError("normalize_text expects a string.")

    text = unicodedata.normalize("NFC", raw_text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    normalized_lines = []
    for line in text.split("\n"):
        collapsed = re.sub(r"[ \t]+", " ", line).strip()
        normalized_lines.append(collapsed)

    text = "\n".join(normalized_lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
