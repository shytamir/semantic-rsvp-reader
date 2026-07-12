const SWIPE_MIN_DISTANCE_PX = 40;
const SWIPE_MAX_VERTICAL_DRIFT_PX = 60;
const LONG_PRESS_MS = 500;
const DOUBLE_TAP_MS = 280;
const DRIFT_RECOVERY_DELAY_MS = 500;
const DRIFT_RECOVERY_LEAD_IN_CHUNKS = 3;
const TAP_MAX_DISTANCE_PX = 12;
const JUMP_CHUNK_COUNT = 5;
const SPEED_LEVELS = [0.75, 0.85, 1.0, 1.15, 1.3, 1.5];
const DEFAULT_SPEED_INDEX = 2;
const MIN_EFFECTIVE_DURATION_MS = 100;
const ADAPTATION_MIN_EVENTS = 3;
const ADAPTATION_REWIND_THRESHOLD = 2;
const ADAPTATION_PAUSE_THRESHOLD = 3;
const ADAPTATION_SMOOTH_CHUNK_THRESHOLD = 12;

const inputMode = document.querySelector("#input-mode");
const readerMode = document.querySelector("#reader-mode");
const form = document.querySelector("#schedule-form");
const input = document.querySelector("#text-input");
const prepareButton = document.querySelector("#prepare-button");
const statusMessage = document.querySelector("#status-message");
const sampleList = document.querySelector("#validation-sample-list");
const sampleStatus = document.querySelector("#sample-status");
const readerArea = document.querySelector("#reader-area");
const chunkDisplay = document.querySelector("#chunk-display");
const progressIndicator = document.querySelector("#progress-indicator");
const playPauseButton = document.querySelector("#play-pause-button");
const previousButton = document.querySelector("#previous-button");
const previousFiveButton = document.querySelector("#previous-five-button");
const nextButton = document.querySelector("#next-button");
const nextFiveButton = document.querySelector("#next-five-button");
const reportDefectButton = document.querySelector("#report-defect-button");
const resetButton = document.querySelector("#reset-button");
const backButton = document.querySelector("#back-button");
const defectPanel = document.querySelector("#defect-panel");
const defectCategory = document.querySelector("#defect-category");
const defectSeverity = document.querySelector("#defect-severity");
const defectNotes = document.querySelector("#defect-notes");
const defectPreferredBehavior = document.querySelector("#defect-preferred-behavior");
const defectContextPreview = document.querySelector("#defect-context-preview");
const defectSubmit = document.querySelector("#defect-submit");
const defectCancel = document.querySelector("#defect-cancel");
const defectStatus = document.querySelector("#defect-status");
const defectCount = document.querySelector("#defect-count");
const speedOverlay = document.querySelector("#speed-overlay");
const speedLabel = document.querySelector("#speed-label");
const speedSlower = document.querySelector("#speed-slower");
const speedFaster = document.querySelector("#speed-faster");
const speedReset = document.querySelector("#speed-reset");
const speedClose = document.querySelector("#speed-close");
const sessionEventCount = document.querySelector("#session-event-count");
const sessionRewindCount = document.querySelector("#session-rewind-count");
const sessionPauseCount = document.querySelector("#session-pause-count");
const sessionSpeedChangeCount = document.querySelector("#session-speed-change-count");
const sessionCompleted = document.querySelector("#session-completed");
const adaptationToggle = document.querySelector("#adaptation-toggle");
const adaptationStatus = document.querySelector("#adaptation-status");
const adaptationReset = document.querySelector("#adaptation-reset");
const adaptationCount = document.querySelector("#adaptation-count");
const sessionCurrentSpeed = document.querySelector("#session-current-speed");
const sessionAdaptationEnabled = document.querySelector("#session-adaptation-enabled");
const navigationScaffold = document.querySelector("#navigation-scaffold");
const structureAnchor = document.querySelector("#structure-anchor");
const progressAnchor = document.querySelector("#progress-anchor");
const progressAnchorFill = document.querySelector("#progress-anchor-fill");
const breakpointStatus = document.querySelector("#breakpoint-status");
const previousChunkDisplay = document.querySelector("#previous-chunk");
const removeContinuityButton = document.querySelector("#remove-continuity-button");
const clearContinuityButton = document.querySelector("#clear-continuity-button");
const continuityStatus = document.querySelector("#continuity-status");
const continuityApi = window.SemanticRSVPContinuity;
let continuityStore = null;
try {
  continuityStore = continuityApi
    ? continuityApi.createStore(window.localStorage)
    : null;
} catch (_error) {
  continuityStore = null;
}

let schedule = [];
let currentIndex = 0;
let navigationEnabled = false;
let breakpoints = [];
let lastProgressMilestoneIndex = 0;
let displayedProgressPercent = 0;
let isPlaying = false;
let timerId = null;
let driftRecoveryTimerId = null;
let driftRecoveryState = null;
let touchStartX = 0;
let touchStartY = 0;
let touchStartTime = 0;
let longPressTimerId = null;
let pendingSingleTapTimerId = null;
let lastTapAt = 0;
let suppressNextTap = false;
let gestureStarted = false;
let longPressActivated = false;
let speedIndex = DEFAULT_SPEED_INDEX;
let playbackSpeed = SPEED_LEVELS[speedIndex];
let sessionEvents = [];
let scheduledSentences = [];
let sessionStartedAt = null;
let completionRecorded = false;
let adaptationEnabled = true;
let lastAdaptationEventIndex = 0;
let smoothChunkRun = 0;
let adaptationSuppressedUntilEventCount = 0;
let lastAdaptationReason = null;
let lastAdaptationDirection = null;
let isLoading = false;
let defectReportCount = 0;
let lastDefectReportId = null;
let isSubmittingDefect = false;
let currentDocumentId = null;
let currentDocumentSourceType = null;
let currentDocumentDisplayName = null;

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  await loadSchedule(input.value);
});
document.addEventListener("visibilitychange", handleVisibilityChange);

playPauseButton.addEventListener("click", togglePlayback);
previousButton.addEventListener("click", previousChunk);
previousFiveButton.addEventListener("click", previousFiveChunks);
nextButton.addEventListener("click", () => nextChunk());
nextFiveButton.addEventListener("click", nextFiveChunks);
reportDefectButton.addEventListener("click", openDefectPanel);
resetButton.addEventListener("click", resetReader);
backButton.addEventListener("click", enterInputMode);
defectSubmit.addEventListener("click", submitDefectReport);
defectCancel.addEventListener("click", closeDefectPanel);
speedSlower.addEventListener("click", decreaseSpeed);
speedFaster.addEventListener("click", increaseSpeed);
speedReset.addEventListener("click", resetSpeed);
speedClose.addEventListener("click", hideSpeedOverlay);
adaptationToggle.addEventListener("click", () => setAdaptationEnabled(!adaptationEnabled));
adaptationReset.addEventListener("click", resetAdaptationWindowFromControl);
removeContinuityButton.addEventListener("click", removeCurrentDocumentContinuity);
clearContinuityButton.addEventListener("click", clearAllContinuity);
speedOverlay.addEventListener("pointerdown", stopOverlayGesturePropagation);
speedOverlay.addEventListener("pointermove", stopOverlayGesturePropagation);
speedOverlay.addEventListener("pointerup", stopOverlayGesturePropagation);
speedOverlay.addEventListener("click", stopOverlayGesturePropagation);
defectPanel.addEventListener("pointerdown", stopOverlayGesturePropagation);
defectPanel.addEventListener("pointermove", stopOverlayGesturePropagation);
defectPanel.addEventListener("pointerup", stopOverlayGesturePropagation);
defectPanel.addEventListener("click", stopOverlayGesturePropagation);
progressAnchor.addEventListener("pointerdown", stopOverlayGesturePropagation);
progressAnchor.addEventListener("click", handleProgressAnchorClick);
attachReaderGestures();
restoreReaderPreferences();
renderSpeedControls();
renderSessionDebug();
renderAdaptationStatus();
renderDefectCount();
loadValidationSamples();
renderInitialContinuityStatus();

