# S-035 Service Surfaces and Fallback Validation

## Automated Preparation

The committed [S-035 characterization](../../../evaluation/service_surfaces/s035_characterization.json) covers `/health`, validation samples, ingest, chunk, schedule, and bounded defect submission in explicit rule-based mode. It also simulates unavailable parser dependencies and verifies successful automatic rule-based fallback, health-state reporting, reason-category-only logging, source-text exclusion from logs, pinned parser dependencies, dependency-light core requirements, and absence of a runtime model-download call.

Reproduce it with:

```bash
python scripts/characterize_s035_service_surfaces.py --check
```

No service, fallback, serialization, logging, or dependency defect was reproduced, so no runtime stabilization was made.

## Fixed Human Startup And API Protocol

Use project-owned validation text only. Record the operating system, Python version, and browser/client used.

### Parser-default startup

1. Install the standard requirements and start the Flask app without setting `RSVP_CHUNKER_MODE`.
2. Open `/health` and confirm `status` is `ok`, `configured_mode` is `parser_assisted`, `fallback` is `rule_based`, and the pinned provider identity is reported.
3. Load a validation sample in the browser and confirm it schedules and reads normally. Confirm startup and first use do not attempt a model download.

### Explicit dependency-light startup

4. In a clean environment install only `requirements-core.txt`, set `RSVP_CHUNKER_MODE=rule_based`, and start the Flask app.
5. Open `/health` and confirm both configured and active mode are `rule_based`, provider is absent, and fallback remains `rule_based`.
6. Exercise `/api/ingest`, `/api/chunk`, and `/api/schedule` with short project-owned text, then load a validation sample in the browser. Confirm JSON responses and reading remain usable.
7. Submit an intentionally incomplete synthetic `/api/defects` request and confirm a bounded JSON `400` response rather than a server error.

### Disposition

Record `passed`, `partially_passed`, `failed`, or `inconclusive`. For a failure, include the mode, endpoint/startup step, expected and observed state, and whether any source text appeared in fallback logs. S-035 remains open until this human gate is recorded.

## Human Disposition

Human reports passed on all GET method tests. /health API calls and sample loading worked in both standard and core environments. All disallowed GET method API calls weren't made. Don't hand off API custom requests and response validations to human, do them yourself before completing the slice or add them to the appropriate CI workflows.
