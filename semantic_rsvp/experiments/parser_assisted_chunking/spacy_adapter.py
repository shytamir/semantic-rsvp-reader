from __future__ import annotations

import importlib
import importlib.metadata
from functools import lru_cache

from semantic_rsvp.experiments.parser_assisted_chunking.alignment import validate_alignment
from semantic_rsvp.experiments.parser_assisted_chunking.models import (
    LinguisticRelation,
    LinguisticSpan,
    LinguisticToken,
    ParseResult,
)

PINNED_SPACY_VERSION = "3.7.5"
PINNED_MODEL_NAME = "en_core_web_sm"
PINNED_MODEL_VERSION = "3.7.1"


def availability() -> tuple[bool, str]:
    try:
        spacy_version = importlib.metadata.version("spacy")
    except importlib.metadata.PackageNotFoundError:
        return False, "spacy_unavailable"
    if spacy_version != PINNED_SPACY_VERSION:
        return False, f"spacy_version_mismatch:{spacy_version}"
    try:
        model_version = importlib.metadata.version(PINNED_MODEL_NAME)
    except importlib.metadata.PackageNotFoundError:
        return False, "model_unavailable"
    if model_version != PINNED_MODEL_VERSION:
        return False, f"model_version_mismatch:{model_version}"
    return True, "available"


@lru_cache(maxsize=1)
def _load_pipeline():
    available, reason = availability()
    if not available:
        raise RuntimeError(reason)
    spacy = importlib.import_module("spacy")
    return spacy.load(PINNED_MODEL_NAME)


def parse_text(text: str) -> ParseResult:
    try:
        nlp = _load_pipeline()
        doc = nlp(text)
    except Exception as exc:
        return ParseResult(
            text=text,
            tokens=(),
            parser_library="spacy",
            parser_version=_version_or_empty("spacy"),
            model_name=PINNED_MODEL_NAME,
            model_version=_version_or_empty(PINNED_MODEL_NAME),
            alignment_status="failed",
            failure_reason=str(exc),
        )

    token_id_by_index = {token.i: index for index, token in enumerate(doc)}
    tokens = tuple(
        LinguisticToken(
            token_id=token_id_by_index[token.i],
            text=token.text,
            start=token.idx,
            end=token.idx + len(token.text),
            sentence_index=_sentence_index(doc, token),
            pos=token.pos_,
            tag=token.tag_,
            dep=token.dep_,
            head_id=token_id_by_index.get(token.head.i),
            entity_type=token.ent_type_,
            whitespace=token.whitespace_,
        )
        for token in doc
    )
    spans: list[LinguisticSpan] = []
    spans.extend(
        LinguisticSpan(ent.start_char, ent.end_char, "entity", ent.label_, "spacy")
        for ent in doc.ents
    )
    spans.extend(
        LinguisticSpan(chunk.start_char, chunk.end_char, "noun_phrase", "", "spacy")
        for chunk in doc.noun_chunks
    )
    relations = _relations(doc, token_id_by_index)
    parse = ParseResult(
        text=text,
        tokens=tokens,
        spans=tuple(_dedupe_spans(spans)),
        relations=tuple(relations),
        parser_library="spacy",
        parser_version=_version_or_empty("spacy"),
        model_name=PINNED_MODEL_NAME,
        model_version=_version_or_empty(PINNED_MODEL_NAME),
        alignment_status="unknown",
    )
    aligned, diagnostics = validate_alignment(parse)
    return ParseResult(
        text=parse.text,
        tokens=parse.tokens,
        spans=parse.spans,
        relations=parse.relations,
        parser_library=parse.parser_library,
        parser_version=parse.parser_version,
        model_name=parse.model_name,
        model_version=parse.model_version,
        alignment_status="ok" if aligned else "failed",
        alignment_diagnostics=diagnostics,
        failure_reason=None if aligned else "alignment_invalid",
    )


def _sentence_index(doc, token) -> int:
    for index, sent in enumerate(doc.sents):
        if sent.start <= token.i < sent.end:
            return index
    return 0


def _relations(doc, token_id_by_index: dict[int, int]) -> list[LinguisticRelation]:
    relations: list[LinguisticRelation] = []
    for token in doc:
        token_id = token_id_by_index[token.i]
        head_id = token_id_by_index.get(token.head.i)
        if head_id is not None and head_id != token_id:
            relations.append(LinguisticRelation(token_id, head_id, "dependency", "spacy"))
        if token.dep_ == "aux" and head_id is not None:
            relations.append(LinguisticRelation(token_id, head_id, "aux_main", "spacy"))
        if token.dep_ == "neg" and head_id is not None:
            relations.append(LinguisticRelation(token_id, head_id, "negation", "spacy"))
        if token.dep_ == "prt" and head_id is not None:
            relations.append(LinguisticRelation(token_id, head_id, "verb_particle", "spacy"))
    return relations


def _dedupe_spans(spans: list[LinguisticSpan]) -> list[LinguisticSpan]:
    seen = set()
    result = []
    for span in spans:
        key = (span.start, span.end, span.span_type, span.label)
        if key not in seen:
            seen.add(key)
            result.append(span)
    return result


def _version_or_empty(package: str) -> str:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return ""