async function loadSchedule(text) {
  if (isLoading) {
    return;
  }

  cancelPendingDriftRecovery("load_schedule");
  clearPendingSingleTapTimer();
  pause({ record: false, render: false });
  hideSpeedOverlay();
  setLoading(true);
  showStatus("Preparing...");

  try {
    const documentId = continuityApi
      ? await continuityApi.computeDocumentId(text).catch(() => null)
      : null;
    const response = await fetch("/api/schedule", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const payload = await response.json();

    validateScheduleResponse(payload, response);

    schedule = payload.schedule;
    scheduledSentences = Array.isArray(payload.sentences) ? payload.sentences : [];
    currentIndex = 0;
    resetNavigationScaffold();
    resetStructureAnchor();
    defectReportCount = 0;
    lastDefectReportId = null;
    resetSpeed({ record: false });
    resetSessionEvents();
    resetAdaptationState();
    restoreReaderPreferences();
    currentDocumentId = documentId;
    currentDocumentSourceType = "inline_text";
    currentDocumentDisplayName = "Pasted text";
    restoreCurrentDocumentContinuity();
    renderDefectCount();
    recordSessionEvent("schedule_loaded", {
      chunk_count: schedule.length,
      sentence_count: payload.sentence_count,
    });
    enterReaderMode();
  } catch (error) {
    schedule = [];
    scheduledSentences = [];
    currentDocumentId = null;
    currentDocumentSourceType = null;
    currentDocumentDisplayName = null;
    currentIndex = 0;
    resetNavigationScaffold();
    resetStructureAnchor();
    stopPlayback({ render: false });
    hideSpeedOverlay();
    closeDefectPanel();
    readerMode.classList.add("is-hidden");
    inputMode.classList.remove("is-hidden");
    showError(error.message);
  } finally {
    setLoading(false);
  }
}

function restoreReaderPreferences() {
  if (!continuityStore) {
    return;
  }
  const preferences = continuityStore.loadPreferences();
  if (!preferences) {
    return;
  }
  speedIndex = Math.min(
    Math.max(preferences.speed_index, 0),
    SPEED_LEVELS.length - 1,
  );
  playbackSpeed = SPEED_LEVELS[speedIndex];
  adaptationEnabled = preferences.adaptation_enabled;
  renderSpeedControls();
  renderAdaptationStatus();
}

function persistReaderPreferences() {
  if (!continuityStore) {
    return false;
  }
  return continuityStore.savePreferences({
    speed_index: speedIndex,
    adaptation_enabled: adaptationEnabled,
  });
}

function restoreCurrentDocumentContinuity() {
  pause({ record: false, render: false });
  if (!continuityStore || !currentDocumentId || schedule.length === 0) {
    setContinuityStatus("Local continuity is unavailable for this document.");
    return false;
  }
  const record = continuityStore.getDocument(currentDocumentId);
  if (!record) {
    currentIndex = 0;
    breakpoints = [];
    setContinuityStatus("New local document reference.");
    return false;
  }
  const restored = continuityApi.resolveDocumentState(record, schedule.length);
  currentIndex = restored.position;
  breakpoints = restored.breakpoints;
  setContinuityStatus(`Restored paused at chunk ${currentIndex + 1}.`);
  return true;
}

function persistCurrentDocumentContinuity() {
  if (!continuityStore || !currentDocumentId || schedule.length === 0) {
    return false;
  }
  return continuityStore.saveDocument({
    document_id: currentDocumentId,
    source_type: currentDocumentSourceType || "inline_text",
    display_name: currentDocumentDisplayName || "Document",
    position: clampIndex(currentIndex),
    breakpoints: normalizeBreakpoints(),
    updated_at: Date.now(),
  });
}

function removeCurrentDocumentContinuity() {
  pause({ record: false });
  if (!continuityStore || !currentDocumentId) {
    setContinuityStatus("No current saved document to remove.");
    return;
  }
  continuityStore.removeDocument(currentDocumentId);
  currentDocumentId = null;
  currentDocumentSourceType = null;
  currentDocumentDisplayName = null;
  breakpoints = [];
  setBreakpointStatus("");
  setContinuityStatus("Removed saved position and breakpoints for this document.");
}

function clearAllContinuity() {
  pause({ record: false });
  if (continuityStore) {
    continuityStore.clearAll();
  }
  currentDocumentId = null;
  currentDocumentSourceType = null;
  currentDocumentDisplayName = null;
  breakpoints = [];
  speedIndex = DEFAULT_SPEED_INDEX;
  playbackSpeed = SPEED_LEVELS[speedIndex];
  adaptationEnabled = true;
  renderSpeedControls();
  renderAdaptationStatus();
  setBreakpointStatus("");
  setContinuityStatus("Cleared local document references and reader preferences.");
}

function renderInitialContinuityStatus() {
  if (!continuityStore) {
    setContinuityStatus("Local continuity is unavailable.");
    return;
  }
  const count = continuityStore.loadDocuments().length;
  if (count === 0) {
    setContinuityStatus("No saved local document references.");
    return;
  }
  setContinuityStatus(
    `${count} saved document reference${count === 1 ? "" : "s"}; prepare matching text to restore.`,
  );
}

function setContinuityStatus(message) {
  if (continuityStatus) {
    continuityStatus.textContent = message;
  }
}

async function loadValidationSamples() {
  if (!sampleList || !sampleStatus) {
    return;
  }

  try {
    const response = await fetch("/api/validation-samples");
    const payload = await response.json();
    if (!response.ok || !payload || !Array.isArray(payload.samples)) {
      throw new Error("Validation samples were unavailable.");
    }
    renderValidationSamples(payload.samples);
  } catch (error) {
    sampleStatus.textContent = error.message;
  }
}

function renderValidationSamples(samples) {
  sampleList.replaceChildren();

  if (samples.length === 0) {
    sampleStatus.textContent = "No samples found.";
    return;
  }

  const collections = new Map();
  for (const sample of samples) {
    const key = sample.collection || "validation_samples";
    if (!collections.has(key)) {
      collections.set(key, {
        label: sample.collection_label || "Validation samples",
        samples: [],
      });
    }
    collections.get(key).samples.push(sample);
  }

  for (const collection of collections.values()) {
    const group = document.createElement("section");
    group.className = "sample-collection";
    const heading = document.createElement("h3");
    heading.className = "sample-collection-title";
    heading.textContent = collection.label;
    group.appendChild(heading);
    const controls = document.createElement("div");
    controls.className = "sample-collection-controls";
    for (const sample of collection.samples) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "sample-button";
      button.textContent = `${sample.id} ${sample.category}`;
      button.setAttribute("aria-label", `Load validation sample ${sample.id}`);
      button.addEventListener("click", () => loadValidationSample(sample));
      controls.appendChild(button);
    }
    group.appendChild(controls);
    sampleList.appendChild(group);
  }

  sampleStatus.textContent = `${samples.length} samples ready.`;
}

function loadValidationSample(sample) {
  input.value = sample.text;
  input.focus();
  showStatus(`Loaded validation sample ${sample.id}.`);
}

