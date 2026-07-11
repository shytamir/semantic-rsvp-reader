import json
from pathlib import Path

from semantic_rsvp.experiments.parser_assisted_chunking.config import OptimizerConfig


FREEZE_RECORD = Path(
    "evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json"
)


def test_parser_integration_does_not_change_frozen_optimizer_config_hash():
    freeze = json.loads(FREEZE_RECORD.read_text(encoding="utf-8"))

    assert OptimizerConfig().stable_hash() == freeze["scoring_configuration"]["hash"]
