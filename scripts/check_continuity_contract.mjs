import assert from "node:assert/strict";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const continuity = require("../static/js/continuity.js");

class MemoryStorage {
  constructor() {
    this.items = new Map();
  }

  getItem(key) {
    return this.items.has(key) ? this.items.get(key) : null;
  }

  setItem(key, value) {
    this.items.set(key, String(value));
  }

  removeItem(key) {
    this.items.delete(key);
  }
}

const now = 1_800_000_000_000;
const storage = new MemoryStorage();
const store = continuity.createStore(storage, () => now);

assert.equal(
  await continuity.computeDocumentId("First.\r\nSecond."),
  "41c5632dced6f5dfe91629fdb5689c231db41495f61a42298bdee0c830cf9915",
  "browser identity must match the SourceDocument contract",
);

assert.equal(store.loadPreferences(), null);
assert.equal(
  store.savePreferences({ speed_index: 4, adaptation_enabled: false }),
  true,
);
assert.deepEqual(store.loadPreferences(), {
  speed_index: 4,
  adaptation_enabled: false,
});

for (let index = 0; index < 14; index += 1) {
  store.saveDocument({
    document_id: index.toString(16).padStart(64, "0"),
    source_type: "inline_text",
    display_name: `Document ${index}`,
    position: index,
    breakpoints: Array.from({ length: 70 }, (_, item) => item),
    updated_at: now,
  });
}
assert.equal(store.loadDocuments().length, continuity.MAX_DOCUMENTS);
assert.equal(store.loadDocuments()[0].breakpoints.length, continuity.MAX_BREAKPOINTS);

const resolved = continuity.resolveDocumentState(
  { position: 999, breakpoints: [-1, 2, 2, 999] },
  5,
);
assert.deepEqual(resolved, { position: 4, breakpoints: [2, 4] });

const serializedDocuments = storage.getItem(continuity.DOCUMENTS_KEY);
for (const excluded of ["source_text", "defect", "session", "telemetry", "timer"]) {
  assert.equal(serializedDocuments.includes(excluded), false);
}

storage.setItem(continuity.PREFERENCES_KEY, "not-json");
assert.equal(store.loadPreferences(), null);
assert.equal(storage.getItem(continuity.PREFERENCES_KEY), null);

storage.setItem(
  continuity.DOCUMENTS_KEY,
  JSON.stringify({
    version: continuity.VERSION,
    documents: [
      {
        document_id: "f".repeat(64),
        source_type: "inline_text",
        display_name: "Stale",
        position: 1,
        breakpoints: [],
        updated_at: now - continuity.STALE_AFTER_MS - 1,
      },
    ],
  }),
);
assert.deepEqual(store.loadDocuments(), []);

storage.setItem(
  continuity.DOCUMENTS_KEY,
  JSON.stringify({ version: continuity.VERSION + 1, documents: [] }),
);
assert.deepEqual(store.loadDocuments(), []);
assert.equal(storage.getItem(continuity.DOCUMENTS_KEY), null);

store.clearAll();
assert.equal(storage.getItem(continuity.PREFERENCES_KEY), null);
assert.equal(storage.getItem(continuity.DOCUMENTS_KEY), null);

console.log("S-041 continuity contract checks passed.");
