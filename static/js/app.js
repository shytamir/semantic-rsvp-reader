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

let schedule = [];
let currentIndex = 0;
let isPlaying = false;
let timerId = null;

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  await loadSchedule(input.value);
});

playPauseButton.addEventListener("click", togglePlayback);
previousButton.addEventListener("click", previousChunk);
nextButton.addEventListener("click", () => nextChunk());
resetButton.addEventListener("click", resetReader);
backButton.addEventListener("click", enterInputMode);
readerArea.addEventListener("click", togglePlayback);

async function loadSchedule(text) {
  pause();
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
  readerMode.classList.add("is-hidden");
  inputMode.classList.remove("is-hidden");
  showStatus("Prepare text to start reading.");
}

function enterReaderMode() {
  inputMode.classList.add("is-hidden");
  readerMode.classList.remove("is-hidden");
  isPlaying = false;
  clearPlaybackTimer();
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
