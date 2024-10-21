from datetime import date
from . import table as t

def TIMESTAMP(timestamp):
    if isinstance(timestamp, str):
        return date_from_iso_format(timestamp)
    return date.fromtimestamp(timestamp)

def date_from_iso_format(date_string):
    return date.fromisoformat(date_string)

_identity = lambda x: x

BOOLEAN = _identity
INTEGER = _identity
FLOAT = _identity
STRING = _identity
DATE = _identity
ISO_DATE = date_from_iso_format

class JoinedStrings:
    def __init__(self, separator="\n"):
        self.separator = separator

    def __call__(self, string):
        return string.split(self.separator)

class ListOf:
    def __init__(self, field_constructor):
        self.field_constructor = t.TableMeta.adapt_constructor(field_constructor)

    def __call__(self, objs):
        return [
            self.field_constructor(obj) if obj is not None else None
            for obj in objs
        ]

class FirstElementOf:
    def __init__(self, iterable_constructor):
        self.iterable_constructor = iterable_constructor

    def __call__(self, objs):
        return self.iterable_constructor(objs)[0]
