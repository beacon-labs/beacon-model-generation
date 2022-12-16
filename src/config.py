"""BMG's config file reader"""

from typing import Any
from schema import Schema, Optional
import yaml

SCHEMA = Schema(
    {
        Optional("config"): {
            "prefix": str,
        },
        "models": [
            {
                "name": str,
                "description": str,
                "attributes": [
                    {
                        "name": str,
                        "type": str,
                        Optional("primary"): bool,
                        Optional("list"): bool,
                    }
                ],
            }
        ],
    }
)

DEFAULTS = {"config": {"prefix": "BMG"}, "models": []}


def load(fn: str):
    """Loads YAML from filename then validates against config.SCHEMA"""
    with open(fn, "r") as f:
        config = DEFAULTS | yaml.safe_load(f)
        SCHEMA.validate(config)
    return config
