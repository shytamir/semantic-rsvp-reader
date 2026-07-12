(function initializeContinuity(root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  }
  if (root) {
    root.SemanticRSVPContinuity = api;
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function buildContinuity() {
  const VERSION = 1;
  const PREFERENCES_KEY = "semantic-rsvp-reader.preferences.v1";
  const DOCUMENTS_KEY = "semantic-rsvp-reader.documents.v1";
  const MAX_DOCUMENTS = 12;
  const MAX_BREAKPOINTS = 64;
  const STALE_AFTER_MS = 90 * 24 * 60 * 60 * 1000;

  function normalizeSourceText(rawText) {
    let text = String(rawText || "").normalize("NFC");
    text = text.replace(/\r\n?/g, "\n");
    text = text.replace(/([A-Za-z0-9])"(?=[A-Za-z])/g, '$1" ');
    text = text
      .split("\n")
      .map((line) => line.replace(/[ \t]+/g, " ").trim())
      .join("\n");
    return text.replace(/\n{3,}/g, "\n\n").trim();
  }

  async function computeDocumentId(
    rawText,
    sourceType = "inline_text",
    cryptoObject = globalThis.crypto,
  ) {
    if (!cryptoObject || !cryptoObject.subtle) {
      throw new Error("Web Crypto is unavailable.");
    }
    const material = `source-document-v1\0${sourceType}\0${normalizeSourceText(rawText)}`;
    const digest = await cryptoObject.subtle.digest(
      "SHA-256",
      new TextEncoder().encode(material),
    );
    return [...new Uint8Array(digest)]
      .map((value) => value.toString(16).padStart(2, "0"))
      .join("");
  }

  function resolveDocumentState(record, scheduleLength) {
    const lastIndex = Math.max(Number(scheduleLength || 0) - 1, 0);
    const position = Math.min(Math.max(Number(record.position || 0), 0), lastIndex);
    const breakpoints = [...new Set(record.breakpoints || [])]
      .filter((value) => Number.isInteger(value) && value >= 0)
      .map((value) => Math.min(value, lastIndex))
      .filter((value, index, values) => values.indexOf(value) === index)
      .sort((left, right) => left - right)
      .slice(0, MAX_BREAKPOINTS);
    return { position, breakpoints };
  }

  function createStore(storage, now = () => Date.now()) {
    function read(key) {
      try {
        return storage ? storage.getItem(key) : null;
      } catch (_error) {
        return null;
      }
    }

    function write(key, value) {
      try {
        if (storage) {
          storage.setItem(key, JSON.stringify(value));
        }
        return true;
      } catch (_error) {
        return false;
      }
    }

    function remove(key) {
      try {
        if (storage) {
          storage.removeItem(key);
        }
      } catch (_error) {
        return;
      }
    }

    function parse(key) {
      const raw = read(key);
      if (!raw) {
        return null;
      }
      try {
        return JSON.parse(raw);
      } catch (_error) {
        remove(key);
        return null;
      }
    }

    function loadPreferences() {
      const record = parse(PREFERENCES_KEY);
      if (
        !record ||
        record.version !== VERSION ||
        !Number.isInteger(record.speed_index) ||
        typeof record.adaptation_enabled !== "boolean"
      ) {
        if (record) {
          remove(PREFERENCES_KEY);
        }
        return null;
      }
      return {
        speed_index: record.speed_index,
        adaptation_enabled: record.adaptation_enabled,
      };
    }

    function savePreferences(preferences) {
      if (
        !preferences ||
        !Number.isInteger(preferences.speed_index) ||
        typeof preferences.adaptation_enabled !== "boolean"
      ) {
        return false;
      }
      return write(PREFERENCES_KEY, { version: VERSION, ...preferences });
    }

    function validDocument(record) {
      return Boolean(
        record &&
          typeof record.document_id === "string" &&
          /^[0-9a-f]{64}$/.test(record.document_id) &&
          typeof record.source_type === "string" &&
          record.source_type.length <= 64 &&
          typeof record.display_name === "string" &&
          record.display_name.length <= 128 &&
          Number.isInteger(record.position) &&
          record.position >= 0 &&
          Array.isArray(record.breakpoints) &&
          record.breakpoints.every((value) => Number.isInteger(value) && value >= 0) &&
          Number.isFinite(record.updated_at)
      );
    }

    function loadDocuments() {
      const container = parse(DOCUMENTS_KEY);
      if (!container || container.version !== VERSION || !Array.isArray(container.documents)) {
        if (container) {
          remove(DOCUMENTS_KEY);
        }
        return [];
      }
      const cutoff = now() - STALE_AFTER_MS;
      const documents = container.documents
        .filter(validDocument)
        .filter((record) => record.updated_at >= cutoff && record.updated_at <= now())
        .map((record) => ({
          ...record,
          breakpoints: [...new Set(record.breakpoints)].slice(0, MAX_BREAKPOINTS),
        }))
        .sort((left, right) => right.updated_at - left.updated_at)
        .slice(0, MAX_DOCUMENTS);
      if (documents.length !== container.documents.length) {
        write(DOCUMENTS_KEY, { version: VERSION, documents });
      }
      return documents;
    }

    function getDocument(documentId) {
      return loadDocuments().find((record) => record.document_id === documentId) || null;
    }

    function saveDocument(record) {
      if (!validDocument(record)) {
        return false;
      }
      const normalized = {
        ...record,
        source_type: record.source_type.slice(0, 64),
        display_name: record.display_name.slice(0, 128),
        breakpoints: [...new Set(record.breakpoints)]
          .sort((left, right) => left - right)
          .slice(0, MAX_BREAKPOINTS),
        updated_at: now(),
      };
      const documents = loadDocuments().filter(
        (item) => item.document_id !== normalized.document_id,
      );
      documents.unshift(normalized);
      return write(DOCUMENTS_KEY, {
        version: VERSION,
        documents: documents.slice(0, MAX_DOCUMENTS),
      });
    }

    function removeDocument(documentId) {
      const documents = loadDocuments().filter(
        (record) => record.document_id !== documentId,
      );
      return write(DOCUMENTS_KEY, { version: VERSION, documents });
    }

    function clearAll() {
      remove(PREFERENCES_KEY);
      remove(DOCUMENTS_KEY);
    }

    return {
      clearAll,
      getDocument,
      loadDocuments,
      loadPreferences,
      removeDocument,
      saveDocument,
      savePreferences,
    };
  }

  return {
    DOCUMENTS_KEY,
    MAX_BREAKPOINTS,
    MAX_DOCUMENTS,
    PREFERENCES_KEY,
    STALE_AFTER_MS,
    VERSION,
    computeDocumentId,
    createStore,
    normalizeSourceText,
    resolveDocumentState,
  };
});
