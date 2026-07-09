from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from semantic_rsvp.timing.schedule import schedule_text  # noqa: E402


def scheduled_chunk_to_dict(scheduled_chunk):
    chunk = scheduled_chunk.chunk
    return {
        "index": scheduled_chunk.index,
        "sentence_index": scheduled_chunk.sentence_index,
        "text": chunk.text,
        "content_word_count": chunk.content_word_count,
        "char_length": chunk.char_length,
        "syntactic_hint": chunk.syntactic_hint,
        "duration_ms": scheduled_chunk.duration_ms,
    }


def build_payload(text: str) -> dict:
    schedule = [scheduled_chunk_to_dict(item) for item in schedule_text(text)]
    return {
        "schedule": schedule,
        "chunk_count": len(schedule),
    }


def format_readable(payload: dict) -> str:
    if not payload["schedule"]:
        return "No chunks generated."

    lines = [f"{payload['chunk_count']} chunk(s) generated.", ""]
    for item in payload["schedule"]:
        lines.append(
            "{index:>3}. [{duration_ms:>4} ms] s{sentence_index}: {text}".format(
                **item
            )
        )
    return "\n".join(lines)


def read_input(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Semantic RSVP schedule from a text file or stdin."
    )
    parser.add_argument("path", nargs="?", help="Plain text file to schedule.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the schedule as JSON instead of readable text.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    payload = build_payload(read_input(args.path))
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(format_readable(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
