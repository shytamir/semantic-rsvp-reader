import { spawn } from "node:child_process";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const host = "127.0.0.1";
const port = Number(process.env.RSVP_BROWSER_SMOKE_PORT || 5058);
const baseUrl = `http://${host}:${port}`;
const python = process.env.PYTHON || "python";
const browserChannel = process.env.RSVP_BROWSER_CHANNEL || undefined;
const fixture = [
  "# Browser Smoke Fixture",
  "",
  "The first deterministic paragraph provides enough words for playback, pause, seeking, and breakpoint checks without depending on external content.",
  "",
  "## Reset Boundary",
  "",
  "The second deterministic paragraph confirms that reset returns to the first scheduled chunk while navigation metadata remains available.",
].join("\n");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

async function waitForServer(processHandle) {
  const deadline = Date.now() + 20_000;
  while (Date.now() < deadline) {
    if (processHandle.exitCode !== null) {
      throw new Error(`Flask exited before browser smoke startup (${processHandle.exitCode}).`);
    }
    try {
      const response = await fetch(`${baseUrl}/health`);
      if (response.ok) {
        return;
      }
    } catch {
      // The development server is still starting.
    }
    await new Promise((resolve) => setTimeout(resolve, 200));
  }
  throw new Error("Timed out waiting for the Flask browser-smoke server.");
}

async function runSmoke(page) {
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto(baseUrl, { waitUntil: "networkidle" });

  await page.locator("#text-input").fill(fixture);
  await page.locator("#prepare-button").click();
  await page.locator("#reader-mode").waitFor({ state: "visible" });

  const initialProgress = await page.locator("#progress-indicator").textContent();
  const total = Number(initialProgress?.match(/^1 \/ (\d+)$/)?.[1]);
  assert(Number.isInteger(total) && total >= 6, "Text loading did not create the expected deterministic schedule.");

  await page.locator("#play-pause-button").click();
  await page.locator("#play-pause-button").waitFor({ state: "visible" });
  assert((await page.locator("#play-pause-button").textContent()) === "Pause", "Playback did not start.");
  await page.locator("#play-pause-button").click();
  assert((await page.locator("#play-pause-button").textContent()) === "Play", "Playback did not pause.");

  const progressAnchor = page.locator("#progress-anchor");
  const bounds = await progressAnchor.boundingBox();
  assert(bounds && bounds.width > 0, "Progress seek control is not measurable.");
  await page.mouse.click(bounds.x + bounds.width * 0.75, bounds.y + bounds.height / 2);
  const soughtProgress = await page.locator("#progress-indicator").textContent();
  const soughtIndex = Number(soughtProgress?.match(/^(\d+) \/ \d+$/)?.[1]);
  assert(soughtIndex > 1 && soughtIndex <= total, "Progress seeking did not move to a later chunk.");

  await page.locator("#reader-area").click();
  await page.waitForTimeout(100);
  await page.locator("#reader-area").click();
  await page.locator("#breakpoint-status").filter({ hasText: "Breakpoint set" }).waitFor();

  await page.locator("#reset-button").click();
  assert((await page.locator("#progress-indicator").textContent()) === `1 / ${total}`, "Reset did not return to the first chunk.");
  assert((await page.locator("#play-pause-button").textContent()) === "Play", "Reset did not leave playback paused.");

  await page.setViewportSize({ width: 320, height: 568 });
  const layout = await page.evaluate(() => {
    const reader = document.querySelector("#reader-mode").getBoundingClientRect();
    const controls = document.querySelector(".reader-controls").getBoundingClientRect();
    return {
      documentWidth: document.documentElement.scrollWidth,
      viewportWidth: window.innerWidth,
      readerLeft: reader.left,
      readerRight: reader.right,
      controlsLeft: controls.left,
      controlsRight: controls.right,
      controlsVisible: controls.width > 0 && controls.height > 0,
    };
  });
  assert(layout.documentWidth <= layout.viewportWidth, "Narrow layout has catastrophic horizontal document overflow.");
  assert(layout.readerLeft >= 0 && layout.readerRight <= layout.viewportWidth, "Reader escapes the narrow viewport.");
  assert(
    layout.controlsVisible && layout.controlsLeft >= 0 && layout.controlsRight <= layout.viewportWidth,
    "Critical reader controls escape the narrow viewport.",
  );

  const canonicalId = "a".repeat(64);
  await page.route("**/api/epub/schedule", async (route) => {
    const request = route.request();
    assert(request.method() === "POST", "EPUB bridge did not use POST.");
    assert(request.headers()["content-type"] === "application/epub+zip", "EPUB bridge changed its dedicated media type.");
    assert(request.headers()["x-epub-filename"] === "smoke.epub", "EPUB filename metadata was not bounded to the dedicated request.");
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        document: { document_id: canonicalId, source_type: "epub", display_name: "Smoke EPUB", source_name: "smoke.epub" },
        sentence_count: 1,
        sentences: ["EPUB reader bridge smoke content."],
        schedule: [{
          index: 0,
          sentence_index: 0,
          text: "EPUB reader bridge smoke content.",
          content_word_count: 5,
          char_length: 33,
          syntactic_hint: null,
          duration_ms: 900,
          in_quote: false,
          quote_boundary: null,
          in_parenthetical: false,
          parenthetical_depth: 0,
          navigation: { progress_percent: 100, paragraph_index: 0, source_start: 0, source_end: 33 },
          structure: { active_h1: null, active_h2: null, active_path: [] },
        }],
      }),
    });
  });
  await page.reload({ waitUntil: "networkidle" });
  await page.locator("#epub-input").setInputFiles({
    name: "smoke.epub",
    mimeType: "application/epub+zip",
    buffer: Buffer.from("browser smoke fixture"),
  });
  await page.locator("#prepare-epub-button").click();
  await page.locator("#reader-mode").waitFor({ state: "visible" });
  assert((await page.locator("#chunk-display").textContent()) === "EPUB reader bridge smoke content.", "EPUB response did not enter the existing reader.");
  const saved = await page.evaluate(() => JSON.parse(localStorage.getItem("semantic-rsvp-reader.documents.v1")));
  assert(saved.documents[0].document_id === canonicalId, "EPUB continuity did not use the canonical server identity.");
  assert(saved.documents[0].source_type === "epub", "EPUB continuity did not preserve source type.");
  assert(!JSON.stringify(saved).includes("browser smoke fixture"), "EPUB bytes leaked into continuity storage.");
}

const flask = spawn(
  python,
  ["-m", "flask", "--app", "semantic_rsvp.web:create_app", "run", "--host", host, "--port", String(port), "--no-debugger", "--no-reload"],
  {
    cwd: process.cwd(),
    env: { ...process.env, RSVP_CHUNKER_MODE: "rule_based" },
    stdio: ["ignore", "pipe", "pipe"],
    windowsHide: true,
  },
);

let browser;
try {
  await waitForServer(flask);
  browser = await chromium.launch({ headless: true, channel: browserChannel });
  const page = await browser.newPage();
  await runSmoke(page);
  console.log("Browser smoke passed: baseline reader flows, narrow layout, and canonical EPUB application identity.");
} finally {
  await browser?.close();
  flask.kill();
}
