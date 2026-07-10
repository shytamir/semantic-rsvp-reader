from __future__ import annotations

from semantic_rsvp.experiments.parser_assisted_chunking.models import ParseResult


def validate_alignment(parse: ParseResult) -> tuple[bool, tuple[str, ...]]:
    diagnostics: list[str] = []
    previous_end = 0
    for token in parse.tokens:
        if token.start < 0 or token.end > len(parse.text) or token.start >= token.end:
            diagnostics.append(f"token {token.token_id} has invalid offsets")
            continue
        if token.start < previous_end:
            diagnostics.append(f"token {token.token_id} overlaps a previous token")
        if parse.text[token.start:token.end] != token.text:
            diagnostics.append(f"token {token.token_id} text does not match source")
        previous_end = token.end
    for span in parse.spans:
        if span.start < 0 or span.end > len(parse.text) or span.start >= span.end:
            diagnostics.append(f"span {span.span_type}:{span.label} has invalid offsets")
    for relation in parse.relations:
        token_ids = {token.token_id for token in parse.tokens}
        if relation.source_id not in token_ids or relation.target_id not in token_ids:
            diagnostics.append(f"relation {relation.relation_type} references missing token")
    return not diagnostics, tuple(diagnostics)
