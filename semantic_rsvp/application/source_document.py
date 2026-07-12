from __future__ import annotations

import hashlib
from collections.abc import Mapping
from dataclasses import dataclass

from semantic_rsvp.structure.markdown_headers import MarkdownHeader, detect_markdown_headers
from semantic_rsvp.text.normalize import normalize_text


@dataclass(frozen=True)
class SourceDocument:
    document_id: str
    source_type: str
    text: str
    structure: tuple[MarkdownHeader, ...]
    provenance: tuple[tuple[str, str], ...]

    @classmethod
    def from_text(
        cls,
        raw_text: str,
        *,
        source_type: str = "inline_text",
        provenance: Mapping[str, str] | None = None,
    ) -> SourceDocument:
        if not isinstance(source_type, str) or not source_type or len(source_type) > 64:
            raise ValueError("source_type must be a non-empty string of at most 64 characters.")
        normalized_text = normalize_text(raw_text)
        identity_payload = f"source-document-v1\0{source_type}\0{normalized_text}"
        return cls(
            document_id=hashlib.sha256(identity_payload.encode("utf-8")).hexdigest(),
            source_type=source_type,
            text=raw_text,
            structure=tuple(detect_markdown_headers(raw_text)),
            provenance=_normalize_provenance(provenance),
        )


def _normalize_provenance(
    provenance: Mapping[str, str] | None,
) -> tuple[tuple[str, str], ...]:
    if provenance is None:
        return ()
    if len(provenance) > 8:
        raise ValueError("provenance supports at most 8 fields.")
    normalized = []
    for key, value in provenance.items():
        if not isinstance(key, str) or not key or len(key) > 64:
            raise ValueError("provenance keys must be non-empty strings of at most 64 characters.")
        if not isinstance(value, str) or len(value) > 256:
            raise ValueError("provenance values must be strings of at most 256 characters.")
        normalized.append((key, value))
    return tuple(sorted(normalized))
