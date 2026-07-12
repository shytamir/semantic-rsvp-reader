import json
import zipfile
from pathlib import Path

import pytest

from scripts import run_s024_comparison as s024
from semantic_rsvp.chunking.models import Chunk


def test_safe_extract_rejects_path_traversal(tmp_path):
    archive = tmp_path / "bad.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("../escape.txt", "nope")

    with pytest.raises(ValueError, match="unsafe archive path"):
        s024.safe_extract_zip(archive, tmp_path / "out")


def test_internal_hash_validation(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "file.txt").write_text("hello", encoding="utf-8")
    digest = s024.sha256_file(package / "file.txt")
    (package / "SHA256SUMS.txt").write_text(f"{digest}  file.txt\n", encoding="utf-8")

    assert s024.verify_internal_hashes(package) == {"file.txt": digest}


def test_case_annotation_validation_and_boundary_metrics():
    case = {"case_id": "synthetic-1", "text": "Alpha beta gamma.", "text_sha256": s024.sha256_text("Alpha beta gamma.")}
    annotation = {
        "case_id": "synthetic-1",
        "source_sha256": s024.sha256_text("Alpha beta gamma."),
        "boundaries": [
            {"offset": 6, "type": "forbidden", "rationale": "keep pair"},
            {"offset": 11, "type": "required", "rationale": "split before gamma"},
            {"offset": 11, "type": "preferred", "rationale": "rhythm"},
        ],
        "protected_spans": [{"start": 0, "end": 10, "label": "phrase", "rationale": "unit"}],
        "whole_sentence_segmentations": [["Alpha beta", "gamma."]],
    }
    output = s024.SystemOutput(
        "test",
        (
            s024.MappedChunk("Alpha beta", 0, 10, 10, 2),
            s024.MappedChunk("gamma.", 11, 17, 6, 1),
        ),
    )

    assert s024.validate_case_annotation(case, annotation) == []
    metrics = s024.boundary_metrics(annotation, output)
    assert metrics["forbidden"] == {"numerator": 0, "denominator": 1}
    assert metrics["required"] == {"numerator": 1, "denominator": 1}
    assert metrics["preferred"] == {"numerator": 1, "denominator": 1}
    assert metrics["protected_spans"] == {"numerator": 0, "denominator": 1}
    assert metrics["complete_segmentation_match"] is True


def test_chunk_to_source_mapping_and_hard_compliance():
    source = "Alpha beta. Gamma delta."
    chunks = [Chunk("Alpha beta.", 2, 11), Chunk("Gamma delta.", 2, 12)]

    mapped = s024.map_chunks_to_source(source, chunks)
    output = s024.SystemOutput("test", mapped)
    hard = s024.hard_compliance(source, output)

    assert [chunk.start for chunk in mapped] == [0, 12]
    assert hard["source_coverage_failure"] is False
    assert hard["source_ordering_failure"] is False
    assert hard["max_width_violations"] == 0


def test_distribution_and_paired_aggregation():
    case_results = [
        {
            "rule_based": {
                "hard": _hard(),
                "annotation": _annotation(forbidden=1, required=0),
                "distribution": _distribution(total_chunks=3),
                "fallback_used": None,
            },
            "parser_assisted": {
                "hard": _hard(),
                "annotation": _annotation(forbidden=0, required=1),
                "distribution": _distribution(total_chunks=2),
                "fallback_used": False,
            },
        }
    ]

    baseline = s024.aggregate_case_metrics(case_results, "rule_based")
    parser = s024.aggregate_case_metrics(case_results, "parser_assisted")
    paired = s024.paired_summary(case_results)

    assert baseline["annotation_metrics"]["forbidden"]["numerator"] == 1
    assert parser["annotation_metrics"]["required"]["numerator"] == 1
    assert paired["forbidden"]["parser_wins"] == 1
    assert paired["required"]["parser_wins"] == 1
    assert paired["chunk_count"]["parser_fewer_chunks"] == 1


