const SWIPE_MIN_DISTANCE_PX = 40;
const SWIPE_MAX_VERTICAL_DRIFT_PX = 60;
const LONG_PRESS_MS = 500;
const TAP_MAX_DISTANCE_PX = 12;
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
const statusMessage = document.querySelector("#status-message");
const readerArea = document.querySelector("#reader-area");
const chunkDisplay = document.querySelector("#chunk-display");
const progressIndicator = document.querySelector("#progress-indicator");
const playPauseButton = document.querySelector("#play-pause-button");
const previousButton = document.querySelector("#previous-button");
const nextButton = document.querySelector("#next-button");
const resetButton = document.querySelector("#reset-button");
const backButton = document.querySelector("#back-button");
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
let speedIndex = DEFAULT_SPEED_INDEX;
let playbackSpeed = SPEED_LEVELS[speedIndex];
let sessionEvents = [];
let sessionStartedAt = null;
let completionRecorded = false;
let adaptationEnabled = true;
let lastAdaptationEventIndex = 0;
let smoothChunkRun = 0;
let adaptationSuppressedUntilEventCount = 0;

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  await loadSchedule(input.value);
});

playPauseButton.addEventListener("click", togglePlayback);
previousButton.addEventListener("click", previousChunk);
nextButton.addEventListener("click", () => nextChunk());
resetButton.addEventListener("click", resetReader);
backButton.addEventListener("click", enterInputMode);
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
attachReaderGestures();
renderSpeedControls();
renderSessionDebug();
renderAdaptationStatus();

async function loadSchedule(text) {
  pause({ record: false });
  hideSpeedOverlay();
  showStatus("Preparing...");

  try {
    const response = await fetch("/api/schedule", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const payload = await response.json();

    if (!response.ok) {
      throw new Error(payload.error || "Unable to prepare text.");
    }
    if (!Array.isArray(payload.schedule) || payload.schedule.length === 0) {
      throw new Error("No readable chunks were returned.");
    }

    schedule = payload.schedule;
    currentIndex = 0;
    resetSpeed({ record: false });
    resetSessionEvents();
    resetAdaptationState();
    recordSessionEvent("schedule_loaded", {
      chunk_count: schedule.length,
      sentence_count: payload.sentence_count,
    });
    enterReaderMode();
  } catch (error) {
    schedule = [];
    currentIndex = 0;
    showError(error.message);
  }
}

function renderCurrentChunk() {
  if (schedule.length === 0) {
    chunkDisplay.textContent = "No text loaded";
    progressIndicator.textContent = "0 / 0";
    playPauseButton.textContent = "Play";
    return;
  }

  currentIndex = clampIndex(currentIndex);
  const item = schedule[currentIndex];
  chunkDisplay.textContent = item.text;
  progressIndicator.textContent = `${currentIndex + 1} / ${schedule.length}`;
  playPauseButton.textContent = isPlaying ? "Pause" : "Play";
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

function pause({ record = true } = {}) {
  const wasPlaying = isPlaying;
  isPlaying = false;
  clearPlaybackTimer();
  if (record && wasPlaying) {
    recordSessionEvent("pause");
    smoothChunkRun = 0;
    maybeAdaptPlaybackSpeed("pause");
  }
  renderCurrentChunk();
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
  const oldIndex = currentIndex;
  currentIndex = Math.max(0, currentIndex - 1);
  recordSessionEvent("previous_chunk", {
    from_index: oldIndex,
    to_index: currentIndex,
  });
  smoothChunkRun = 0;
  maybeAdaptPlaybackSpeed("rewind");
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
  renderCurrentChunk();
  renderSessionDebug();
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

function renderCompletion() {
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
  clearLongPressTimer();
}

function handleLongPress() {
  if (!gestureStarted || !isReaderModeActive()) {
    return;
  }

  suppressNextTap = true;
  clearLongPressTimer();
  toggleSpeedOverlay();
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
  return {
    event_count: sessionEvents.length,
    rewind_count: countSessionEvents("previous_chunk"),
    manual_next_count: countSessionEvents("next_chunk"),
    pause_count: countSessionEvents("pause"),
    speed_change_count: countSessionEvents("speed_changed"),
    completed: sessionEvents.some((event) => event.type === "playback_completed"),
    adaptation_count: countSessionEvents("adaptation_applied"),
    adaptation_enabled: adaptationEnabled,
    current_speed: playbackSpeed,
    current_index: currentIndex,
    total_chunks: schedule.length,
  };
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
