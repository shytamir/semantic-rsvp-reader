def test_index_includes_static_assets(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b'name="viewport"' in response.data
    assert b"app.css" in response.data
    assert b"app.js" in response.data


def test_index_includes_reader_and_input_ids(client):
    response = client.get("/")

    assert response.status_code == 200
    for marker in [
        b'id="input-mode"',
        b'id="reader-mode"',
        b'id="schedule-form"',
        b'id="text-input"',
        b'id="status-message"',
        b'id="reader-area"',
        b'id="chunk-display"',
        b'id="speed-overlay"',
        b'id="speed-label"',
        b'id="speed-slower"',
        b'id="speed-faster"',
        b'id="speed-reset"',
        b'id="speed-close"',
        b'id="adaptation-toggle"',
        b'id="adaptation-status"',
        b'id="adaptation-reset"',
        b'id="adaptation-count"',
        b'id="session-debug"',
        b'id="session-event-count"',
        b'id="session-rewind-count"',
        b'id="session-pause-count"',
        b'id="session-speed-change-count"',
        b'id="session-completed"',
        b'id="session-current-speed"',
        b'id="session-adaptation-enabled"',
        b'id="progress-indicator"',
        b'id="play-pause-button"',
        b'id="previous-button"',
        b'id="next-button"',
        b'id="reset-button"',
        b'id="back-button"',
    ]:
        assert marker in response.data


def test_static_css_route_returns_ok(client):
    response = client.get("/static/css/app.css")

    assert response.status_code == 200


def test_static_js_route_returns_ok(client):
    response = client.get("/static/js/app.js")

    assert response.status_code == 200
