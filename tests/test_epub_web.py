import io
import zipfile
from pathlib import Path
from types import SimpleNamespace

from semantic_rsvp.application.epub_ingestion import ingest_epub_document
from semantic_rsvp.web import create_app


FIXTURE = Path(__file__).parent / "fixtures" / "epub"


def build_epub(*, chapter_suffix=b"", filler_size=0, chapters=None, encrypted=False):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        archive.writestr("mimetype", b"application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", (FIXTURE / "container.xml").read_bytes())
        archive.writestr("EPUB/package.opf", (FIXTURE / "package.opf").read_bytes())
        chapters = chapters or {
            "EPUB/chapter-1.xhtml": (FIXTURE / "chapter-1.xhtml").read_bytes() + chapter_suffix,
            "EPUB/chapter-2.xhtml": (FIXTURE / "chapter-2.xhtml").read_bytes(),
        }
        for name, data in chapters.items():
            archive.writestr(name, data)
        if filler_size:
            archive.writestr("EPUB/unused.bin", b"x" * filler_size, compress_type=zipfile.ZIP_STORED)
        if encrypted:
            archive.writestr("META-INF/encryption.xml", b"<encryption/>")
    return stream.getvalue()


def post_epub(client, data, name="book.epub", content_type="application/epub+zip"):
    return client.post(
        "/api/epub/schedule",
        data=data,
        content_type=content_type,
        headers={"X-EPUB-Filename": name},
    )


def test_epub_schedule_returns_canonical_identity_and_existing_schedule(client):
    response = post_epub(client, build_epub(), "renamed.epub")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["document"]["source_type"] == "epub"
    assert payload["document"]["display_name"] == "Project Fixture"
    assert payload["document"]["source_name"] == "renamed.epub"
    assert len(payload["document"]["document_id"]) == 64
    assert payload["schedule"]
    assert payload["schedule"][-1]["navigation"]["progress_percent"] == 100
    assert payload["preparation"] == {
        "changes": [],
        "discarded_resources": 0,
        "epub_version": "3.0",
        "mode": "unchanged",
    }


def test_epub_route_prepares_raw_bytes_before_final_ingestion():
    raw = build_epub()
    prepared = build_epub(chapter_suffix=b" Prepared.")
    calls = []

    def preparer(data, *, source_name):
        calls.append(("prepare", data, source_name))
        return SimpleNamespace(
            data=prepared,
            mode="normalized",
            epub_version="3.0",
            discarded_resources=1,
            changes=("removed_meta",),
        )

    def ingestor(data, *, source_name):
        calls.append(("ingest", data, source_name))
        assert data is prepared
        return ingest_epub_document(data, source_name=source_name)

    app = create_app({
        "TESTING": True,
        "RSVP_CHUNKER_MODE": "rule_based",
        "EPUB_PREPARER": preparer,
        "EPUB_INGESTOR": ingestor,
    })
    response = post_epub(app.test_client(), raw, "ordered.epub")

    assert response.status_code == 200
    assert calls == [("prepare", raw, "ordered.epub"), ("ingest", prepared, "ordered.epub")]
    assert response.get_json()["preparation"]["mode"] == "normalized"


def test_normalized_epub_path_is_stable_and_returns_no_archive_bytes(client):
    chapter = b'''<!DOCTYPE html PUBLIC "legacy"><html><head><meta charset="utf-8"><link rel="stylesheet" href="book.css"></head><body style="x"><h1>Prepared</h1><p>Readable text.</p></body></html>'''
    chapters = {
        "EPUB/chapter-1.xhtml": chapter,
        "EPUB/chapter-2.xhtml": b"<html><body><h2>Continuation</h2><p>Done.</p></body></html>",
    }
    source = build_epub(chapters=chapters)
    first = post_epub(client, source, "first.epub")
    renamed = post_epub(client, source, "renamed.epub")
    payload = first.get_json()

    assert first.status_code == renamed.status_code == 200
    assert payload["preparation"]["mode"] == "normalized"
    assert {"legacy_doctype", "removed_link", "removed_meta", "removed_attributes"} <= set(payload["preparation"]["changes"])
    assert payload["document"]["document_id"] == renamed.get_json()["document"]["document_id"]
    assert set(payload["preparation"]) == {"mode", "epub_version", "discarded_resources", "changes"}
    assert "application/epub+zip" not in str(payload)


def test_epub_identity_ignores_filename_but_changes_with_extracted_text(client):
    first = post_epub(client, build_epub(), "first.epub").get_json()["document"]["document_id"]
    renamed = post_epub(client, build_epub(), "second.epub").get_json()["document"]["document_id"]
    changed = post_epub(
        client,
        build_epub(chapter_suffix=b" Changed."),
        "first.epub",
    ).get_json()["document"]["document_id"]

    assert first == renamed
    assert changed != first


def test_dedicated_epub_boundary_does_not_raise_global_json_limit(client):
    response = post_epub(client, build_epub(filler_size=1_100_000))
    assert response.status_code == 200

    oversized_json = client.post(
        "/api/schedule",
        data=b'{}' + b" " * 1_100_000,
        content_type="application/json",
    )
    assert oversized_json.status_code == 413


def test_epub_boundary_reports_media_type_and_ingestion_failures(client):
    wrong_type = post_epub(client, build_epub(), content_type="application/octet-stream")
    malformed = post_epub(client, b"not an epub")
    encrypted = post_epub(client, build_epub(encrypted=True))

    assert wrong_type.status_code == 415
    assert wrong_type.get_json()["error"] == "Expected application/epub+zip bytes."
    assert malformed.status_code == 400
    assert "valid ZIP container" in malformed.get_json()["error"]
    assert encrypted.status_code == 400
    assert "Encrypted or DRM" in encrypted.get_json()["error"]


def test_browser_uses_server_epub_identity_without_persisting_source(client):
    html = client.get("/").data
    javascript = client.get("/static/js/app.js").data.decode("utf-8")
    continuity = client.get("/static/js/continuity.js").data.decode("utf-8")

    assert b'id="epub-input"' in html
    assert b'accept=".epub,application/epub+zip"' in html
    assert 'fetch("/api/epub/schedule"' in javascript
    assert "document.document_id" in javascript
    assert "computeDocumentId(file" not in javascript
    assert "source_text" not in continuity
    assert "epub_bytes" not in continuity
    assert "preparation.data" not in javascript


def test_browser_smoke_epub_fixture_matches_required_schedule_schema():
    smoke = (Path(__file__).parents[1] / "scripts" / "run_browser_smoke.mjs").read_text()

    assert "paragraph_index: 0" in smoke
    assert "is_header_chunk: false" in smoke
