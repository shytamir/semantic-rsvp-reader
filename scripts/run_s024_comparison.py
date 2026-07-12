from __future__ import annotations

import argparse
import hashlib
import html
import importlib
import json
import math
import platform
import random
import statistics
import subprocess
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from chunking_experiment_common import EXPERIMENT_ROOT, REPO_ROOT, load_cases, manifest_hashes, sha256_file, write_json
except ModuleNotFoundError:
    from scripts.chunking_experiment_common import (
        EXPERIMENT_ROOT,
        REPO_ROOT,
        load_cases,
        manifest_hashes,
        sha256_file,
        write_json,
    )

sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker, tokenize
from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.config import OptimizerConfig
from semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter import (
    PINNED_MODEL_NAME,
    PINNED_MODEL_VERSION,
    PINNED_SPACY_VERSION,
    availability,
)
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences


EXPECTED_ZIP_SHA256 = "a8926e9dc9cd68399f2c9f6a8b63ee44ac0cdd5b4f4361a20460410617b1f71b"
EXPECTED_CANONICAL_SHA256 = "a6647ba26a9e32cfc154bfb904579f57ebdfbef9bdd2b64b7253cfefaa026502"
EXPECTED_BASELINE_COMMIT = "8b50a3049bb5d92a304a03527385c519194ce8da"
EXPECTED_IMPLEMENTATION_COMMIT = "b01085193a36b664b6415686ff835426d0434c92"
EXPECTED_CONFIG_HASH = "0e3266b6917b75da27896b382104ecf164457fee7f28d7e4d835ccb7251accab"
MAX_CHARS = 32

REDACTED_RESULT_PATH = EXPERIMENT_ROOT / "results" / "s024_objective_comparison.json"
RUN_RECORD_PATH = EXPERIMENT_ROOT / "freeze" / "s024_objective_run_record.json"
MARKDOWN_REPORT_PATH = REPO_ROOT / "docs" / "experiments" / "parser_assisted_chunking" / "s024_objective_comparison.md"


@dataclass(frozen=True)
class MappedChunk:
    text: str
    start: int
    end: int
    char_length: int
    content_word_count: int


@dataclass(frozen=True)
class SystemOutput:
    system_id: str
    chunks: tuple[MappedChunk, ...]
    fallback_used: bool | None = None
    fallback_reason: str | None = None
    mapping_failure: str | None = None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_extract_zip(zip_path: Path, output_dir: Path) -> Path:
    archive_root = output_dir.resolve()
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            target = (output_dir / info.filename).resolve()
            if archive_root not in (target, *target.parents):
                raise ValueError(f"unsafe archive path: {info.filename}")
        archive.extractall(output_dir)
    return output_dir / "rsvp_blind_challenge_v1"


def verify_internal_hashes(package_dir: Path) -> dict[str, str]:
    sums_path = package_dir / "SHA256SUMS.txt"
    entries: dict[str, str] = {}
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split(maxsplit=1)
        name = name.strip().lstrip("*")
        actual = sha256_file(package_dir / name)
        if actual.lower() != digest.lower():
            raise ValueError(f"internal hash mismatch for {name}")
        entries[name] = actual
    return entries


