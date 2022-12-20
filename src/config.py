"""BMG's config file reader"""

from typing import Any
from schema import Schema, Optional
import yaml
from .utils.structures import merge

SCHEMA = Schema(
    {
        Optional("settings"): {
            "prefix": str,
            Optional("includes"): [str],
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
                        Optional("containment"): bool,
                    }
                ],
            }
        ],
    }
)

DEFAULTS = {"settings": {"prefix": "BL", "includes": []}, "models": []}


def load(fn: str):
    """Loads YAML from filename then validates against config.SCHEMA"""
    with open(fn, "r") as f:
        config = DEFAULTS.copy()
        merge(yaml.safe_load(f), config)
        SCHEMA.validate(config), config
    return config