def test_unscorable_mapping_failure_removes_annotation_denominators(monkeypatch):
    case = {
        "case_id": "synthetic-2",
        "text": "Alpha beta.",
        "text_sha256": s024.sha256_text("Alpha beta."),
    }
    item = {
        "case": case,
        "annotation": {
            "case_id": "synthetic-2",
            "source_sha256": s024.sha256_text("Alpha beta."),
            "boundaries": [{"offset": 6, "type": "forbidden", "rationale": "test"}],
            "protected_spans": [{"start": 0, "end": 10, "label": "phrase", "rationale": "test"}],
            "whole_sentence_segmentations": [],
        },
    }
    failed = s024.SystemOutput("rule_based", (), mapping_failure="chunk_mapping_failed")
    ok = s024.SystemOutput("parser_assisted", (s024.MappedChunk("Alpha beta.", 0, 11, 11, 2),), False)
    monkeypatch.setattr(s024, "run_rule_based", lambda source: failed)
    monkeypatch.setattr(s024, "run_parser_assisted", lambda source: ok)

    result = s024.evaluate_cases([item], "synthetic")[0]

    assert result["rule_based"]["annotation"]["forbidden"]["denominator"] == 0
    assert result["rule_based"]["annotation"]["protected_spans"]["denominator"] == 0
    assert result["rule_based"]["hard"]["unsafe_mapping_failure"] is True
    assert result["rule_based"]["hard"]["source_coverage_failure"] is False
    assert result["rule_based"]["hard"]["dropped_text"] is False
    assert result["rule_based"]["hard"]["source_ordering_failure"] is False
    assert result["parser_assisted"]["annotation"]["forbidden"]["denominator"] == 1


def test_ab_packet_keeps_identity_key_separate_and_redaction_check(tmp_path):
    items = [{"case": {"case_id": "blind-1", "text": "Secret source text."}}]
    outputs = {
        "blind-1": {
            "rule_based": s024.SystemOutput("rule_based", (s024.MappedChunk("Secret", 0, 6, 6, 1),)),
            "parser_assisted": s024.SystemOutput("parser_assisted", (s024.MappedChunk("source text.", 7, 19, 12, 2),)),
        }
    }

    record = s024.generate_private_ab_packet(items, outputs, tmp_path)

    review = Path(record["review_packet"])
    key = Path(record["identity_key"])
    assert review.exists()
    assert key.exists()
    assert "rule_based" not in review.read_text(encoding="utf-8")
    assert "parser_assisted" not in review.read_text(encoding="utf-8")
    assert "rule_based" in key.read_text(encoding="utf-8")

    redacted = tmp_path / "redacted.json"
    redacted.write_text(json.dumps({"case_id": "blind-1"}), encoding="utf-8")
    assert s024.redaction_check([redacted], items) == []
    redacted.write_text("Secret source text.", encoding="utf-8")
    assert s024.redaction_check([redacted], items) == ["blind-1"]


def _hard():
    return {
        "source_coverage_failure": False,
        "dropped_text": False,
        "duplicated_text": False,
        "source_ordering_failure": False,
        "structural_boundary_violations": 0,
        "max_width_violations": 0,
        "unsafe_mapping_failure": False,
        "unscorable_reason": None,
    }


def _annotation(forbidden=0, required=0):
    return {
        "forbidden": {"numerator": forbidden, "denominator": 1},
        "protected_spans": {"numerator": 0, "denominator": 1},
        "required": {"numerator": required, "denominator": 1},
        "required_structural": {"numerator": 0, "denominator": 0},
        "preferred": {"numerator": 0, "denominator": 0},
        "acceptable": {"numerator": 0, "denominator": 0},
        "complete_segmentation_match": False,
        "complete_segmentation_denominator": 0,
    }


def _distribution(total_chunks):
    return {
        "total_chunks": total_chunks,
        "mean_chars_per_chunk": 5,
        "median_chars_per_chunk": 5,
        "char_width_distribution": {"5": total_chunks},
        "mean_words_per_chunk": 1,
        "median_words_per_chunk": 1,
        "single_word_chunk_rate": 1,
        "long_chunk_rate": 0,
        "chunks_per_sentence": total_chunks,
        "chunks_per_1000_words": total_chunks * 100,
        "chunks_exceeding_density_target": 0,
    }
