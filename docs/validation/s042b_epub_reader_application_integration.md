# S-042B EPUB Reader Application Integration Validation

## Scope

S-042B connects the bounded S-042A adapter to the existing RSVP reader through
one dedicated raw-byte request. It adds no contents UI, heading navigation,
source persistence, new resume control, or playback-policy change. It has no
human gate and is dispositioned only from objective evidence.

## Local Evidence

Focused route, integration, continuity, and reader checks passed: 50 passed and
one documented Node-dependent check skipped. S-031 characterization passed after
the existing pasted-text initialization remained verbatim. S-032 and S-033
records were refreshed only for the authorized application/template source
hashes; their behavioral invariants remained passing. The provisional
integration record changed only the registered `semantic_rsvp/web.py` hash.

The applicable full suite completed 328 passing tests and one documented
Node-dependent skip before two registered-hash checks identified the authorized
`web.py` integration change. After updating only the integration hash and its
derived S-037 source-evidence identity, the affected repository/S-037 checks
passed 7 of 7. The 22-case corpus, frozen rule-based baseline, and S-037 semantic
characterization remained reproducible.

The optional security runner reported Bandit, pip-audit, Semgrep, Gitleaks, and
detect-secrets unavailable and skipped; focused malformed/media-type/boundary
security cases passed. JavaScript syntax reported its documented local
Node-unavailable skip. Full-suite, repository, frozen-evidence, and browser-smoke
results are recorded after the implementation push.

## Remote Evidence And Disposition

CI run `29214042029` for head `9381c5f` recorded a real S-042B regression. The
browser-smoke job timed out waiting for `#reader-mode` to become visible. Its
mocked EPUB schedule supplied progress and source offsets but omitted required
`navigation.paragraph_index`; the unchanged browser response validator rejected
that malformed mock before reader initialization. This was not pending or flaky
evidence. The smoke fixture now supplies the required field without weakening
its baseline reader, canonical identity, dedicated boundary, continuity, or
byte-non-persistence assertions.

That run's integrity job passed. Its Core job ran 325 tests successfully and
then encountered the separately known S-031 characterization mismatch; CodeQL
run `29214041836` passed. Final disposition follows the stabilization commit's
terminal local and remote results.

After the smoke-fixture correction, focused EPUB, continuity, shell,
characterization, and repository checks passed 39 tests with one documented
Node-dependent skip. The full managed suite passed 330 tests with the same one
skip. The 22-case corpus, frozen rule-based baseline, S-031 and S-037
characterizations, repository integrity, Markdown links, and diff whitespace
passed. Local execution of the Playwright smoke remained unavailable because
Node was not installed; the CI browser job is the authoritative execution of
that unchanged harness.
