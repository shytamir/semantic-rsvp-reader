def test_reader_exposes_accessible_bounded_contents_controls(client):
    html = client.get("/").data
    css = client.get("/static/css/app.css").data.decode("utf-8")

    assert b'id="contents-panel"' in html
    assert b'aria-label="Document contents"' in html
    assert b'id="contents-empty"' in html
    assert b"No supported H1/H2 headings." in html
    assert ".contents-list" in css
    assert "max-height: min(32vh, 240px)" in css
    assert "max-width: 100%" in css


def test_contents_uses_existing_structure_and_paused_navigation_contract(client):
    javascript = client.get("/static/js/app.js").data.decode("utf-8")

    assert "structure.is_header_chunk" in javascript
    assert "structure.header_level" in javascript
    assert "structure.active_h1" in javascript
    assert "structure.active_h2" in javascript
    assert 'currentDocumentSourceType !== "epub"' in javascript
    assert 'cancelPendingDriftRecovery("contents_jump")' in javascript
    assert "pause({ record: false, render: false })" in javascript
    assert "renderCurrentChunk()" in javascript
    assert "updateProgressAnchor({ force: true })" in javascript
    assert 'recordSessionEvent("contents_jump"' in javascript
    assert "persistCurrentDocumentContinuity" in javascript


def test_contents_does_not_add_epub_navigation_parsing_or_playback_policy(client):
    javascript = client.get("/static/js/app.js").data.decode("utf-8")

    assert "nav.xhtml" not in javascript
    assert "toc.ncx" not in javascript
    assert "epub_navigation" not in javascript
