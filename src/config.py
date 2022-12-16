"""BMG's config file reader"""

from typing import Any
from schema import Schema, Optional
import yaml

SCHEMA = Schema({
    Optional("config"): {
        "prefix": str,
    },
    "models" : [{
        "name": str,
        "attributes" : [{
            "name": str,
            "type": str,
            Optional("primary"): bool,
            Optional("list"): bool,
        }],
    }]
})

DEFAULTS = {
    "config": {
        "prefix": "BMG"
    },
    "models": []
}

def load(fn:str):
    """Load YAML from filename and validates"""
    with open(fn, 'r') as f:
        config = yaml.safe_load(f)
        SCHEMA.validate(config)
    return DEFAULTS | config
