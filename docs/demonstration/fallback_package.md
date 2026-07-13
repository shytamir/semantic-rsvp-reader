# Bounded Demonstration Fallback

Use this offline sequence if the live browser path cannot be completed:

1. Show [portfolio-demo.md](../../samples/portfolio-demo.md) and explain how its H1/H2 structure becomes schedule structure.
2. Verify the [unchanged](../../samples/portfolio-demo.epub), [normalization-required](../../samples/portfolio-demo-normalization-required.epub), and [encrypted rejection](../../samples/portfolio-demo-encrypted-rejected.epub) EPUBs with `python scripts/build_portfolio_demo_epub.py --check`.
3. Demonstrate the persistent offline CLI path when useful: `python scripts/convert_epub_to_demo_subset.py samples/portfolio-demo-normalization-required.epub prepared-portfolio-demo.epub`. The output is local demonstration residue; remove it after use and never commit it.
4. Walk through the [repository orientation](repository_orientation.md), [EPUB contract](../features/epub_ingestion.md), and [supported claims](supported_claims_and_limitations.md).
5. Show the automated command results and terminal GitHub Actions links recorded in the [S-043 handoff](../validation/s043_portfolio_demonstration_rehearsal.md).
6. If a live EPUB path fails unexpectedly, show the deterministic files and their focused evidence without substituting arbitrary books. If the documented fallback also fails, stop and record a rehearsal blocker.

No screenshots or recording are committed because no human-captured media exists and S-043 forbids fabricated evidence. The committed source inputs, deterministic builder, protocols, evidence links, and architecture map are the complete bounded fallback. A future human-created screenshot or recording is optional and must not replace live or automated evidence.
