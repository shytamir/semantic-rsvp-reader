const form = document.querySelector("#ingest-form");
const input = document.querySelector("#text-input");
const statusMessage = document.querySelector("#status-message");
const sentenceList = document.querySelector("#sentence-list");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  statusMessage.classList.remove("is-error");
  statusMessage.textContent = "Loading...";
  sentenceList.replaceChildren();

  try {
    const response = await fetch("/api/ingest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: input.value }),
    });
    const payload = await response.json();

    if (!response.ok) {
      throw new Error(payload.error || "Unable to ingest text.");
    }

    statusMessage.textContent = `${payload.sentence_count} sentence(s) ready for future playback.`;
    for (const sentence of payload.sentences) {
      const item = document.createElement("li");
      item.textContent = sentence;
      sentenceList.append(item);
    }
  } catch (error) {
    statusMessage.classList.add("is-error");
    statusMessage.textContent = error.message;
  }
});
