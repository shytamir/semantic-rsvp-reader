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
        b'id="validation-samples-title"',
        b'id="validation-sample-list"',
        b'id="sample-status"',
        b'id="status-message"',
        b'id="reader-area"',
        b'id="previous-chunk"',
        b'id="chunk-display"',
        b'id="progress-anchor"',
        b'id="progress-anchor-fill"',
        b'id="breakpoint-status"',
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
        b'id="previous-five-button"',
        b'id="previous-button"',
        b'id="next-button"',
        b'id="next-five-button"',
        b'id="report-defect-button"',
        b'id="defect-panel"',
        b'id="defect-category"',
        b'id="defect-severity"',
        b'id="defect-notes"',
        b'id="defect-preferred-behavior"',
        b'id="defect-context-preview"',
        b'id="defect-submit"',
        b'id="defect-cancel"',
        b'id="defect-status"',
        b'id="defect-count"',
        b'id="reset-button"',
        b'id="back-button"',
    ]:
        assert marker in response.data


def test_static_css_route_returns_ok(client):
    response = client.get("/static/css/app.css")

    assert response.status_code == 200


def test_chunk_display_disables_browser_word_splitting(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert ".chunk-display" in css
    assert "hyphens: none" in css
    assert "overflow-wrap: normal" in css
    assert "word-break: normal" in css
    assert "overflow-x: hidden" in css


def test_chunk_display_has_quote_and_parenthetical_state_styles(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert ".chunk-display.state-quote" in css
    assert ".chunk-display.state-parenthetical" in css
    assert "border-left" in css


def test_previous_chunk_display_is_ghosted_and_noninteractive(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert ".previous-chunk" in css
    assert "position: absolute" in css
    assert "opacity: 0.45" in css
    assert "pointer-events: none" in css
    assert ".previous-chunk.is-empty" in css


def test_navigation_scaffold_is_hidden_and_inert(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert ".navigation-scaffold[hidden]" in css
    assert "position: fixed" in css
    assert "height: 2px" in css
    assert "opacity: 0.35" in css
    assert "pointer-events: none" in css
    assert "pointer-events: auto" in css
    assert ".progress-anchor-fill" in css


def test_static_js_route_returns_ok(client):
    response = client.get("/static/js/app.js")

    assert response.status_code == 200


def test_static_js_collects_chunk_display_metadata(client):
    response = client.get("/static/js/app.js")
    javascript = response.data.decode("utf-8")

    assert "getChunkDisplayMetadata" in javascript
    assert "chunk_scroll_width_px" in javascript
    assert "chunk_client_width_px" in javascript
    assert "chunk_may_overflow" in javascript


def test_static_js_applies_quote_and_parenthetical_state(client):
    response = client.get("/static/js/app.js")
    javascript = response.data.decode("utf-8")

    assert "renderChunkDisplayState" in javascript
    assert "state-quote" in javascript
    assert "state-parenthetical" in javascript
    assert "parenthetical_depth" in javascript


def test_static_js_includes_dormant_navigation_helpers(client):
    response = client.get("/static/js/app.js")
    javascript = response.data.decode("utf-8")

    assert "navigationEnabled = false" in javascript
    assert "getCurrentNavigationMeta" in javascript
    assert "getNearestProgressMilestoneIndex" in javascript
    assert "toggleBreakpoint" in javascript
    assert "getPreviousBreakpointIndex" in javascript
    assert "getNextBreakpointIndex" in javascript
    assert "jumpToBreakpoint" in javascript
    assert "startDriftRecoveryToBreakpoint" in javascript
    assert "completeDriftRecovery" in javascript
    assert "cancelPendingDriftRecovery" in javascript
    assert "getDriftRecoveryMetadata" in javascript
    assert "renderPreviousChunk" in javascript
    assert "getPreviousDisplayedChunkMetadata" in javascript
    assert "setBreakpointAtCurrentChunk" in javascript
    assert "computeLeadInIndex" in javascript


def test_static_js_includes_breakpoint_traversal_feedback(client):
    response = client.get("/static/js/app.js")
    javascript = response.data.decode("utf-8")

    assert "breakpoint_added" in javascript
    assert "breakpoint_removed" in javascript
    assert "breakpoint_jump" in javascript
    assert "drift_recovery_started" in javascript
    assert "drift_recovery_resumed" in javascript
    assert "drift_recovery_cancelled" in javascript
    assert "reader-flash" in javascript
    assert "traverseBreakpointOrStep" in javascript


def test_static_js_updates_and_seeks_progress_anchor(client):
    response = client.get("/static/js/app.js")
    javascript = response.data.decode("utf-8")

    assert "handleProgressAnchorClick" in javascript
    assert "shouldUpdateProgressAnchor" in javascript
    assert "updateProgressAnchor" in javascript
    assert "progress_seek" in javascript
    assert "is_progress_milestone" in javascript
