"""a map to json schema types for serialization"""

import uuid
import typing
import types

EMBEDDING_LENGTH_OPEN_AI = 1536

PYTHON_TO_JSON_MAP = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
    list: "array",
    dict: "object",
}


def match_type(f, t):
    """a general way to see if we would match this type allowing for optionality and unions"""
    if f is t:
        return True
    args = getattr(f, "__args__", {}) or ()
    return t in args


def some_default_for_type(f):
    """it may be convenient to create a dummy value for a type
    this is somewhat subjective so we are experimenting with this over time
    this is used for DB use cases primarily so things will be serialized in such a way
    """
    is_nullable = types.NoneType in typing.get_args(f)
    if match_type(f, uuid.UUID):
        return str(uuid.uuid4())
    if match_type(f, str):
        return "" if not is_nullable else None
    if match_type(f, typing.List):
        return [] if not is_nullable else None
    if match_type(f, dict):
        return "{}" if not is_nullable else None
    if match_type(f, int):
        return 0 if not is_nullable else None
    if match_type(f, float):
        return 0.0 if not is_nullable else None
    if match_type(f, bool):
        return False if not is_nullable else None

    return "" if not is_nullable else None
