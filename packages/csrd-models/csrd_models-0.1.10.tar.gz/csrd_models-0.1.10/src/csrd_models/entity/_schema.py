from typing import Any, Union, get_origin, get_args
from csrd_utils.string_utils import to_camel, to_title


def get_name(obj: Any) -> str:
    return obj.__name__


def _get_properties(obj: Any) -> dict:
    return {k: obj.__dict__[k] for k in obj.__dict__ if not k.startswith('_')}


def map_type(type_: Any):
    if type(type_) is not str:
        type_ = get_name(type_)

    return {
        "str": "string",
        "int": "integer",
        "float": "number",
        "bool": "boolean",
        "List": "array",
        "NoneType": 'null'
    }[type_]


def is_union(value: Any) -> bool:
    return get_origin(get_args(value)[0]) == Union


def handle_union(key, name, value):
    return {
        # 'title': to_title(key),
        'items': {'anyOf': [{"type": map_type(x)} for x in get_args(get_args(value)[0])]}, 'type': map_type(name)}


def handle_optional(key, name, value, props):
    return {
        'type': map_type([x for x in get_args(value) if x is not type(None)][0]),
        'default': props.get(key, None),
        'title': to_title(key),
        'required': False
    }


def build_type(key, value: Any, props = None):
    name = get_name(value)

    if name in ('str', 'int', 'float', 'bool'):
        return {
            'title': to_title(key),
            'type': map_type(name)
        }

    if name in ("List",):
        args = get_args(value)[0]
        if is_union(value):
            return handle_union(key, name, value)
        else:
            return {
                'title': to_title(key),
                'type': map_type(name),
                'items': {'type': map_type(args)}
            }

    if name in ("Optional",):
        return handle_optional(key, name, value, props)

    # this is probably missing some cases
    return {'$ref': f'#/definitions/{value.__name__}'}


def _build_properties(value: Any):
    props = getattr(value, '__properties__', None)
    annno = getattr(value, '__annotations__', None)
    return { to_camel(key): build_type(key, annno[key], props) for key in annno }


def _build_schema(cls: Any):
    return {
            "properties": _build_properties(cls),
            "title": get_name(cls),
            "type": "object"
    }


class _Schema:
    def __init__(self, __class__):
        self._set_schema(__class__)

    @classmethod
    def _set_schema(cls, __class__):
        setattr(cls, '__annotations__', __class__.__annotations__)
        setattr(cls, '__name__', __class__.__name__)
        setattr(cls, '__properties__', _get_properties(__class__))

    @classmethod
    def dump_schema(cls):
        return _build_schema(cls)
