from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from semantic_rsvp.application.document_ingestion import (
    DocumentIngestionError,
    ingest_local_document,
)
from semantic_rsvp.application.schedule_service import ScheduleService


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    try:
        document = ingest_local_document(
            args.path.read_bytes(),
            source_name=args.path.name,
        )
        schedule = ScheduleService().generate(document.text)
    except (DocumentIngestionError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(
        json.dumps(
            {
                "document_id": document.document_id,
                "source_type": document.source_type,
                "text": document.text,
                "structure": [asdict(item) for item in document.structure],
                "provenance": dict(document.provenance),
                "reader_chunks": [item.chunk.text for item in schedule.schedule],
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
