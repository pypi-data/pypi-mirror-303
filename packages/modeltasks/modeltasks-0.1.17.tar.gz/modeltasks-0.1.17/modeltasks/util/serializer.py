from decimal import Decimal
from typing import Any
from collections import OrderedDict


def normalize_object(o: Any) -> Any:
    """
    Tries to normalize & order objects for serialisation (to achieve same results by a serializer as JSON or Pickle)
    """
    if isinstance(o, dict):
        ordered_dict = OrderedDict(sorted(o.items()))
        for k, v in ordered_dict.items():
            v = normalize_object(v)
            ordered_dict[str(k)] = v
        o = ordered_dict
    elif isinstance(o, (list, tuple, set)):
        o = [normalize_object(el) for el in o]
    else:
        if isinstance(o, int):
            return o
        elif isinstance(o, float):
            return o
        elif isinstance(o, Decimal):
            return o
        o = str(o).strip()
    return o
