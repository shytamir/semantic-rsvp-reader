# Bounded Demonstration Fallback

Use this offline sequence if the live browser path cannot be completed:

1. Show [portfolio-demo.md](../../samples/portfolio-demo.md) and explain how its H1/H2 structure becomes schedule structure.
2. Show the source elements in [the project-owned EPUB fixture](../../tests/fixtures/epub/README.md), then verify [portfolio-demo.epub](../../samples/portfolio-demo.epub) with `python scripts/build_portfolio_demo_epub.py --check`.
3. Walk through the [repository orientation](repository_orientation.md), [EPUB contract](../features/epub_ingestion.md), and [supported claims](supported_claims_and_limitations.md).
4. Show the automated command results and terminal GitHub Actions links recorded in the [S-043 handoff](../validation/s043_portfolio_demonstration_rehearsal.md).
5. If the app starts but a prepared input fails, switch once between the text and EPUB paths. If both fail, stop and record a rehearsal blocker rather than altering the environment or using unapproved material.

No screenshots or recording are committed because no human-captured media exists and S-043 forbids fabricated evidence. The committed source inputs, deterministic builder, protocols, evidence links, and architecture map are the complete bounded fallback. A future human-created screenshot or recording is optional and must not replace live or automated evidence.