function renderCurrentChunk() {
  if (schedule.length === 0) {
    chunkDisplay.textContent = "No text loaded";
    renderPreviousChunk();
    updateStructureAnchor();
    setChunkDisplaySizing("No text loaded");
    renderChunkDisplayState(null);
    progressIndicator.textContent = "0 / 0";
    playPauseButton.textContent = "Play";
    return;
  }

  currentIndex = clampIndex(currentIndex);
  const item = schedule[currentIndex];
  chunkDisplay.textContent = item.text;
  renderPreviousChunk();
  updateStructureAnchor();
  setChunkDisplaySizing(item.text);
  renderChunkDisplayState(item);
  progressIndicator.textContent = `${currentIndex + 1} / ${schedule.length}`;
  playPauseButton.textContent = isPlaying ? "Pause" : "Play";
  updateProgressAnchor();
  persistCurrentDocumentContinuity();
}

function renderPreviousChunk() {
  if (!previousChunkDisplay) {
    return;
  }
  const previousItem = getPreviousDisplayedScheduleItem();
  previousChunkDisplay.textContent = previousItem ? previousItem.text : "";
  previousChunkDisplay.classList.toggle("is-empty", !previousItem);
  previousChunkDisplay.classList.remove("is-long-chunk", "is-extra-long-token");
}

function openDefectPanel() {
  if (!isReaderModeActive() || schedule.length === 0) {
    return;
  }

  cancelPendingDriftRecovery("defect_report");
  pause();
  hideSpeedOverlay();
  defectNotes.value = "";
  defectPreferredBehavior.value = "";
  defectSeverity.value = "2";
  setDefectStatus("");
  renderDefectContextPreview(buildDefectPayload());
  defectPanel.classList.remove("is-hidden");
  defectNotes.focus();
}

function closeDefectPanel() {
  if (!defectPanel) {
    return;
  }
  defectPanel.classList.add("is-hidden");
  setDefectStatus("");
}

function buildDefectPayload() {
  const item = getCurrentScheduleItem();
  const context = getChunkContext();
  const timing = getTimingContext(item);
  return {
    category: defectCategory.value,
    severity: Number(defectSeverity.value),
    notes: defectNotes.value,
    preferred_behavior: defectPreferredBehavior.value,
    reader_state: {
      current_index: currentIndex,
      sentence_index: item ? item.sentence_index : null,
      current_chunk: item ? item.text : "",
      current_duration_ms: item ? item.duration_ms : null,
      base_duration_ms: timing.base_duration_ms,
      effective_duration_ms: timing.effective_duration_ms,
      duration_source: timing.duration_source,
      current_syntactic_hint: item ? item.syntactic_hint : "",
      current_content_word_count: item ? item.content_word_count : null,
      char_length: item ? item.char_length : null,
      in_quote: item ? Boolean(item.in_quote) : false,
      quote_boundary: item ? item.quote_boundary || "none" : "none",
      in_parenthetical: item ? Boolean(item.in_parenthetical) : false,
      parenthetical_depth: item ? Number(item.parenthetical_depth || 0) : 0,
      navigation: item && item.navigation ? item.navigation : null,
      structure: item && item.structure ? item.structure : null,
      previous_displayed_chunk: getPreviousDisplayedChunkMetadata(),
      breakpoints: getBreakpointMetadata(),
      drift_recovery: getDriftRecoveryMetadata(),
      original_sentence: getOriginalSentenceForCurrentChunk(),
      previous_chunks: context.previous_chunks,
      next_chunks: context.next_chunks,
      playback_speed: playbackSpeed,
      adaptation_enabled: adaptationEnabled,
      session_summary: getSessionSummary(),
    },
    client: {
      user_agent: navigator.userAgent,
      viewport_width: window.innerWidth,
      viewport_height: window.innerHeight,
      ...getChunkDisplayMetadata(),
    },
  };
}

function setChunkDisplaySizing(text) {
  const words = String(text || "").split(/\s+/).filter(Boolean);
  const longestWordLength = words.reduce(
    (longest, word) => Math.max(longest, word.length),
    0,
  );
  const isLongChunk = String(text || "").length > 32;
  const isExtraLongToken = longestWordLength > 22;
  if (chunkDisplay) {
    chunkDisplay.classList.toggle("is-long-chunk", isLongChunk);
    chunkDisplay.classList.toggle("is-extra-long-token", isExtraLongToken);
  }
}

function renderChunkDisplayState(item) {
  const inQuote = Boolean(item && item.in_quote);
  const quoteBoundary = item && item.quote_boundary ? item.quote_boundary : "none";
  const inParenthetical = Boolean(item && item.in_parenthetical);
  chunkDisplay.classList.toggle("state-quote", inQuote || quoteBoundary !== "none");
  chunkDisplay.classList.toggle("state-parenthetical", inParenthetical);
}

function getChunkDisplayMetadata() {
  const previousChunkVisible = Boolean(
    previousChunkDisplay &&
      !previousChunkDisplay.classList.contains("is-empty") &&
      previousChunkDisplay.textContent,
  );
  return {
    display_width_px: Math.round(readerArea ? readerArea.clientWidth : 0),
    chunk_scroll_width_px: Math.round(chunkDisplay ? chunkDisplay.scrollWidth : 0),
    chunk_client_width_px: Math.round(chunkDisplay ? chunkDisplay.clientWidth : 0),
    chunk_may_overflow: Boolean(
      chunkDisplay && chunkDisplay.scrollWidth > chunkDisplay.clientWidth + 1,
    ),
    layout_context: {
      previous_chunk_visible: previousChunkVisible,
      previous_chunk_text_length: previousChunkDisplay
        ? previousChunkDisplay.textContent.length
        : 0,
      active_chunk_text_length: chunkDisplay ? chunkDisplay.textContent.length : 0,
      viewport_width: window.innerWidth,
      viewport_height: window.innerHeight,
    },
  };
}

function getPreviousDisplayedScheduleItem() {
  if (schedule.length === 0 || currentIndex <= 0) {
    return null;
  }
  return schedule[clampIndex(currentIndex - 1)] || null;
}

function getPreviousDisplayedChunkMetadata() {
  const previousItem = getPreviousDisplayedScheduleItem();
  return previousItem ? formatChunkContextItem(previousItem) : null;
}

function getCurrentStructureMeta() {
  const item = getCurrentScheduleItem();
  return item && item.structure ? item.structure : null;
}

function getCurrentStructureLabel() {
  const structure = getCurrentStructureMeta();
  return structure && typeof structure.active_label === "string"
    ? structure.active_label.trim()
    : "";
}

function updateStructureAnchor() {
  const label = getCurrentStructureLabel();
  if (!label) {
    hideStructureAnchor();
    return;
  }
  showStructureAnchor(label);
}

function showStructureAnchor(label) {
  if (!structureAnchor) {
    return;
  }
  structureAnchor.textContent = label;
  structureAnchor.classList.remove("is-hidden");
}

function hideStructureAnchor() {
  if (!structureAnchor) {
    return;
  }
  structureAnchor.textContent = "";
  structureAnchor.classList.add("is-hidden");
}

function resetStructureAnchor() {
  hideStructureAnchor();
}

