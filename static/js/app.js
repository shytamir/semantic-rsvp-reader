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

    statusMessage.textContent = `${payload.sentence_count} sentence(s) chunked for future playback.`;
    for (const sentenceResult of payload.chunked_sentences) {
      const item = document.createElement("li");
      const sentenceText = document.createElement("p");
      sentenceText.className = "sentence-text";
      sentenceText.textContent = sentenceResult.sentence;

      const chunks = document.createElement("div");
      chunks.className = "chunk-list";

      for (const chunk of sentenceResult.chunks) {
        const chip = document.createElement("span");
        chip.className = `chunk-chip chunk-${chunk.syntactic_hint}`;
        chip.textContent = chunk.text;
        chunks.append(chip);
      }

      item.append(sentenceText, chunks);
      sentenceList.append(item);
    }
  } catch (error) {
    statusMessage.classList.add("is-error");
    statusMessage.textContent = error.message;
  }
});
