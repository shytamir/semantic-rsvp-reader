# Portfolio Demonstration Package

This is the repository-owned S-043 package for a local portfolio demonstration. It is deterministic, offline after dependency setup, and limited to the validated prototype. The immutable demonstration SHA is recorded in the [S-043 handoff](../validation/s043_portfolio_demonstration_rehearsal.md) after the package commit exists.

## Run It

1. Use the `standard` profile in the [environment contract](../development/environment_contract.md) with Python 3.12 and clear any inherited `RSVP_CHUNKER_MODE` override.
2. Verify all three committed EPUB paths with `python scripts/build_portfolio_demo_epub.py --check`.
3. Start with `python -m flask --app semantic_rsvp.web:create_app run` and open `http://127.0.0.1:5000`.
4. Use [portfolio-demo.md](../../samples/portfolio-demo.md) and the three EPUB paths below with the [short](short_protocol.md) or [full](full_protocol.md) protocol.

## EPUB Paths

- [Unchanged](../../samples/portfolio-demo.epub): already demo-safe and passed through byte-for-byte.
- [Normalized](../../samples/portfolio-demo-normalization-required.epub): legacy doctype, `<link>`, `<meta>`, CSS, and style attributes are simplified transiently before final ingestion.
- [Bounded failure](../../samples/portfolio-demo-encrypted-rejected.epub): synthetic encryption declaration is rejected without opening the reader.

The EPUBs can be regenerated only when their project-owned source elements intentionally change: `python scripts/build_portfolio_demo_epub.py --write`. The script fixes entry order, timestamps, permissions, and compression choices so `--check` compares exact bytes.

## Package Map

- [Short protocol](short_protocol.md): three-to-five-minute interview path.
- [Full protocol](full_protocol.md): approximately ten-minute technical path.
- [Repository orientation](repository_orientation.md): concise architecture and evidence map.
- [Supported claims and limitations](supported_claims_and_limitations.md): safe statements and explicit boundaries.
- [Fallback package](fallback_package.md): offline recovery order with no fabricated media.
- [Human rehearsal handoff](../validation/s043_portfolio_demonstration_rehearsal.md): fixed twelve-step gate owned by Human.

All inputs are synthetic, project-owned, and covered by the repository license. No private evaluation material, credentials, third-party book content, screenshots, or recordings are included.
