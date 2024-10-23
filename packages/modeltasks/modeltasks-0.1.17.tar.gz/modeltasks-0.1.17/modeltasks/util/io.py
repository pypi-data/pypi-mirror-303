import json
import pickle
from typing import Any
from pathlib import Path
from modeltasks.config import SETTINGS
from modeltasks.util.serializer import normalize_object


def serialize(result: Path, value: Any = None):
    try:
        if value is not None:
            simplified_value = normalize_object(value)
            with open(result, 'w') as r:
                json.dump(simplified_value, r, sort_keys=True, indent=4)
    except json.JSONDecodeError:
        if SETTINGS['allow_pickle']:
            try:
                pickle.dump(value, r, 5)
            except pickle.UnpicklingError:
                raise ValueError('Unsupported result value (Cannot serialize)')
        else:
            raise ValueError('Unsupported result value (Cannot serialize)')


def deserialize(result: Path):
    try:
        with open(result, 'r') as r:
            return json.load(r)
    except json.JSONDecodeError:
        if SETTINGS['allow_pickle']:
            try:
                return pickle.load(r)
            except pickle.UnpicklingError:
                raise ValueError('Invalid result file (Cannot deserialize)')
        else:
            raise ValueError('Unsupported result value (Cannot deserialize)')
