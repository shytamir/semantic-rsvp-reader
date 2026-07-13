import hashlib
import io
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

from semantic_rsvp.application.epub_ingestion import ingest_epub_document
from semantic_rsvp.application.epub_preparation import EpubPreparationError, prepare_epub


FIXTURE = Path(__file__).parent / "fixtures" / "epub"
SCRIPT = Path(__file__).parents[1] / "scripts" / "convert_epub_to_demo_subset.py"


def _epub(*, version="3.0", chapters=None, extras=None, encrypted=False):
    chapters = chapters or {
        "EPUB/chapter-1.xhtml": (FIXTURE / "chapter-1.xhtml").read_bytes(),
        "EPUB/chapter-2.xhtml": (FIXTURE / "chapter-2.xhtml").read_bytes(),
    }
    package = (FIXTURE / "package.opf").read_text(encoding="utf-8").replace('version="3.0"', f'version="{version}"').encode()
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        archive.writestr("mimetype", b"application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", (FIXTURE / "container.xml").read_bytes())
        archive.writestr("EPUB/package.opf", package)
        for name, data in chapters.items():
            archive.writestr(name, data)
        for name, data in (extras or {}).items():
            archive.writestr(name, data)
        if encrypted:
            archive.writestr("META-INF/encryption.xml", b"<encryption/>")
    return stream.getvalue()


def test_demo_safe_input_is_exact_byte_preserving_noop():
    source = _epub(extras={"EPUB/unused.bin": b"kept exactly"})
    before = ingest_epub_document(source, source_name="safe.epub")
    result = prepare_epub(source, source_name="safe.epub")
    after = ingest_epub_document(result.data, source_name="renamed.epub")

    assert result.mode == "unchanged"
    assert result.data is source
    assert result.sha256 == hashlib.sha256(source).hexdigest()
    assert result.discarded_resources == 0
    assert result.changes == ()
    assert result.document_id == before.document_id == after.document_id


def test_epub3_normalization_is_deterministic_verified_and_structured():
    chapter = b'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="x.css"><style>x</style></head><body><article style="x"><h1 onclick="x">Opening</h1><p>Hello <a href="https://example.invalid"><em>reader</em></a>.</p><h3>Minor</h3><ul><li>One</li></ul><blockquote>Quoted</blockquote><script>secret</script><svg><text>image</text></svg><img src="x"><math>x</math></article></body></html>'''
    source = _epub(chapters={"EPUB/chapter-1.xhtml": chapter, "EPUB/chapter-2.xhtml": b"<!doctype html><html><body><h2>Continuation</h2><p>Done.</p></body></html>"}, extras={"EPUB/nav.xhtml": b"unused", "EPUB/style.css": b"x"})

    first = prepare_epub(source, source_name="normal.epub")
    second = prepare_epub(source, source_name="normal.epub")
    document = ingest_epub_document(first.data, source_name="normal.epub")
    repeated = prepare_epub(first.data, source_name="normal.epub")

    assert first.mode == second.mode == "normalized"
    assert first.data == second.data
    assert repeated.mode == "unchanged"
    assert repeated.data == first.data
    assert first.document_id == document.document_id == repeated.document_id
    assert [(item.level, item.text) for item in document.structure] == [(1, "Opening"), (2, "Continuation")]
    assert "Minor" in document.text and "secret" not in document.text and "image" not in document.text
    assert first.discarded_resources == 2
    assert {"removed_link", "removed_meta", "removed_style", "removed_script", "removed_svg", "removed_img", "removed_math", "removed_event_handlers", "lower_heading_to_paragraph"} <= set(first.changes)


def test_epub2_legacy_doctype_and_passive_markup_normalize_without_heading_promotion():
    chapter = b'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"><html><body><header><h1>Top</h1></header><section><h4>Lower</h4><p>Body <mark>marked</mark>.</p></section></body></html>'''
    result = prepare_epub(_epub(version="2.0", chapters={"EPUB/chapter-1.xhtml": chapter, "EPUB/chapter-2.xhtml": b"<html><body><p>End.</p></body></html>"}), source_name="legacy.epub")
    document = ingest_epub_document(result.data, source_name="legacy.epub")

    assert result.mode == "normalized"
    assert result.epub_version == "2.0"
    assert [(item.level, item.text) for item in document.structure] == [(1, "Top")]
    assert "Lower" in document.text
    assert {"legacy_doctype", "lower_heading_to_paragraph", "unwrapped_header", "unwrapped_mark"} <= set(result.changes)


@pytest.mark.parametrize(
    ("data", "message"),
    [
        (_epub(encrypted=True), "Encrypted or DRM"),
        (_epub(extras={"../escape": b"unsafe"}), "unsafe or duplicate"),
        (_epub(chapters={"EPUB/chapter-1.xhtml": b"<html><body><table><tr><td>ambiguous</td></tr></table></body></html>", "EPUB/chapter-2.xhtml": b"<html><body><p>end</p></body></html>"}), "ambiguous structured"),
        (b"not zip", "valid ZIP"),
    ],
)
def test_unsafe_ambiguous_and_malformed_inputs_are_bounded_rejections(data, message):
    with pytest.raises(EpubPreparationError, match=message):
        prepare_epub(data, source_name="rejected.epub")


def test_cli_exact_copy_overwrite_protection_normalization_and_failure_cleanup(tmp_path):
    safe = _epub()
    source = tmp_path / "source.epub"
    output = tmp_path / "output.epub"
    source.write_bytes(safe)

    same_path = subprocess.run([sys.executable, str(SCRIPT), str(source), str(source)], capture_output=True, text=True)
    assert same_path.returncode != 0 and "must differ" in same_path.stderr

    first = subprocess.run([sys.executable, str(SCRIPT), str(source), str(output)], capture_output=True, text=True)
    assert first.returncode == 0 and "unchanged" in first.stdout
    assert output.read_bytes() == safe
    protected = subprocess.run([sys.executable, str(SCRIPT), str(source), str(output)], capture_output=True, text=True)
    assert protected.returncode != 0 and "--overwrite" in protected.stderr

    source.write_bytes(_epub(chapters={"EPUB/chapter-1.xhtml": b"<html><head><meta name='x'></head><body><h1>Prepared</h1></body></html>", "EPUB/chapter-2.xhtml": b"<html><body><p>End.</p></body></html>"}))
    normalized = subprocess.run([sys.executable, str(SCRIPT), str(source), str(output), "--overwrite"], capture_output=True, text=True)
    assert normalized.returncode == 0 and "normalized" in normalized.stdout
    ingest_epub_document(output.read_bytes(), source_name="output.epub")

    source.write_bytes(b"broken")
    failed = subprocess.run([sys.executable, str(SCRIPT), str(source), str(output), "--overwrite"], capture_output=True, text=True)
    assert failed.returncode == 1
    assert output.read_bytes() != b"broken"
    assert not list(tmp_path.glob(".output.epub.*.tmp"))
