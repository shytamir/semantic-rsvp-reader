from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.chunking_experiment_common import load_cases
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.schedule import schedule_text


OUTPUT_PATH = REPO_ROOT / "evaluation" / "semantic_integrity" / "s030_characterization.json"
HUMAN_CASE_IDS = {
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
}
PROTECTED_SPANS = {
    "dev-names-0001": ["Dr. Mira Patel", "Air Force officials", "Strait of Hormuz"],
    "dev-date-0002": ["July 4, 2026"],
    "dev-negation-0003": ["did not", "back down"],
    "dev-quote-0007": ["the core claim"],
    "reg-air-force-0003": ["Air Force One"],
    "reg-khamenei-0004": ["Ayatollah Ali Khamenei", "Air Force officials", "Strait of Hormuz"],
    "reg-phrasal-0005": ["built up"],
    "reg-qualifier-0006": ["far less"],
    "reg-coordinated-0007": ["left and right wings"],
    "gen-synthetic-0003": ["ruled out"],
    "gen-synthetic-0005": ["June 18, 2026"],
}
STRUCTURAL_TEXT = "# Main Title\n\nIntro text.\n\n## First Section\n\nSection body.\n\n## Second Section\n\nClosing body."


def _chunks_with_boundaries(text: str, chunker) -> tuple[list[str], list[int]]:
    normalized = normalize_text(text)
    chunks = []
    boundaries = []
    cursor = 0
    for sentence in split_sentences(normalized):
        for chunk in chunker.chunk_sentence(sentence):
            start = normalized.find(chunk.text, cursor)
            if start < 0:
                raise ValueError("chunk_source_mapping_failed")
            end = start + len(chunk.text)
            chunks.append(chunk.text)
            boundaries.append(end)
            cursor = end
    return chunks, boundaries[:-1]


def _split_spans(text: str, boundaries: list[int], spans: list[str]) -> list[str]:
    split = []
    for span in spans:
        start = text.find(span)
        if start < 0:
            raise ValueError(f"protected_span_missing:{span}")
        end = start + len(span)
        if any(start < boundary < end for boundary in boundaries):
            split.append(span)
    return split


def build_report() -> dict:
    parser = ParserAssistedChunker()
    fallback = RuleBasedChunker()
    cases = []
    parser_fallback_count = 0
    width_violation_count = 0
    parser_protected_splits = 0
    rule_protected_splits = 0
    for case in load_cases():
        normalized = normalize_text(case["text"])
        parser_results = [parser.chunk_sentence_with_trace(sentence) for sentence in split_sentences(normalized)]
        parser_chunks = [chunk.text for result in parser_results for chunk in result.chunks]
        parser_boundaries = []
        cursor = 0
        for chunk_text in parser_chunks[:-1]:
            start = normalized.find(chunk_text, cursor)
            if start < 0:
                raise ValueError(f"{case['case_id']}:parser_source_mapping_failed")
            cursor = start + len(chunk_text)
            parser_boundaries.append(cursor)
        fallback_chunks, fallback_boundaries = _chunks_with_boundaries(normalized, fallback)
        fallback_used = any(result.optimization.fallback_used for result in parser_results)
        parser_fallback_count += int(fallback_used)
        width_violations = [
            chunk
            for chunk in parser_chunks
            if len(chunk) > parser.config.max_chars and not any(len(word) > parser.config.max_chars for word in chunk.split())
        ]
        width_violation_count += len(width_violations)
        spans = PROTECTED_SPANS.get(case["case_id"], [])
        parser_splits = _split_spans(normalized, parser_boundaries, spans)
        fallback_splits = _split_spans(normalized, fallback_boundaries, spans)
        parser_protected_splits += len(parser_splits)
        rule_protected_splits += len(fallback_splits)
        item = {
            "case_id": case["case_id"],
            "corpus": case["corpus"],
            "notes": case["notes"],
            "parser_chunk_count": len(parser_chunks),
            "rule_based_chunk_count": len(fallback_chunks),
            "parser_fallback_used": fallback_used,
            "parser_width_violations": width_violations,
            "protected_spans": spans,
            "parser_protected_span_splits": parser_splits,
            "rule_based_protected_span_splits": fallback_splits,
        }
        if case["case_id"] in HUMAN_CASE_IDS:
            item["text"] = normalized
            item["parser_chunks"] = parser_chunks
            item["rule_based_chunks"] = fallback_chunks
        cases.append(item)

    schedule = schedule_text(STRUCTURAL_TEXT, chunker=parser)
    structure = [
        {
            "text": item.chunk.text,
            "active_h1": item.structure.active_h1,
            "active_h2": item.structure.active_h2,
            "active_label": item.structure.active_label,
            "active_path": list(item.structure.active_path),
            "is_header_chunk": item.structure.is_header_chunk,
            "header_level": item.structure.header_level,
        }
        for item in schedule
    ]
    structural_failures = []
    if not any(item["active_label"] == "Main Title" for item in structure):
        structural_failures.append("missing_h1_context")
    if not any(item["active_path"] == ["Main Title", "First Section"] for item in structure):
        structural_failures.append("missing_first_h2_context")
    if not any(item["active_path"] == ["Main Title", "Second Section"] for item in structure):
        structural_failures.append("missing_second_h2_context")

    return {
        "slice": "S-030",
        "case_count": len(cases),
        "fixed_human_case_ids": sorted(HUMAN_CASE_IDS),
        "summary": {
            "parser_fallback_count": parser_fallback_count,
            "parser_width_violation_count": width_violation_count,
            "protected_span_count": sum(len(spans) for spans in PROTECTED_SPANS.values()),
            "parser_protected_span_split_count": parser_protected_splits,
            "rule_based_protected_span_split_count": rule_protected_splits,
            "structural_failure_count": len(structural_failures),
        },
        "hard_failures": [
            *( [f"parser_fallback_count:{parser_fallback_count}"] if parser_fallback_count else [] ),
            *( [f"parser_width_violation_count:{width_violation_count}"] if width_violation_count else [] ),
            *( [f"parser_protected_span_split_count:{parser_protected_splits}"] if parser_protected_splits else [] ),
            *structural_failures,
        ],
        "cases": cases,
        "structural_fixture": {"text": STRUCTURAL_TEXT, "schedule": structure},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(serialized, encoding="utf-8")
        print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    if args.check:
        if not OUTPUT_PATH.is_file() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            print("S-030 characterization does not match the committed record.")
            return 1
        if report["hard_failures"]:
            print(f"S-030 hard failures: {report['hard_failures']}")
            return 1
        print("S-030 semantic/structural characterization is reproducible and hard invariants pass.")
    if not args.write and not args.check:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