def validate_package(zip_path: Path, private_output_dir: Path) -> tuple[Path, dict[str, Any]]:
    zip_hash = sha256_file(zip_path)
    if zip_hash.lower() != EXPECTED_ZIP_SHA256:
        raise ValueError(f"zip sha256 mismatch: {zip_hash}")

    extract_dir = private_output_dir / "extracted"
    extract_dir.mkdir(parents=True, exist_ok=True)
    package_dir = safe_extract_zip(zip_path, extract_dir)

    canonical_path = package_dir / "sealed_blind_set.json"
    canonical_hash = sha256_file(canonical_path)
    if canonical_hash.lower() != EXPECTED_CANONICAL_SHA256:
        raise ValueError(f"canonical sha256 mismatch: {canonical_hash}")

    internal_hashes = verify_internal_hashes(package_dir)
    validator = package_dir / "validate_sealed_blind_set.py"
    validation = subprocess.run(
        [sys.executable, str(validator), str(canonical_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    sealed = load_json(canonical_path)
    metadata = sealed.get("metadata", {})
    if metadata.get("case_count") != 16 or len(sealed.get("cases", [])) != 16:
        raise ValueError("sealed package did not contain 16 cases")
    if metadata.get("baseline_commit") != EXPECTED_BASELINE_COMMIT:
        raise ValueError("sealed package baseline commit mismatch")
    if metadata.get("max_chars") != MAX_CHARS:
        raise ValueError("sealed package max_chars mismatch")

    return package_dir, {
        "zip_sha256": zip_hash,
        "canonical_sha256": canonical_hash,
        "internal_hashes": internal_hashes,
        "validator_stdout": validation.stdout.strip(),
        "case_count": len(sealed.get("cases", [])),
        "package_metadata": {
            "package_id": metadata.get("package_id"),
            "language": metadata.get("language"),
            "max_chars": metadata.get("max_chars"),
            "baseline_commit": metadata.get("baseline_commit"),
            "visibility": metadata.get("visibility"),
            "methodological_note": metadata.get("methodological_note"),
        },
    }


def validate_case_annotation(case: dict[str, Any], annotation: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    text = case["text"]
    if case.get("text_sha256") and case["text_sha256"] != sha256_text(text):
        failures.append("case_text_sha256_mismatch")
    if annotation.get("source_sha256") and annotation["source_sha256"] != sha256_text(text):
        failures.append("annotation_source_sha256_mismatch")
    if case["case_id"] != annotation.get("case_id"):
        failures.append("case_annotation_id_mismatch")
    for boundary in annotation.get("boundaries", []):
        if not 0 <= boundary["offset"] <= len(text):
            failures.append("boundary_offset_out_of_range")
    for span in annotation.get("protected_spans", []):
        if not 0 <= span["start"] < span["end"] <= len(text):
            failures.append("protected_span_out_of_range")
    return failures


def sentence_spans(normalized: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    cursor = 0
    for sentence in split_sentences(normalized):
        start = normalized.find(sentence, cursor)
        if start == -1:
            raise ValueError("sentence_mapping_failed")
        end = start + len(sentence)
        spans.append((start, end, sentence))
        cursor = end
    return spans


def map_chunks_to_source(source: str, chunks: list[Chunk], start_offset: int = 0) -> tuple[MappedChunk, ...]:
    mapped: list[MappedChunk] = []
    cursor = start_offset
    for chunk in chunks:
        while cursor < len(source) and source[cursor].isspace():
            cursor += 1
        start = source.find(chunk.text, cursor)
        if start == -1:
            raise ValueError(f"chunk_mapping_failed:{sha256_text(chunk.text)}")
        end = start + len(chunk.text)
        if source[start:end] != chunk.text:
            raise ValueError("chunk_text_mismatch")
        mapped.append(MappedChunk(chunk.text, start, end, len(chunk.text), chunk.content_word_count))
        cursor = end
    return tuple(mapped)


def run_rule_based(source: str) -> SystemOutput:
    chunker = RuleBasedChunker(max_chars=MAX_CHARS, max_content_words=2)
    mapped: list[MappedChunk] = []
    try:
        for start, _end, sentence in sentence_spans(source):
            mapped.extend(map_chunks_to_source(source, chunker.chunk_sentence(sentence), start))
        return SystemOutput("rule_based", tuple(mapped), fallback_used=None)
    except ValueError as exc:
        return SystemOutput("rule_based", (), fallback_used=None, mapping_failure=str(exc).split(":", 1)[0])


def run_parser_assisted(source: str) -> SystemOutput:
    chunker = ParserAssistedChunker()
    mapped: list[MappedChunk] = []
    fallback = False
    reasons: set[str] = set()
    try:
        for start, _end, sentence in sentence_spans(source):
            result = chunker.chunk_sentence_with_trace(sentence)
            fallback = fallback or result.optimization.fallback_used
            if result.optimization.fallback_reason:
                reasons.add(result.optimization.fallback_reason.split(":", 1)[0])
            mapped.extend(map_chunks_to_source(source, list(result.chunks), start))
        return SystemOutput("parser_assisted", tuple(mapped), fallback, ";".join(sorted(reasons)) or None)
    except ValueError as exc:
        return SystemOutput("parser_assisted", (), fallback, ";".join(sorted(reasons)) or None, str(exc).split(":", 1)[0])


def predicted_boundaries(output: SystemOutput) -> set[int]:
    return {chunk.start for chunk in output.chunks[1:]}


def structural_boundaries(source: str) -> set[int]:
    return {start for start, _end, _sentence in sentence_spans(source)[1:]}


def hard_compliance(source: str, output: SystemOutput) -> dict[str, Any]:
    if output.mapping_failure:
        return {
            "source_coverage_failure": False,
            "dropped_text": False,
            "duplicated_text": False,
            "source_ordering_failure": False,
            "structural_boundary_violations": 0,
            "max_width_violations": 0,
            "unsafe_mapping_failure": True,
            "unscorable_reason": output.mapping_failure,
        }
    chunks = output.chunks
    ordered = all(chunks[index].end <= chunks[index + 1].start for index in range(len(chunks) - 1))
    covered = "".join(chunk.text for chunk in chunks)
    source_non_ws = "".join(char for char in source if not char.isspace())
    covered_non_ws = "".join(char for char in covered if not char.isspace())
    structural_missing = sorted(structural_boundaries(source) - predicted_boundaries(output))
    width_violations = [
        chunk.char_length
        for chunk in chunks
        if chunk.char_length > MAX_CHARS and not _has_unsplittable_long_token(chunk.text, MAX_CHARS)
    ]
    return {
        "source_coverage_failure": covered_non_ws != source_non_ws,
        "dropped_text": covered_non_ws != source_non_ws,
        "duplicated_text": len({(chunk.start, chunk.end) for chunk in chunks}) != len(chunks),
        "source_ordering_failure": not ordered,
        "structural_boundary_violations": len(structural_missing),
        "max_width_violations": len(width_violations),
        "unsafe_mapping_failure": False,
        "unscorable_reason": None,
    }


def _has_unsplittable_long_token(text: str, max_chars: int) -> bool:
    return any(len(token.strip(".,!?;:\"'()[]")) > max_chars for token in tokenize(text))


def boundary_metrics(annotation: dict[str, Any], output: SystemOutput) -> dict[str, Any]:
    boundaries = predicted_boundaries(output)
    grouped = {"forbidden": [], "required": [], "required_structural": [], "preferred": [], "acceptable": []}
    for item in annotation.get("boundaries", []):
        grouped[item["type"]].append(item["offset"])

    protected = annotation.get("protected_spans", [])
    split_spans = [span for span in protected if any(span["start"] < boundary < span["end"] for boundary in boundaries)]
    whole = annotation.get("whole_sentence_segmentations", [])
    output_texts = [chunk.text for chunk in output.chunks]
    return {
        "forbidden": {"numerator": sum(1 for offset in grouped["forbidden"] if offset in boundaries), "denominator": len(grouped["forbidden"])},
        "protected_spans": {"numerator": len(split_spans), "denominator": len(protected)},
        "required": {"numerator": sum(1 for offset in grouped["required"] if offset in boundaries), "denominator": len(grouped["required"])},
        "required_structural": {
            "numerator": sum(1 for offset in grouped["required_structural"] if offset in boundaries),
            "denominator": len(grouped["required_structural"]),
        },
        "preferred": {"numerator": sum(1 for offset in grouped["preferred"] if offset in boundaries), "denominator": len(grouped["preferred"])},
        "acceptable": {"numerator": sum(1 for offset in grouped["acceptable"] if offset in boundaries), "denominator": len(grouped["acceptable"])},
        "complete_segmentation_match": any(output_texts == segmentation for segmentation in whole),
        "complete_segmentation_denominator": len(whole),
    }


def distribution(source: str, output: SystemOutput) -> dict[str, Any]:
    chunks = list(output.chunks)
    lengths = [chunk.char_length for chunk in chunks]
    word_counts = [len([token for token in tokenize(chunk.text) if any(char.isalnum() for char in token)]) for chunk in chunks]
    total_words = max(1, len([token for token in tokenize(source) if any(char.isalnum() for char in token)]))
    sentence_count = max(1, len(sentence_spans(source)))
    return {
        "total_chunks": len(chunks),
        "mean_chars_per_chunk": round(statistics.mean(lengths), 3) if lengths else 0,
        "median_chars_per_chunk": round(statistics.median(lengths), 3) if lengths else 0,
        "char_width_distribution": {str(width): lengths.count(width) for width in sorted(set(lengths))},
        "mean_words_per_chunk": round(statistics.mean(word_counts), 3) if word_counts else 0,
        "median_words_per_chunk": round(statistics.median(word_counts), 3) if word_counts else 0,
        "single_word_chunk_rate": _rate(sum(1 for count in word_counts if count == 1), len(word_counts)),
        "long_chunk_rate": _rate(sum(1 for length in lengths if length > 26), len(lengths)),
        "chunks_per_sentence": round(len(chunks) / sentence_count, 3),
        "chunks_per_1000_words": round(len(chunks) / total_words * 1000, 3),
        "chunks_exceeding_density_target": sum(1 for chunk in chunks if chunk.content_word_count > 2),
    }


def _rate(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator, 6)


def aggregate_case_metrics(case_results: list[dict[str, Any]], system_id: str) -> dict[str, Any]:
    system_cases = [case[system_id] for case in case_results]
    hard_keys = [
        "source_coverage_failure",
        "dropped_text",
        "duplicated_text",
        "source_ordering_failure",
        "structural_boundary_violations",
        "max_width_violations",
        "unsafe_mapping_failure",
    ]
    totals: dict[str, Any] = {
        "evaluated_cases": len(system_cases),
        "unscorable_cases": sum(1 for case in system_cases if case["hard"]["unscorable_reason"]),
        "hard_compliance": {},
        "annotation_metrics": {},
        "distribution": {},
    }
    for key in hard_keys:
        totals["hard_compliance"][key] = sum(
            int(bool(case["hard"][key])) if isinstance(case["hard"][key], bool) else case["hard"][key]
            for case in system_cases
        )

    metric_names = ["forbidden", "protected_spans", "required", "required_structural", "preferred", "acceptable"]
    for name in metric_names:
        numerator = sum(case["annotation"][name]["numerator"] for case in system_cases)
        denominator = sum(case["annotation"][name]["denominator"] for case in system_cases)
        totals["annotation_metrics"][name] = {"numerator": numerator, "denominator": denominator, "rate": _rate(numerator, denominator)}
    match_count = sum(1 for case in system_cases if case["annotation"]["complete_segmentation_match"])
    whole_denominator = sum(1 for case in system_cases if case["annotation"]["complete_segmentation_denominator"])
    totals["annotation_metrics"]["complete_segmentation_match"] = {
        "numerator": match_count,
        "denominator": whole_denominator,
        "rate": _rate(match_count, whole_denominator),
    }

    for key in ["total_chunks", "chunks_exceeding_density_target"]:
        totals["distribution"][key] = sum(case["distribution"][key] for case in system_cases)
    for key in [
        "mean_chars_per_chunk",
        "median_chars_per_chunk",
        "mean_words_per_chunk",
        "median_words_per_chunk",
        "single_word_chunk_rate",
        "long_chunk_rate",
        "chunks_per_sentence",
        "chunks_per_1000_words",
    ]:
        values = [case["distribution"][key] for case in system_cases if case["distribution"][key] is not None]
        totals["distribution"][key] = round(statistics.mean(values), 6) if values else None
    char_distribution: dict[str, int] = {}
    for case in system_cases:
        for width, count in case["distribution"]["char_width_distribution"].items():
            char_distribution[width] = char_distribution.get(width, 0) + count
    totals["distribution"]["char_width_distribution"] = dict(sorted(char_distribution.items(), key=lambda item: int(item[0])))
    if system_id == "parser_assisted":
        fallback_cases = sum(1 for case in system_cases if case["fallback_used"])
        totals["fallback"] = {"cases": fallback_cases, "rate": _rate(fallback_cases, len(system_cases))}
    else:
        totals["fallback"] = {"cases": None, "rate": None}
    return totals


def paired_summary(case_results: list[dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    metric_names = ["forbidden", "protected_spans", "required", "required_structural", "preferred", "acceptable"]
    lower_is_better = {"forbidden", "protected_spans"}
    for metric in metric_names:
        p_wins = b_wins = ties = 0
        for case in case_results:
            baseline = case["rule_based"]["annotation"][metric]
            parser = case["parser_assisted"]["annotation"][metric]
            if baseline["denominator"] == 0 or parser["denominator"] == 0:
                ties += 1
                continue
            baseline_rate = baseline["numerator"] / baseline["denominator"]
            parser_rate = parser["numerator"] / parser["denominator"]
            if math.isclose(baseline_rate, parser_rate):
                ties += 1
            elif metric in lower_is_better:
                p_wins += int(parser_rate < baseline_rate)
                b_wins += int(baseline_rate < parser_rate)
            else:
                p_wins += int(parser_rate > baseline_rate)
                b_wins += int(baseline_rate > parser_rate)
        summary[metric] = {"parser_wins": p_wins, "baseline_wins": b_wins, "ties": ties}

    fewer = more = identical = 0
    for case in case_results:
        baseline_count = case["rule_based"]["distribution"]["total_chunks"]
        parser_count = case["parser_assisted"]["distribution"]["total_chunks"]
        fewer += int(parser_count < baseline_count)
        more += int(parser_count > baseline_count)
        identical += int(parser_count == baseline_count)
    summary["chunk_count"] = {
        "parser_fewer_chunks": fewer,
        "parser_more_chunks": more,
        "identical_chunk_count": identical,
    }
    return summary


def evaluate_cases(cases: list[dict[str, Any]], corpus: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for item in cases:
        case = item["case"] if "case" in item else item
        annotation = item.get("annotation", _empty_annotation(case["case_id"], case["text"]))
        normalized = normalize_text(case["text"])
        validation_failures = validate_case_annotation(case, annotation)
        outputs = {
            "rule_based": run_rule_based(normalized),
            "parser_assisted": run_parser_assisted(normalized),
        }
        case_result: dict[str, Any] = {
            "case_id": case["case_id"],
            "corpus": corpus,
            "source_sha256": sha256_text(case["text"]),
            "normalized_identical": normalized == case["text"],
            "annotation_validation_failures": validation_failures,
        }
        for system_id, output in outputs.items():
            case_result[system_id] = {
                "chunk_count": len(output.chunks),
                "fallback_used": output.fallback_used,
                "fallback_reason": output.fallback_reason,
                "hard": hard_compliance(normalized, output),
                "annotation": _unscorable_boundary_metrics() if output.mapping_failure else boundary_metrics(annotation, output),
                "distribution": distribution(normalized, output),
            }
        results.append(case_result)
    return results


def _empty_annotation(case_id: str, text: str) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "source_sha256": sha256_text(text),
        "boundaries": [],
        "protected_spans": [],
        "whole_sentence_segmentations": [],
    }


def _unscorable_boundary_metrics() -> dict[str, Any]:
    empty = {"numerator": 0, "denominator": 0}
    return {
        "forbidden": dict(empty),
        "protected_spans": dict(empty),
        "required": dict(empty),
        "required_structural": dict(empty),
        "preferred": dict(empty),
        "acceptable": dict(empty),
        "complete_segmentation_match": False,
        "complete_segmentation_denominator": 0,
    }


def summarize_corpus(case_results: list[dict[str, Any]], corpus: str) -> dict[str, Any]:
    return {
        "corpus": corpus,
        "case_count": len(case_results),
        "rule_based": aggregate_case_metrics(case_results, "rule_based"),
        "parser_assisted": aggregate_case_metrics(case_results, "parser_assisted"),
        "paired": paired_summary(case_results),
    }


def generate_private_ab_packet(blind_items: list[dict[str, Any]], outputs_by_case: dict[str, dict[str, SystemOutput]], private_output_dir: Path) -> dict[str, Any]:
    seed = random.SystemRandom().randrange(1, 2**63)
    rng = random.Random(seed)
    assignments: dict[str, dict[str, str]] = {}
    response_cases: list[dict[str, Any]] = []
    sections: list[str] = []
    for item in blind_items:
        case = item["case"]
        case_id = case["case_id"]
        systems = ["rule_based", "parser_assisted"]
        rng.shuffle(systems)
        labels = {"A": systems[0], "B": systems[1]}
        assignments[case_id] = labels
        response_cases.append({"case_id": case_id, "choice": None, "confidence": None, "note": ""})
        rows = []
        for label in ["A", "B"]:
            chunks = outputs_by_case[case_id][labels[label]].chunks
            rows.append(
                f"<section><h3>Output {label}</h3><ol>"
                + "".join(f"<li>{html.escape(chunk.text)}</li>" for chunk in chunks)
                + "</ol></section>"
            )
        sections.append(
            f"<article><h2>{html.escape(case_id)}</h2>"
            f"<h3>Source passage</h3><p>{html.escape(case['text'])}</p>"
            + "".join(rows)
            + "<p>Choice: A / B / equivalent / both poor<br>Confidence: low / medium / high<br>Optional note:</p>"
            + "</article>"
        )
    html_doc = (
        "<!doctype html><html><head><meta charset='utf-8'><title>S-024 Blind A/B Review</title>"
        "<style>body{font-family:Arial,sans-serif;line-height:1.45;max-width:900px;margin:32px auto;padding:0 16px}"
        "article{border-top:1px solid #ccc;padding:24px 0}li{margin:4px 0}</style></head><body>"
        "<h1>S-024 Blind A/B Review</h1><p>For each case, choose A, B, equivalent, or both poor. "
        "System identities are intentionally hidden.</p>"
        + "".join(sections)
        + "</body></html>"
    )
    review_path = private_output_dir / "blind_ab_review.html"
    response_path = private_output_dir / "blind_ab_response_template.json"
    key_path = private_output_dir / "blind_ab_identity_key.json"
    review_path.write_text(html_doc, encoding="utf-8")
    write_private_json(response_path, {"cases": response_cases, "allowed_choices": ["A", "B", "equivalent", "both poor"], "confidence": ["low", "medium", "high"]})
    write_private_json(key_path, {"seed": seed, "assignments": assignments})
    return {
        "review_packet": str(review_path),
        "response_template": str(response_path),
        "identity_key": str(key_path),
        "case_count": len(blind_items),
    }


def write_private_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def redaction_check(paths: list[Path], blind_items: list[dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    contents = "\n".join(path.read_text(encoding="utf-8") for path in paths if path.exists())
    for item in blind_items:
        source = item["case"]["text"]
        if source and source in contents:
            failures.append(item["case"]["case_id"])
    return failures


def directory_size_mb(path: Path) -> float:
    total = sum(child.stat().st_size for child in path.rglob("*") if child.is_file())
    return round(total / (1024 * 1024), 2)


def operational_measurements(private_case_inputs: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    import spacy

    start = time.perf_counter()
    spacy.load(PINNED_MODEL_NAME)
    parser_init_ms = round((time.perf_counter() - start) * 1000, 3)

    spacy_module = importlib.import_module("spacy")
    model_module = importlib.import_module("en_core_web_sm")
    case_count = sum(len(items) for items in private_case_inputs.values())
    char_count = sum(
        len(normalize_text((item["case"] if "case" in item else item)["text"]))
        for items in private_case_inputs.values()
        for item in items
    )
    return {
        "parser_initialization_latency_ms": parser_init_ms,
        "spacy_package_footprint_mb": directory_size_mb(Path(spacy_module.__file__).parent),
        "model_footprint_mb": directory_size_mb(Path(model_module.__file__).parent),
        "case_count": case_count,
        "normalized_character_count": char_count,
    }


def build_markdown_report(payload: dict[str, Any]) -> str:
    lines = [
        "# S-024 Objective Comparison",
        "",
        "This report contains repository-safe, redacted objective evidence only. It does not include blind source text, annotations, raw chunks, parser traces, or the A/B identity key.",
        "",
        "The blind challenge set was revealed only after the S-023 implementation freeze. The set is synthetic and model-authored; it is useful for held-out boundary checks but does not establish human preference or broad real-world superiority by itself.",
        "",
        "## Frozen Identities",
        "",
        f"- S-023 implementation commit: `{payload['metadata']['implementation_commit']}`",
        f"- Configuration hash: `{payload['metadata']['config_hash']}`",
        f"- ZIP SHA-256: `{payload['package']['zip_sha256']}`",
        f"- Canonical SHA-256: `{payload['package']['canonical_sha256']}`",
        "",
        "## Corpus Summaries",
        "",
    ]
    for corpus, summary in payload["summaries"].items():
        lines.extend(
            [
                f"### {corpus.title()}",
                "",
                f"- Cases: {summary['case_count']}",
                f"- Rule-based forbidden violations: {summary['rule_based']['annotation_metrics']['forbidden']}",
                f"- Parser-assisted forbidden violations: {summary['parser_assisted']['annotation_metrics']['forbidden']}",
                f"- Rule-based protected-span splits: {summary['rule_based']['annotation_metrics']['protected_spans']}",
                f"- Parser-assisted protected-span splits: {summary['parser_assisted']['annotation_metrics']['protected_spans']}",
                f"- Rule-based required-boundary recall: {summary['rule_based']['annotation_metrics']['required']}",
                f"- Parser-assisted required-boundary recall: {summary['parser_assisted']['annotation_metrics']['required']}",
                f"- Parser fallback: {summary['parser_assisted']['fallback']}",
                f"- Rule-based hard compliance: {summary['rule_based']['hard_compliance']}",
                f"- Parser-assisted hard compliance: {summary['parser_assisted']['hard_compliance']}",
                f"- Rule-based distribution: {summary['rule_based']['distribution']}",
                f"- Parser-assisted distribution: {summary['parser_assisted']['distribution']}",
                f"- Paired chunk-count behavior: {summary['paired']['chunk_count']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Interpretation Boundary",
            "",
            "No production disposition is made here. S-024 remains pending human A/B review; S-025 owns any later promotion, revision, or abandonment decision.",
            "",
        ]
    )
    return "\n".join(lines)


def run_comparison(zip_path: Path, private_output_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    package_dir, package_record = validate_package(zip_path, private_output_dir)
    sealed = load_json(package_dir / "sealed_blind_set.json")
    blind_items = sealed["cases"]

    available, reason = availability()
    if not available:
        raise RuntimeError(f"pinned NLP environment unavailable: {reason}")
    if OptimizerConfig().stable_hash() != EXPECTED_CONFIG_HASH:
        raise RuntimeError("configuration hash mismatch")

    start_all = time.perf_counter()
    visible_cases = load_cases()
    corpus_inputs = {
        "regression": [{"case": case} for case in visible_cases if case["corpus"] == "regression"],
        "generalization": [{"case": case} for case in visible_cases if case["corpus"] == "generalization"],
        "blind": blind_items,
    }
    operational = operational_measurements(corpus_inputs)
    case_results = {corpus: evaluate_cases(items, corpus) for corpus, items in corpus_inputs.items()}
    summaries = {corpus: summarize_corpus(results, corpus) for corpus, results in case_results.items()}

    outputs_by_case: dict[str, dict[str, SystemOutput]] = {}
    for item in blind_items:
        source = normalize_text(item["case"]["text"])
        outputs_by_case[item["case"]["case_id"]] = {
            "rule_based": run_rule_based(source),
            "parser_assisted": run_parser_assisted(source),
        }
    ab_record = generate_private_ab_packet(blind_items, outputs_by_case, private_output_dir)

    payload = {
        "metadata": {
            "slice": "S-024",
            "implementation_commit": EXPECTED_IMPLEMENTATION_COMMIT,
            "baseline_commit": EXPECTED_BASELINE_COMMIT,
            "production_default": "semantic_rsvp.chunking.rules.RuleBasedChunker",
            "experimental_entry_point": "semantic_rsvp.experiments.parser_assisted_chunking.chunker.ParserAssistedChunker",
            "config_version": OptimizerConfig().version,
            "config_hash": OptimizerConfig().stable_hash(),
            "spacy_version": PINNED_SPACY_VERSION,
            "model_name": PINNED_MODEL_NAME,
            "model_version": PINNED_MODEL_VERSION,
            "manifest_hashes": manifest_hashes(),
            "visibility_note": "Regression and generalization inputs were repository-visible before S-023; blind material was held out until after freeze.",
        },
        "package": {
            "zip_sha256": package_record["zip_sha256"],
            "canonical_sha256": package_record["canonical_sha256"],
            "internal_hash_entry_count": len(package_record["internal_hashes"]),
            "validator_result": package_record["validator_stdout"],
            "package_metadata": package_record["package_metadata"],
        },
        "summaries": summaries,
        "cases": case_results,
        "human_ab_packet": {
            "private_review_packet_created": True,
            "case_count": ab_record["case_count"],
            "identity_key_committed": False,
        },
    }
    run_record = {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "total_elapsed_ms": round((time.perf_counter() - start_all) * 1000, 3),
        "average_case_latency_ms": round((time.perf_counter() - start_all) * 1000 / operational["case_count"], 3),
        "latency_ms_per_1000_chars": round((time.perf_counter() - start_all) * 1000 / operational["normalized_character_count"] * 1000, 3),
        "parser_initialization_latency_ms": operational["parser_initialization_latency_ms"],
        "spacy_package_footprint_mb": operational["spacy_package_footprint_mb"],
        "model_footprint_mb": operational["model_footprint_mb"],
        "normalized_character_count": operational["normalized_character_count"],
        "private_output_dir": str(private_output_dir),
        "ab_review_packet": ab_record["review_packet"],
        "ab_response_template": ab_record["response_template"],
        "ab_identity_key_created": True,
        "ab_identity_key_committed": False,
    }
    return payload, run_record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sealed-package", required=True, type=Path)
    parser.add_argument("--private-output-dir", required=True, type=Path)
    parser.add_argument("--write-redacted-results", action="store_true")
    args = parser.parse_args(argv)

    payload, run_record = run_comparison(args.sealed_package, args.private_output_dir)
    if args.write_redacted_results:
        write_json(REDACTED_RESULT_PATH, payload)
        write_json(RUN_RECORD_PATH, run_record)
        MARKDOWN_REPORT_PATH.write_text(build_markdown_report(payload), encoding="utf-8")
        blind_items = load_json(args.private_output_dir / "extracted" / "rsvp_blind_challenge_v1" / "sealed_blind_set.json")["cases"]
        failures = redaction_check([REDACTED_RESULT_PATH, RUN_RECORD_PATH, MARKDOWN_REPORT_PATH], blind_items)
        if failures:
            raise RuntimeError(f"redaction check failed for cases: {', '.join(failures)}")
        print(f"Wrote {REDACTED_RESULT_PATH.relative_to(REPO_ROOT)}")
        print(f"Wrote {RUN_RECORD_PATH.relative_to(REPO_ROOT)}")
        print(f"Wrote {MARKDOWN_REPORT_PATH.relative_to(REPO_ROOT)}")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
