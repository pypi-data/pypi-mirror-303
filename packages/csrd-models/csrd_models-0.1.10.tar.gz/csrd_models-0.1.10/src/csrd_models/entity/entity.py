from ._schema import _Schema

from csrd_utils.string_utils import to_camel


class Entity:
    _schema = _Schema

    def __init__(self, /, **data):
        self._schema = _Schema(self.__class__)
        for key, value in data.items():
            self.__dict__[key] = value

    @property
    def name(self):
        return self.__name__

    @classmethod
    def schema(cls):
        cls._schema._set_schema(cls)
        return cls._schema.dump_schema()

    def json(self):
        return {to_camel(k): self.__dict__[k] for k in self.__dict__ if not k.startswith('_')}
