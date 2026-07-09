const SWIPE_MIN_DISTANCE_PX = 40;
const SWIPE_MAX_VERTICAL_DRIFT_PX = 60;
const LONG_PRESS_MS = 500;
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

let schedule = [];
let currentIndex = 0;
let isPlaying = false;
let timerId = null;
let touchStartX = 0;
let touchStartY = 0;
let touchStartTime = 0;
let longPressTimerId = null;
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
speedOverlay.addEventListener("pointerdown", stopOverlayGesturePropagation);
speedOverlay.addEventListener("pointermove", stopOverlayGesturePropagation);
speedOverlay.addEventListener("pointerup", stopOverlayGesturePropagation);
speedOverlay.addEventListener("click", stopOverlayGesturePropagation);
defectPanel.addEventListener("pointerdown", stopOverlayGesturePropagation);
defectPanel.addEventListener("pointermove", stopOverlayGesturePropagation);
defectPanel.addEventListener("pointerup", stopOverlayGesturePropagation);
defectPanel.addEventListener("click", stopOverlayGesturePropagation);
attachReaderGestures();
renderSpeedControls();
renderSessionDebug();
renderAdaptationStatus();
renderDefectCount();
loadValidationSamples();

async function loadSchedule(text) {
  if (isLoading) {
    return;
  }

  pause({ record: false, render: false });
  hideSpeedOverlay();
  setLoading(true);
  showStatus("Preparing...");

  try {
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
    defectReportCount = 0;
    lastDefectReportId = null;
    resetSpeed({ record: false });
    resetSessionEvents();
    resetAdaptationState();
    renderDefectCount();
    recordSessionEvent("schedule_loaded", {
      chunk_count: schedule.length,
      sentence_count: payload.sentence_count,
    });
    enterReaderMode();
  } catch (error) {
    schedule = [];
    scheduledSentences = [];
    currentIndex = 0;
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

  for (const sample of samples) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "sample-button";
    button.textContent = `${sample.id} ${sample.category}`;
    button.setAttribute("aria-label", `Load validation sample ${sample.id}`);
    button.addEventListener("click", () => loadValidationSample(sample));
    sampleList.appendChild(button);
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
    setChunkDisplaySizing("No text loaded");
    progressIndicator.textContent = "0 / 0";
    playPauseButton.textContent = "Play";
    return;
  }

  currentIndex = clampIndex(currentIndex);
  const item = schedule[currentIndex];
  chunkDisplay.textContent = item.text;
  setChunkDisplaySizing(item.text);
  progressIndicator.textContent = `${currentIndex + 1} / ${schedule.length}`;
  playPauseButton.textContent = isPlaying ? "Pause" : "Play";
}

function openDefectPanel() {
  if (!isReaderModeActive() || schedule.length === 0) {
    return;
  }

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
  chunkDisplay.classList.toggle("is-long-chunk", String(text || "").length > 24);
  chunkDisplay.classList.toggle("is-extra-long-token", longestWordLength > 12);
}

function getChunkDisplayMetadata() {
  return {
    display_width_px: Math.round(readerArea ? readerArea.clientWidth : 0),
    chunk_scroll_width_px: Math.round(chunkDisplay ? chunkDisplay.scrollWidth : 0),
    chunk_client_width_px: Math.round(chunkDisplay ? chunkDisplay.clientWidth : 0),
    chunk_may_overflow: Boolean(
      chunkDisplay && chunkDisplay.scrollWidth > chunkDisplay.clientWidth + 1,
    ),
  };
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

  if (isPlaying) {
    pause();
  } else {
    play();
  }
}

function nextChunk({ auto = false } = {}) {
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
}

function resetReader() {
  const oldIndex = currentIndex;
  currentIndex = 0;
  recordSessionEvent("reset", {
    from_index: oldIndex,
    to_index: currentIndex,
  });
  resetAdaptationWindow();
  pause();
}

function enterInputMode() {
  recordSessionEvent("back_to_input");
  pause();
  hideSpeedOverlay();
  closeDefectPanel();
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
  renderCurrentChunk();
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
      previousChunk();
    } else {
      nextChunk();
    }
    window.setTimeout(() => {
      suppressNextTap = false;
    }, 0);
    return;
  }

  if (Math.hypot(deltaX, deltaY) <= TAP_MAX_DISTANCE_PX && elapsed < LONG_PRESS_MS) {
    togglePlayback();
  }
}

function cancelGesture(event) {
  releasePointerCapture(event);
  gestureStarted = false;
  suppressNextTap = false;
  longPressActivated = false;
  clearLongPressTimer();
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
  renderSpeedControls();
  speedOverlay.classList.toggle("is-hidden");
}

function hideSpeedOverlay() {
  speedOverlay.classList.add("is-hidden");
}

function clearLongPressTimer() {
  if (longPressTimerId !== null) {
    window.clearTimeout(longPressTimerId);
    longPressTimerId = null;
  }
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
  if (adaptationEnabled === enabled) {
    renderAdaptationStatus();
    return;
  }

  adaptationEnabled = enabled;
  resetAdaptationWindow();
  recordSessionEvent(enabled ? "adaptation_enabled" : "adaptation_disabled");
  renderAdaptationStatus();
}

function resetAdaptationWindowFromControl() {
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
