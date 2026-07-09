const SWIPE_MIN_DISTANCE_PX = 40;
const SWIPE_MAX_VERTICAL_DRIFT_PX = 60;
const LONG_PRESS_MS = 500;
const TAP_MAX_DISTANCE_PX = 12;

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
const speedOverlayClose = document.querySelector("#speed-overlay-close");

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

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  await loadSchedule(input.value);
});

playPauseButton.addEventListener("click", togglePlayback);
previousButton.addEventListener("click", previousChunk);
nextButton.addEventListener("click", () => nextChunk());
resetButton.addEventListener("click", resetReader);
backButton.addEventListener("click", enterInputMode);
speedOverlayClose.addEventListener("click", hideSpeedOverlay);
attachReaderGestures();

async function loadSchedule(text) {
  pause();
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
  renderCurrentChunk();
  scheduleNextChunk();
}

function pause() {
  isPlaying = false;
  clearPlaybackTimer();
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
    pause();
    return;
  }

  if (currentIndex >= schedule.length - 1) {
    currentIndex = schedule.length - 1;
    pause();
    renderCompletion();
    return;
  }

  currentIndex += 1;

  if (auto && isPlaying) {
    renderCurrentChunk();
    scheduleNextChunk();
  } else {
    pause();
  }
}

function previousChunk() {
  currentIndex = Math.max(0, currentIndex - 1);
  pause();
}

function resetReader() {
  currentIndex = 0;
  pause();
}

function enterInputMode() {
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
    Number.isFinite(duration) && duration > 0 ? duration : 400,
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
