import io
import zipfile
from pathlib import Path


FIXTURE = Path(__file__).parent / "fixtures" / "epub"


def build_epub(*, chapter_suffix=b"", filler_size=0):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        archive.writestr("mimetype", b"application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", (FIXTURE / "container.xml").read_bytes())
        archive.writestr("EPUB/package.opf", (FIXTURE / "package.opf").read_bytes())
        archive.writestr("EPUB/chapter-1.xhtml", (FIXTURE / "chapter-1.xhtml").read_bytes() + chapter_suffix)
        archive.writestr("EPUB/chapter-2.xhtml", (FIXTURE / "chapter-2.xhtml").read_bytes())
        if filler_size:
            archive.writestr("EPUB/unused.bin", b"x" * filler_size, compress_type=zipfile.ZIP_STORED)
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

    assert wrong_type.status_code == 415
    assert wrong_type.get_json()["error"] == "Expected application/epub+zip bytes."
    assert malformed.status_code == 400
    assert "valid ZIP container" in malformed.get_json()["error"]


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


def test_browser_smoke_epub_fixture_matches_required_schedule_schema():
    smoke = (Path(__file__).parents[1] / "scripts" / "run_browser_smoke.mjs").read_text()

    assert "paragraph_index: 0" in smoke
    assert "is_header_chunk: false" in smoke