function renderDefectContextPreview(payload) {
  const state = payload.reader_state;
  const previous = state.previous_chunks.map((chunk) => `[${chunk.index}] ${chunk.text}`);
  const next = state.next_chunks.map((chunk) => `[${chunk.index}] ${chunk.text}`);
  defectContextPreview.textContent = [
    `Current chunk: ${state.current_chunk || "unknown"}`,
    `Base duration: ${formatDuration(state.base_duration_ms)}`,
    `Effective duration: ${formatDuration(state.effective_duration_ms)}`,
    `Speed: ${state.playback_speed.toFixed(2)}x`,
    `Syntactic hint: ${state.current_syntactic_hint || "unknown"}`,
    `Content words: ${state.current_content_word_count ?? "unknown"}`,
    `Quote state: ${state.in_quote ? "in quote" : "not in quote"} (${state.quote_boundary || "none"})`,
    `Parenthetical: ${state.in_parenthetical ? "inside" : "outside"} (depth ${state.parenthetical_depth ?? 0})`,
    `Structure: ${state.structure && state.structure.active_label ? state.structure.active_label : "none"}`,
    `Previous displayed chunk: ${state.previous_displayed_chunk ? `[${state.previous_displayed_chunk.index}] ${state.previous_displayed_chunk.text}` : "none"}`,
    `Breakpoints: ${state.breakpoints ? state.breakpoints.count : 0}`,
    `Drift recovery: ${state.drift_recovery && state.drift_recovery.pending ? "pending" : "not pending"}`,
    `Original sentence: ${state.original_sentence || "unknown"}`,
    `Previous: ${previous.length ? previous.join(" | ") : "none"}`,
    `Next: ${next.length ? next.join(" | ") : "none"}`,
    `Adaptation: ${state.adaptation_enabled ? "on" : "off"}`,
  ].join("\n");
}

