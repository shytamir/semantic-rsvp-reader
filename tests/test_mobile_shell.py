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
        b'id="structure-anchor"',
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
    assert "--reader-chunk-font-size: clamp(2.1rem, 10.5vw, 4.2rem)" in css
    assert "font-size: var(--reader-chunk-font-size)" in css
    assert "white-space: nowrap" in css
    assert "overflow: hidden" in css
    assert "text-overflow: ellipsis" in css
    assert "4.4vw" not in css
    assert "pointer-events: none" in css
    assert ".previous-chunk.is-empty" in css


def test_active_chunk_sizing_is_explicit_and_independent_from_ghost(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert ".chunk-display" in css
    assert "--reader-chunk-font-size: clamp(2.1rem, 10.5vw, 4.2rem)" in css
    assert "font-size: var(--reader-chunk-font-size)" in css
    assert ".chunk-display.is-long-chunk" in css
    assert ".chunk-display.is-extra-long-token" in css
    assert ".previous-chunk.is-long-chunk" not in css
    assert ".previous-chunk.is-extra-long-token" not in css


def test_reader_area_reserves_previous_chunk_lane_in_short_landscape_heights(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert "--previous-chunk-top" in css
    assert "--previous-chunk-lane-height" in css
    assert "--previous-active-gap" in css
    assert "var(--previous-chunk-top) +" in css
    assert "var(--previous-chunk-lane-height) +" in css
    assert "var(--previous-active-gap)" in css
    assert "@media (max-height: 680px)" in css
    assert "--previous-chunk-top: 3px" in css
    assert "--previous-active-gap: 8px" in css
    assert "padding-top: clamp(20px, 6vh, 42px)" not in css


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


def test_progress_anchor_has_finger_aimable_hit_area_and_subordinate_visual(client):
    css = client.get("/static/css/app.css").data.decode("utf-8")

    progress_anchor = css.split(".progress-anchor {", 1)[1].split("}", 1)[0]
    progress_fill = css.split(".progress-anchor-fill {", 1)[1].split("}", 1)[0]
    reader_footer = css.split(".reader-footer {", 1)[1].split("}", 1)[0]

    assert "height: 44px" in progress_anchor
    assert "background: transparent" in progress_anchor
    assert "pointer-events: auto" in progress_anchor
    assert "height: 2px" in progress_fill
    assert "opacity: 0.35" in progress_fill
    assert "padding-bottom: max(44px, env(safe-area-inset-bottom))" in reader_footer


def test_structure_anchor_is_static_and_inert(client):
    response = client.get("/static/css/app.css")
    css = response.data.decode("utf-8")

    assert ".structure-anchor" in css
    assert "position: fixed" in css
    assert "pointer-events: none" in css
    assert "transition" not in css
    assert "animation" not in css


def test_visible_structure_anchor_reserves_ghost_chunk_lane(client):
    css = client.get("/static/css/app.css").data.decode("utf-8")

    assert ".reader-mode:has(.structure-anchor:not(.is-hidden)) .reader-area" in css
    assert "--previous-chunk-top: max(30px, calc(env(safe-area-inset-top) + 24px))" in css


def test_static_js_route_returns_ok(client):
    response = client.get("/static/js/app.js")

    assert response.status_code == 200


def test_prepare_screen_groups_validation_sample_collections(client):
    javascript = client.get("/static/js/app.js").data.decode("utf-8")
    css = client.get("/static/css/app.css").data.decode("utf-8")

    assert "sample.collection_label" in javascript
    assert 'group.className = "sample-collection"' in javascript
    assert 'controls.className = "sample-collection-controls"' in javascript
    assert ".sample-collection-title" in css
    assert ".sample-collection-controls" in css
    assert "loadValidationSample(sample)" in javascript


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
    assert "updateStructureAnchor" in javascript
    assert "getCurrentStructureMeta" in javascript
    assert "getCurrentStructureLabel" in javascript
    assert "resetStructureAnchor" in javascript
    assert "renderPreviousChunk" in javascript
    assert "getPreviousDisplayedChunkMetadata" in javascript
    assert "previousChunkDisplay" in javascript
    assert "chunkDisplay.classList.toggle(\"is-long-chunk\"" in javascript
    assert "previousChunkDisplay.classList.remove(\"is-long-chunk\", \"is-extra-long-token\")" in javascript
    assert "setBreakpointAtCurrentChunk" in javascript
    assert "computeLeadInIndex" in javascript


def test_static_js_collects_layout_context_for_defects(client):
    response = client.get("/static/js/app.js")
    javascript = response.data.decode("utf-8")

    assert "layout_context" in javascript
    assert "previous_chunk_visible" in javascript
    assert "previous_chunk_text_length" in javascript
    assert "active_chunk_text_length" in javascript


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