async function submitDefectReport() {
  if (isSubmittingDefect) {
    return;
  }

  cancelPendingDriftRecovery("defect_submit");
  const payload = buildDefectPayload();
  renderDefectContextPreview(payload);
  setDefectStatus("Saving...");
  isSubmittingDefect = true;
  defectSubmit.disabled = true;

  try {
    const response = await fetch("/api/defects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const responsePayload = await response.json();
    if (!response.ok) {
      throw new Error(responsePayload && responsePayload.error ? responsePayload.error : "Unable to save defect report.");
    }

    defectReportCount += 1;
    lastDefectReportId = responsePayload.report_id;
    renderDefectCount();
    recordSessionEvent("defect_reported", {
      report_id: responsePayload.report_id,
      category: payload.category,
      severity: payload.severity,
      chunk_index: payload.reader_state.current_index,
      sentence_index: payload.reader_state.sentence_index,
    });
    setDefectStatus(`Saved ${responsePayload.report_id}.`);
  } catch (error) {
    setDefectStatus(error.message, true);
  } finally {
    isSubmittingDefect = false;
    defectSubmit.disabled = false;
  }
}

function getOriginalSentenceForCurrentChunk() {
  const item = getCurrentScheduleItem();
  if (!item || !Array.isArray(scheduledSentences)) {
    return "";
  }
  return scheduledSentences[item.sentence_index] || "";
}

function getChunkContext(radius = 3) {
  if (schedule.length === 0) {
    return { previous_chunks: [], next_chunks: [] };
  }

  const start = Math.max(0, currentIndex - radius);
  const end = Math.min(schedule.length - 1, currentIndex + radius);
  const previous_chunks = schedule
    .slice(start, currentIndex)
    .map(formatChunkContextItem);
  const next_chunks = schedule
    .slice(currentIndex + 1, end + 1)
    .map(formatChunkContextItem);
  return { previous_chunks, next_chunks };
}

function formatChunkContextItem(item) {
  const timing = getTimingContext(item);
  return {
    index: item.index,
    sentence_index: item.sentence_index,
    text: item.text,
    duration_ms: item.duration_ms,
    base_duration_ms: timing.base_duration_ms,
    effective_duration_ms: timing.effective_duration_ms,
    duration_source: timing.duration_source,
    syntactic_hint: item.syntactic_hint,
    content_word_count: item.content_word_count,
    char_length: item.char_length,
    in_quote: Boolean(item.in_quote),
    quote_boundary: item.quote_boundary || "none",
    in_parenthetical: Boolean(item.in_parenthetical),
    parenthetical_depth: Number(item.parenthetical_depth || 0),
    navigation: item.navigation || null,
  };
}

function getTimingContext(item) {
  if (!item) {
    return {
      base_duration_ms: null,
      effective_duration_ms: null,
      duration_source: "unknown",
    };
  }
  return {
    base_duration_ms: item.duration_ms,
    effective_duration_ms: getEffectiveDurationMs(item),
    duration_source: "schedule",
  };
}

function formatDuration(durationMs) {
  return typeof durationMs === "number" ? `${durationMs}ms` : "unknown";
}

function setDefectStatus(message, isError = false) {
  defectStatus.textContent = message;
  defectStatus.classList.toggle("is-error", isError);
}

function renderDefectCount() {
  defectCount.textContent = defectReportCount;
}

function play() {
  if (schedule.length === 0 || isPlaying) {
    return;
  }

  isPlaying = true;
  recordSessionEvent("play");
  renderCurrentChunk();
  scheduleNextChunk();
}

function pause({ record = true, render = true } = {}) {
  const wasPlaying = isPlaying;
  stopPlayback({ render: false });
  if (record && wasPlaying) {
    recordSessionEvent("pause");
    smoothChunkRun = 0;
    maybeAdaptPlaybackSpeed("pause");
  }
  if (render) {
    renderCurrentChunk();
  }
}

function togglePlayback() {
  if (!isReaderModeActive()) {
    return;
  }

  cancelPendingDriftRecovery("play_pause");
  if (isPlaying) {
    pause();
  } else {
    play();
  }
}

function nextChunk({ auto = false } = {}) {
  if (!auto) {
    cancelPendingDriftRecovery("manual_next");
  }
  clearPlaybackTimer();

  if (schedule.length === 0) {
    pause({ record: !auto });
    return;
  }

  const oldIndex = currentIndex;
  if (currentIndex >= schedule.length - 1) {
    currentIndex = schedule.length - 1;
    if (!auto) {
      recordSessionEvent("next_chunk", {
        from_index: oldIndex,
        to_index: currentIndex,
      });
    }
    pause({ record: !auto });
    renderCompletion();
    if (auto) {
      recordCompletion();
    }
    return;
  }

  currentIndex += 1;
  if (!auto) {
    recordSessionEvent("next_chunk", {
      from_index: oldIndex,
      to_index: currentIndex,
    });
    smoothChunkRun = 0;
  }

  if (auto && isPlaying) {
    smoothChunkRun += 1;
    maybeAdaptPlaybackSpeed("auto_advance");
    renderCurrentChunk();
    scheduleNextChunk();
  } else {
    pause();
    if (!auto) {
      updateProgressAnchor({ force: true });
    }
  }
}

function previousChunk() {
  moveManualChunks(-1, "previous_chunk");
}

function previousFiveChunks() {
  moveManualChunks(-JUMP_CHUNK_COUNT, "previous_chunk");
}

function nextFiveChunks() {
  moveManualChunks(JUMP_CHUNK_COUNT, "next_chunk");
}

function moveManualChunks(delta, eventType) {
  cancelPendingDriftRecovery(eventType);
  if (schedule.length === 0) {
    pause();
    return;
  }

  const oldIndex = currentIndex;
  currentIndex = clampIndex(currentIndex + delta);
  recordSessionEvent(eventType, {
    from_index: oldIndex,
    to_index: currentIndex,
    step: Math.abs(delta),
  });
  smoothChunkRun = 0;
  if (eventType === "previous_chunk") {
    maybeAdaptPlaybackSpeed("rewind");
  }
  pause();
  updateProgressAnchor({ force: true });
}

function resetReader() {
  cancelPendingDriftRecovery("reset");
  const oldIndex = currentIndex;
  currentIndex = 0;
  recordSessionEvent("reset", {
    from_index: oldIndex,
    to_index: currentIndex,
  });
  resetAdaptationWindow();
  pause();
  updateProgressAnchor({ force: true, percent: 0 });
  setContinuityStatus("Reset saved position to chunk 1.");
}

function enterInputMode() {
  cancelPendingDriftRecovery("back_to_input");
  recordSessionEvent("back_to_input");
  clearPendingSingleTapTimer();
  pause();
  hideSpeedOverlay();
  closeDefectPanel();
  resetStructureAnchor();
  hideProgressAnchor();
  resetProgressAnchor();
  readerMode.classList.add("is-hidden");
  inputMode.classList.remove("is-hidden");
  showStatus("Prepare text to start reading.");
}

function enterReaderMode() {
  inputMode.classList.add("is-hidden");
  readerMode.classList.remove("is-hidden");
  isPlaying = false;
  clearPlaybackTimer();
  hideSpeedOverlay();
  closeDefectPanel();
  showProgressAnchor();
  renderCurrentChunk();
  updateProgressAnchor({ force: true });
  renderSessionDebug();
  renderDefectCount();
  readerArea.focus();
}

function showError(message) {
  statusMessage.classList.add("is-error");
  statusMessage.textContent = message;
}

function showStatus(message) {
  statusMessage.classList.remove("is-error");
  statusMessage.textContent = message;
}

function scheduleNextChunk() {
  clearPlaybackTimer();

  if (!isPlaying || schedule.length === 0) {
    return;
  }

  const duration = Number(schedule[currentIndex].duration_ms);
  timerId = window.setTimeout(
    () => nextChunk({ auto: true }),
    getEffectiveDurationMs({ duration_ms: Number.isFinite(duration) ? duration : 400 }),
  );
}

function clearPlaybackTimer() {
  if (timerId !== null) {
    window.clearTimeout(timerId);
    timerId = null;
  }
}

function stopPlayback({ render = true } = {}) {
  isPlaying = false;
  clearPlaybackTimer();
  if (render) {
    renderCurrentChunk();
  }
}

function renderCompletion() {
  clearPlaybackTimer();
  progressIndicator.textContent = `${schedule.length} / ${schedule.length} complete`;
  playPauseButton.textContent = "Play";
  updateProgressAnchor({ force: true, percent: 100 });
}

function clampIndex(index) {
  if (schedule.length === 0) {
    return 0;
  }
  return Math.min(Math.max(index, 0), schedule.length - 1);
}

function attachReaderGestures() {
  readerArea.addEventListener("pointerdown", handlePointerStart);
  readerArea.addEventListener("pointermove", handlePointerMove);
  readerArea.addEventListener("pointerup", handlePointerEnd);
  readerArea.addEventListener("pointercancel", cancelGesture);
  readerArea.addEventListener("lostpointercapture", clearLongPressTimer);
}

function handlePointerStart(event) {
  if (!isReaderModeActive() || event.target.closest("button")) {
    return;
  }

  preventGestureDefault(event);
  cancelPendingDriftRecovery("reader_gesture");
  clearPendingSingleTapTimer();
  gestureStarted = true;
  suppressNextTap = false;
  longPressActivated = false;
  touchStartX = event.clientX;
  touchStartY = event.clientY;
  touchStartTime = Date.now();
  if (readerArea.setPointerCapture) {
    readerArea.setPointerCapture(event.pointerId);
  }
  clearLongPressTimer();
  longPressTimerId = window.setTimeout(handleLongPress, LONG_PRESS_MS);
}

function handlePointerMove(event) {
  if (!gestureStarted) {
    return;
  }

  preventGestureDefault(event);
  const deltaX = event.clientX - touchStartX;
  const deltaY = event.clientY - touchStartY;
  if (Math.hypot(deltaX, deltaY) > TAP_MAX_DISTANCE_PX) {
    clearLongPressTimer();
  }
}

function handlePointerEnd(event) {
  if (!gestureStarted) {
    return;
  }

  preventGestureDefault(event);
  releasePointerCapture(event);
  const deltaX = event.clientX - touchStartX;
  const deltaY = event.clientY - touchStartY;
  const elapsed = Date.now() - touchStartTime;
  gestureStarted = false;
  clearLongPressTimer();

  if (!isReaderModeActive()) {
    return;
  }

  if (longPressActivated) {
    if (isSwipe(deltaX, deltaY)) {
      if (deltaX < 0) {
        previousFiveChunks();
      } else {
        nextFiveChunks();
      }
    } else {
      toggleSpeedOverlay();
    }
    longPressActivated = false;
    suppressNextTap = false;
    return;
  }

  if (suppressNextTap) {
    suppressNextTap = false;
    return;
  }

  if (isSwipe(deltaX, deltaY)) {
    suppressNextTap = true;
    if (deltaX < 0) {
      traverseBreakpointOrStep("previous");
    } else {
      traverseBreakpointOrStep("next");
    }
    window.setTimeout(() => {
      suppressNextTap = false;
    }, 0);
    return;
  }

  if (Math.hypot(deltaX, deltaY) <= TAP_MAX_DISTANCE_PX && elapsed < LONG_PRESS_MS) {
    handleReaderTap();
  }
}

function cancelGesture(event) {
  releasePointerCapture(event);
  gestureStarted = false;
  suppressNextTap = false;
  longPressActivated = false;
  clearLongPressTimer();
  clearPendingSingleTapTimer();
}

function handleLongPress() {
  if (!gestureStarted || !isReaderModeActive()) {
    return;
  }

  suppressNextTap = true;
  longPressActivated = true;
  clearLongPressTimer();
}

function isSwipe(deltaX, deltaY) {
  return (
    Math.abs(deltaX) >= SWIPE_MIN_DISTANCE_PX &&
    Math.abs(deltaY) <= SWIPE_MAX_VERTICAL_DRIFT_PX &&
    Math.abs(deltaX) > Math.abs(deltaY)
  );
}

function toggleSpeedOverlay() {
  cancelPendingDriftRecovery("speed_overlay");
  renderSpeedControls();
  speedOverlay.classList.toggle("is-hidden");
}

function hideSpeedOverlay() {
  cancelPendingDriftRecovery("speed_overlay");
  speedOverlay.classList.add("is-hidden");
}

function clearLongPressTimer() {
  if (longPressTimerId !== null) {
    window.clearTimeout(longPressTimerId);
    longPressTimerId = null;
  }
}

function clearPendingSingleTapTimer() {
  if (pendingSingleTapTimerId !== null) {
    window.clearTimeout(pendingSingleTapTimerId);
    pendingSingleTapTimerId = null;
  }
}

function handleReaderTap() {
  const now = Date.now();
  if (now - lastTapAt <= DOUBLE_TAP_MS) {
    lastTapAt = 0;
    clearPendingSingleTapTimer();
    toggleBreakpoint();
    return;
  }

  lastTapAt = now;
  clearPendingSingleTapTimer();
  pendingSingleTapTimerId = window.setTimeout(() => {
    pendingSingleTapTimerId = null;
    lastTapAt = 0;
    togglePlayback();
  }, DOUBLE_TAP_MS);
}

function isReaderModeActive() {
  return !readerMode.classList.contains("is-hidden");
}

function getEffectiveDurationMs(scheduleItem) {
  const baseDuration = Number(scheduleItem.duration_ms);
  const duration = Number.isFinite(baseDuration) && baseDuration > 0 ? baseDuration : 400;
  return Math.max(MIN_EFFECTIVE_DURATION_MS, Math.round(duration / playbackSpeed));
}

function renderSpeedControls() {
  updateSpeedLabel();
  speedSlower.disabled = speedIndex <= 0;
  speedFaster.disabled = speedIndex >= SPEED_LEVELS.length - 1;
}

function setSpeedIndex(
  nextIndex,
  { record = true, reschedule = true, suppressAdaptation = true } = {},
) {
  if (record) {
    cancelPendingDriftRecovery("speed_change");
  }
  const oldSpeed = playbackSpeed;
  speedIndex = Math.min(Math.max(nextIndex, 0), SPEED_LEVELS.length - 1);
  playbackSpeed = SPEED_LEVELS[speedIndex];
  renderSpeedControls();
  if (record && playbackSpeed !== oldSpeed) {
    recordSessionEvent("speed_changed", {
      from_speed: oldSpeed,
      to_speed: playbackSpeed,
    });
    smoothChunkRun = 0;
    resetAdaptationWindow();
    if (suppressAdaptation) {
      adaptationSuppressedUntilEventCount = sessionEvents.length + 3;
    }
  }

  if (reschedule && isPlaying) {
    scheduleNextChunk();
  }
  if (record) {
    persistReaderPreferences();
  }
}

function increaseSpeed() {
  setSpeedIndex(speedIndex + 1);
}

function decreaseSpeed() {
  setSpeedIndex(speedIndex - 1);
}

function resetSpeed({ record = true } = {}) {
  setSpeedIndex(DEFAULT_SPEED_INDEX, { record });
}

function updateSpeedLabel() {
  speedLabel.textContent = `${playbackSpeed.toFixed(2)}x`;
}

function stopOverlayGesturePropagation(event) {
  event.stopPropagation();
}

function preventGestureDefault(event) {
  if (event.cancelable) {
    event.preventDefault();
  }
}

function releasePointerCapture(event) {
  if (
    event &&
    readerArea.releasePointerCapture &&
    readerArea.hasPointerCapture &&
    readerArea.hasPointerCapture(event.pointerId)
  ) {
    readerArea.releasePointerCapture(event.pointerId);
  }
}

function setLoading(nextIsLoading) {
  isLoading = nextIsLoading;
  prepareButton.disabled = nextIsLoading;
  prepareButton.textContent = nextIsLoading ? "Preparing..." : "Prepare";
}

function validateScheduleResponse(payload, response) {
  if (!response.ok) {
    throw new Error(payload && payload.error ? payload.error : "Unable to prepare text.");
  }
  if (!payload || !Array.isArray(payload.schedule)) {
    throw new Error("Schedule response was invalid.");
  }
  if (payload.sentences !== undefined && !Array.isArray(payload.sentences)) {
    throw new Error("Schedule sentences were invalid.");
  }
  if (payload.schedule.length === 0) {
    throw new Error("No readable chunks were returned.");
  }
  for (const item of payload.schedule) {
    if (
      typeof item.text !== "string" ||
      typeof item.duration_ms !== "number" ||
      typeof item.index !== "number"
    ) {
      throw new Error("Schedule item was invalid.");
    }
    if (
      item.in_quote !== undefined &&
      typeof item.in_quote !== "boolean"
    ) {
      throw new Error("Schedule item quote state was invalid.");
    }
    if (
      item.in_parenthetical !== undefined &&
      typeof item.in_parenthetical !== "boolean"
    ) {
      throw new Error("Schedule item parenthetical state was invalid.");
    }
    if (
      item.navigation !== undefined &&
      (!item.navigation ||
        typeof item.navigation.progress_percent !== "number" ||
        typeof item.navigation.paragraph_index !== "number")
    ) {
      throw new Error("Schedule item navigation metadata was invalid.");
    }
    if (
      item.structure !== undefined &&
      (!item.structure ||
        !Array.isArray(item.structure.active_path) ||
        typeof item.structure.is_header_chunk !== "boolean")
    ) {
      throw new Error("Schedule item structure metadata was invalid.");
    }
  }
}

function handleVisibilityChange() {
  if (!document.hidden || !isPlaying) {
    return;
  }

  recordSessionEvent("page_hidden_pause");
  pause({ record: false });
}

function getCurrentScheduleItem() {
  if (schedule.length === 0) {
    return null;
  }
  return schedule[clampIndex(currentIndex)] || null;
}

function resetNavigationScaffold() {
  navigationEnabled = false;
  breakpoints = [];
  lastProgressMilestoneIndex = 0;
  resetProgressAnchor();
  hideProgressAnchor();
  clearBreakpoints();
  if (breakpointStatus) {
    breakpointStatus.textContent = "";
  }
}

function resetProgressAnchor() {
  displayedProgressPercent = 0;
  if (progressAnchorFill) {
    progressAnchorFill.style.width = "0%";
  }
}

function showProgressAnchor() {
  if (navigationScaffold) {
    navigationScaffold.hidden = false;
  }
  navigationEnabled = true;
}

function hideProgressAnchor() {
  if (navigationScaffold) {
    navigationScaffold.hidden = true;
  }
  navigationEnabled = false;
}

function shouldUpdateProgressAnchor(item) {
  if (!item || !item.navigation) {
    return false;
  }
  return Boolean(
    item.navigation.is_progress_milestone ||
      item.navigation.is_paragraph_start,
  );
}

function updateProgressAnchor({ force = false, percent = null } = {}) {
  if (!progressAnchorFill || !navigationEnabled) {
    return;
  }
  const item = getCurrentScheduleItem();
  if (!force && !shouldUpdateProgressAnchor(item)) {
    return;
  }
  const nextPercent = percent === null ? getCurrentProgressPercent() : clampPercent(percent);
  displayedProgressPercent = nextPercent;
  if (item && item.navigation && item.navigation.is_progress_milestone) {
    lastProgressMilestoneIndex = item.index;
  }
  progressAnchorFill.style.width = `${displayedProgressPercent}%`;
}

function handleProgressAnchorClick(event) {
  event.stopPropagation();
  if (!isReaderModeActive() || schedule.length === 0 || !progressAnchor) {
    return;
  }
  cancelPendingDriftRecovery("progress_seek");
  const bounds = progressAnchor.getBoundingClientRect();
  if (!bounds.width) {
    return;
  }
  const targetPercent = clampPercent(
    ((event.clientX - bounds.left) / bounds.width) * 100,
  );
  const oldIndex = currentIndex;
  const nextIndex = getNearestProgressMilestoneIndex(targetPercent);
  pause({ record: false, render: false });
  currentIndex = clampIndex(nextIndex);
  smoothChunkRun = 0;
  adaptationSuppressedUntilEventCount = sessionEvents.length + 3;
  resetAdaptationWindow();
  renderCurrentChunk();
  updateProgressAnchor({ force: true });
  const navigation = getCurrentNavigationMeta();
  recordSessionEvent("progress_seek", {
    from_index: oldIndex,
    to_index: currentIndex,
    target_percent: Math.round(targetPercent),
    resolved_percent: navigation ? navigation.progress_percent : 0,
  });
  if (breakpointStatus) {
    breakpointStatus.textContent = `Progress seek ${currentIndex + 1}`;
  }
}

function getCurrentNavigationMeta() {
  const item = getCurrentScheduleItem();
  return item && item.navigation ? item.navigation : null;
}

function getNavigationMetaForIndex(index) {
  if (schedule.length === 0) {
    return null;
  }
  const item = schedule[clampIndex(index)];
  return item && item.navigation ? item.navigation : null;
}

function getCurrentProgressPercent() {
  const navigation = getCurrentNavigationMeta();
  return navigation ? clampPercent(navigation.progress_percent) : 0;
}

function getNearestProgressMilestoneIndex(targetPercent) {
  if (schedule.length === 0) {
    return 0;
  }
  const target = clampPercent(targetPercent);
  let nearestIndex = 0;
  let nearestDistance = Infinity;
  let foundMilestone = false;
  schedule.forEach((item, index) => {
    const navigation = item.navigation || {};
    if (!navigation.is_progress_milestone) {
      return;
    }
    foundMilestone = true;
    const distance = Math.abs(clampPercent(navigation.progress_percent || 0) - target);
    if (distance < nearestDistance) {
      nearestIndex = index;
      nearestDistance = distance;
    }
  });
  if (!foundMilestone) {
    schedule.forEach((item, index) => {
      const navigation = item.navigation || {};
      const distance = Math.abs(clampPercent(navigation.progress_percent || 0) - target);
      if (distance < nearestDistance) {
        nearestIndex = index;
        nearestDistance = distance;
      }
    });
  }
  return nearestIndex;
}

function normalizeBreakpoints() {
  if (schedule.length === 0) {
    breakpoints = [];
    return [];
  }
  breakpoints = [...new Set(breakpoints.map((index) => clampIndex(index)))]
    .sort((left, right) => left - right);
  return [...breakpoints];
}

function hasBreakpoint(index) {
  return normalizeBreakpoints().includes(clampIndex(index));
}

function addBreakpoint(index) {
  breakpoints = [...breakpoints, clampIndex(index)];
  return normalizeBreakpoints();
}

function removeBreakpoint(index) {
  const resolvedIndex = clampIndex(index);
  breakpoints = normalizeBreakpoints().filter(
    (breakpointIndex) => breakpointIndex !== resolvedIndex,
  );
  return [...breakpoints];
}

function toggleBreakpoint(index = currentIndex) {
  if (schedule.length === 0) {
    return [];
  }
  cancelPendingDriftRecovery("breakpoint_toggle");
  const resolvedIndex = clampIndex(index);
  const navigation = getNavigationMetaForIndex(resolvedIndex);
  const metadata = {
    index: resolvedIndex,
    progress_percent: navigation ? navigation.progress_percent : 0,
    paragraph_index: navigation ? navigation.paragraph_index : null,
  };
  if (hasBreakpoint(resolvedIndex)) {
    removeBreakpoint(resolvedIndex);
    recordSessionEvent("breakpoint_removed", metadata);
    setBreakpointStatus("Breakpoint removed");
  } else {
    addBreakpoint(resolvedIndex);
    recordSessionEvent("breakpoint_added", metadata);
    setBreakpointStatus("Breakpoint set");
  }
  persistCurrentDocumentContinuity();
  flashReaderSurface();
  return [...breakpoints];
}

function setBreakpointAtCurrentChunk() {
  return addBreakpoint(currentIndex);
}

function clearBreakpoints() {
  breakpoints = [];
}

function getPreviousBreakpointIndex(fromIndex = currentIndex) {
  const resolvedIndex = clampIndex(fromIndex);
  const previous = normalizeBreakpoints().filter((index) => index < resolvedIndex);
  return previous.length ? previous[previous.length - 1] : null;
}

function getNextBreakpointIndex(fromIndex = currentIndex) {
  const resolvedIndex = clampIndex(fromIndex);
  const next = normalizeBreakpoints().find((index) => index > resolvedIndex);
  return next === undefined ? null : next;
}

function traverseBreakpointOrStep(direction) {
  if (normalizeBreakpoints().length === 0) {
    if (direction === "previous") {
      previousChunk();
    } else {
      nextChunk();
    }
    return;
  }

  const targetIndex = direction === "next"
    ? getNextBreakpointIndex()
    : getPreviousBreakpointIndex();
  if (targetIndex === null) {
    setBreakpointStatus("No breakpoint");
    flashReaderSurface();
    pause({ record: false });
    return;
  }
  startDriftRecoveryToBreakpoint(targetIndex, direction);
}

function jumpToBreakpoint(index, { direction = "unknown" } = {}) {
  if (schedule.length === 0) {
    return false;
  }
  const oldIndex = currentIndex;
  const resolvedIndex = clampIndex(index);
  pause({ record: false, render: false });
  currentIndex = resolvedIndex;
  smoothChunkRun = 0;
  adaptationSuppressedUntilEventCount = sessionEvents.length + 3;
  resetAdaptationWindow();
  renderCurrentChunk();
  updateProgressAnchor({ force: true });
  const navigation = getCurrentNavigationMeta();
  recordSessionEvent("breakpoint_jump", {
    from_index: oldIndex,
    to_index: currentIndex,
    direction,
    breakpoint_count: normalizeBreakpoints().length,
    progress_percent: navigation ? navigation.progress_percent : 0,
  });
  setBreakpointStatus("Jumped to breakpoint");
  flashReaderSurface();
  return true;
}

function startDriftRecoveryToBreakpoint(targetIndex, direction = "unknown") {
  if (schedule.length === 0) {
    return false;
  }
  cancelPendingDriftRecovery("new_drift_recovery");
  const resolvedTargetIndex = clampIndex(targetIndex);
  const leadInIndex = computeLeadInIndex(
    resolvedTargetIndex,
    DRIFT_RECOVERY_LEAD_IN_CHUNKS,
  );
  pause({ record: false, render: false });
  currentIndex = leadInIndex;
  smoothChunkRun = 0;
  adaptationSuppressedUntilEventCount = sessionEvents.length + 3;
  resetAdaptationWindow();
  renderCurrentChunk();
  updateProgressAnchor({ force: true });
  const navigation = getCurrentNavigationMeta();
  driftRecoveryState = {
    active: true,
    pending: true,
    targetBreakpointIndex: resolvedTargetIndex,
    leadInIndex,
    startedAt: Date.now(),
    delayMs: DRIFT_RECOVERY_DELAY_MS,
    direction,
  };
  recordSessionEvent("drift_recovery_started", {
    target_breakpoint_index: resolvedTargetIndex,
    lead_in_index: leadInIndex,
    lead_in_chunks: DRIFT_RECOVERY_LEAD_IN_CHUNKS,
    delay_ms: DRIFT_RECOVERY_DELAY_MS,
    direction,
    progress_percent: navigation ? navigation.progress_percent : 0,
  });
  setBreakpointStatus("Recovering context before breakpoint");
  flashReaderSurface();
  driftRecoveryTimerId = window.setTimeout(
    completeDriftRecovery,
    DRIFT_RECOVERY_DELAY_MS,
  );
  return true;
}

function completeDriftRecovery() {
  if (!driftRecoveryState || !driftRecoveryState.pending) {
    return false;
  }
  const recovery = driftRecoveryState;
  driftRecoveryTimerId = null;
  driftRecoveryState = {
    ...recovery,
    active: false,
    pending: false,
  };
  recordSessionEvent("drift_recovery_resumed", {
    target_breakpoint_index: recovery.targetBreakpointIndex,
    lead_in_index: recovery.leadInIndex,
    delay_ms: recovery.delayMs,
  });
  setBreakpointStatus("Playback resumed");
  play();
  return true;
}

function cancelPendingDriftRecovery(reason = "user_action") {
  if (driftRecoveryTimerId !== null) {
    window.clearTimeout(driftRecoveryTimerId);
    driftRecoveryTimerId = null;
  }
  if (!driftRecoveryState || !driftRecoveryState.pending) {
    driftRecoveryState = null;
    return false;
  }
  const recovery = driftRecoveryState;
  driftRecoveryState = {
    ...recovery,
    active: false,
    pending: false,
  };
  recordSessionEvent("drift_recovery_cancelled", {
    reason,
    target_breakpoint_index: recovery.targetBreakpointIndex,
    lead_in_index: recovery.leadInIndex,
  });
  return true;
}

function getBreakpointMetadata() {
  const normalized = normalizeBreakpoints();
  return {
    count: normalized.length,
    indices: normalized,
    nearest_previous: getPreviousBreakpointIndex(),
    nearest_next: getNextBreakpointIndex(),
    current_is_breakpoint: hasBreakpoint(currentIndex),
  };
}

function getDriftRecoveryMetadata() {
  if (!driftRecoveryState) {
    return {
      active: false,
      pending: false,
      target_breakpoint_index: null,
      lead_in_index: null,
      delay_ms: DRIFT_RECOVERY_DELAY_MS,
      direction: null,
    };
  }
  return {
    active: Boolean(driftRecoveryState.active),
    pending: Boolean(driftRecoveryState.pending),
    target_breakpoint_index: driftRecoveryState.targetBreakpointIndex,
    lead_in_index: driftRecoveryState.leadInIndex,
    delay_ms: driftRecoveryState.delayMs,
    direction: driftRecoveryState.direction,
  };
}

function setBreakpointStatus(message) {
  if (breakpointStatus) {
    breakpointStatus.textContent = message;
  }
}

function flashReaderSurface() {
  if (!readerArea) {
    return;
  }
  readerArea.classList.add("reader-flash");
  window.requestAnimationFrame(() => {
    window.requestAnimationFrame(() => {
      readerArea.classList.remove("reader-flash");
    });
  });
}

function computeLeadInIndex(targetIndex, leadInChunks = 3) {
  return clampIndex(Number(targetIndex || 0) - Number(leadInChunks || 0));
}

function clampPercent(value) {
  const percent = Number(value);
  if (!Number.isFinite(percent)) {
    return 0;
  }
  return Math.min(Math.max(percent, 0), 100);
}

function recordSessionEvent(type, metadata = {}) {
  const item = getCurrentScheduleItem();
  if (sessionStartedAt === null) {
    sessionStartedAt = Date.now();
  }
  sessionEvents.push({
    type,
    timestamp_ms: Date.now(),
    chunk_index: item ? item.index : currentIndex,
    sentence_index: item ? item.sentence_index : null,
    playback_speed: playbackSpeed,
    metadata,
  });
  renderSessionDebug();
}

function resetSessionEvents() {
  sessionEvents = [];
  sessionStartedAt = Date.now();
  completionRecorded = false;
  renderSessionDebug();
}

function getSessionSummary() {
  const elapsedSessionMs = sessionStartedAt === null ? 0 : Date.now() - sessionStartedAt;
  return {
    event_count: sessionEvents.length,
    rewind_count: countSessionEvents("previous_chunk"),
    manual_next_count: countSessionEvents("next_chunk"),
    pause_count: countSessionEvents("pause"),
    speed_change_count: countSessionEvents("speed_changed"),
    completed: sessionEvents.some((event) => event.type === "playback_completed"),
    adaptation_count: countSessionEvents("adaptation_applied"),
    adaptation_enabled: adaptationEnabled,
    last_adaptation_reason: lastAdaptationReason,
    last_adaptation_direction: lastAdaptationDirection,
    current_speed: playbackSpeed,
    current_index: currentIndex,
    total_chunks: schedule.length,
    elapsed_session_ms: elapsedSessionMs,
    estimated_remaining_chunks: Math.max(schedule.length - currentIndex - 1, 0),
    average_effective_duration_ms: getAverageEffectiveDurationMs(),
  };
}

function getAverageEffectiveDurationMs() {
  if (schedule.length === 0) {
    return null;
  }
  const total = schedule.reduce(
    (sum, item) => sum + getEffectiveDurationMs(item),
    0,
  );
  return Math.round(total / schedule.length);
}

function renderSessionDebug() {
  const summary = getSessionSummary();
  sessionEventCount.textContent = summary.event_count;
  sessionRewindCount.textContent = summary.rewind_count;
  sessionPauseCount.textContent = summary.pause_count;
  sessionSpeedChangeCount.textContent = summary.speed_change_count;
  sessionCompleted.textContent = summary.completed ? "Yes" : "No";
  adaptationCount.textContent = summary.adaptation_count;
  sessionCurrentSpeed.textContent = `${summary.current_speed.toFixed(2)}x`;
  sessionAdaptationEnabled.textContent = summary.adaptation_enabled ? "On" : "Off";
}

function countSessionEvents(type) {
  return sessionEvents.filter((event) => event.type === type).length;
}

function recordCompletion() {
  if (completionRecorded) {
    return;
  }
  completionRecorded = true;
  recordSessionEvent("playback_completed");
  maybeAdaptPlaybackSpeed("completion");
}

function resetAdaptationState() {
  adaptationEnabled = true;
  smoothChunkRun = 0;
  adaptationSuppressedUntilEventCount = 0;
  lastAdaptationReason = null;
  lastAdaptationDirection = null;
  lastAdaptationEventIndex = sessionEvents.length;
  renderAdaptationStatus();
}

function setAdaptationEnabled(enabled) {
  cancelPendingDriftRecovery("adaptation_toggle");
  if (adaptationEnabled === enabled) {
    renderAdaptationStatus();
    return;
  }

  adaptationEnabled = enabled;
  persistReaderPreferences();
  resetAdaptationWindow();
  recordSessionEvent(enabled ? "adaptation_enabled" : "adaptation_disabled");
  renderAdaptationStatus();
}

function resetAdaptationWindowFromControl() {
  cancelPendingDriftRecovery("adaptation_reset");
  resetAdaptationWindow();
  adaptationSuppressedUntilEventCount = 0;
  recordSessionEvent("adaptation_reset");
  renderAdaptationStatus();
}

function resetAdaptationWindow() {
  smoothChunkRun = 0;
  lastAdaptationEventIndex = sessionEvents.length;
  renderAdaptationStatus();
}

function countEventsSinceLastAdaptation(type) {
  return sessionEvents
    .slice(lastAdaptationEventIndex)
    .filter((event) => event.type === type).length;
}

function maybeAdaptPlaybackSpeed(reason = "unknown") {
  if (!adaptationEnabled) {
    return;
  }
  if (sessionEvents.length < adaptationSuppressedUntilEventCount) {
    return;
  }

  const eventWindowSize = sessionEvents.length - lastAdaptationEventIndex;
  const rewindCount = countEventsSinceLastAdaptation("previous_chunk");
  const pauseCount = countEventsSinceLastAdaptation("pause");

  if (
    eventWindowSize >= ADAPTATION_MIN_EVENTS &&
    rewindCount >= ADAPTATION_REWIND_THRESHOLD
  ) {
    applyAdaptiveSpeedChange("slower", "rewinds");
    return;
  }

  if (
    eventWindowSize >= ADAPTATION_MIN_EVENTS &&
    pauseCount >= ADAPTATION_PAUSE_THRESHOLD
  ) {
    applyAdaptiveSpeedChange("slower", "pauses");
    return;
  }

  if (smoothChunkRun >= ADAPTATION_SMOOTH_CHUNK_THRESHOLD) {
    applyAdaptiveSpeedChange("faster", reason === "completion" ? "completion" : "smooth_run");
  }
}

function applyAdaptiveSpeedChange(direction, reason) {
  const nextIndex = direction === "faster" ? speedIndex + 1 : speedIndex - 1;
  if (nextIndex < 0 || nextIndex >= SPEED_LEVELS.length) {
    resetAdaptationWindow();
    return false;
  }

  const oldSpeed = playbackSpeed;
  lastAdaptationReason = reason;
  lastAdaptationDirection = direction;
  setSpeedIndex(nextIndex, {
    record: false,
    reschedule: false,
    suppressAdaptation: false,
  });
  recordSessionEvent("adaptation_applied", {
    direction,
    reason,
    from_speed: oldSpeed,
    to_speed: playbackSpeed,
  });
  resetAdaptationWindow();
  renderSpeedControls();
  renderSessionDebug();
  return true;
}

function renderAdaptationStatus() {
  adaptationStatus.textContent = adaptationEnabled ? "On" : "Off";
  adaptationToggle.textContent = adaptationEnabled ? "Disable adaptation" : "Enable adaptation";
  adaptationToggle.setAttribute("aria-pressed", String(adaptationEnabled));
  if (sessionAdaptationEnabled) {
    sessionAdaptationEnabled.textContent = adaptationEnabled ? "On" : "Off";
  }
}
