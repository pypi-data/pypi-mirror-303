from abc import ABCMeta, abstractmethod
from enum import Enum
from .types import STRING
from .operators import Operator, Filter, Expression, VariableExpression
from ..error import TableUsedError

class Comparable(Expression):
    def __init__(self, table, api_name, field_name, field_constructor):
        self.table = table
        self.api_name = api_name
        self.field_name = field_name
        self.field_constructor = TableMeta.adapt_constructor(field_constructor)

    def __repr__(self):
        return "<Column '%s.%s'>" % (self.table.table_name, self.api_name)

    def __str__(self):
        return self.api_name

    def check_table_used(self, table):
        if self.table != table:
            raise TableUsedError(self.table, table)

    def __hash__(self):
        return hash(self._get_key())

    def __eq__(self, other):
        if isinstance(other, Comparable):
            return self._get_key() == other._get_key()
        return Filter.binary(self, Operator.EQ, other)
    def __ne__(self, other):
        if isinstance(other, Comparable):
            return self._get_key() != other._get_key()
        return Filter.binary(self, Operator.NE, other)
    def __le__(self, other):
        if isinstance(other, Comparable):
            return self._get_key() <= other._get_key()
        return Filter.binary(self, Operator.LE, other)
    def __lt__(self, other):
        if isinstance(other, Comparable):
            return self._get_key() < other._get_key()
        return Filter.binary(self, Operator.LT, other)
    def __ge__(self, other):
        if isinstance(other, Comparable):
            return self._get_key() >= other._get_key()
        return Filter.binary(self, Operator.GE, other)
    def __gt__(self, other):
        if isinstance(other, Comparable):
            return self._get_key() > other._get_key()
        return Filter.binary(self, Operator.GT, other)

    def _get_key(self):
        return (
            self.table,
            self.api_name,
            self.field_name,
            self.field_constructor
        )

class _Search(Comparable):
    def __init__(self, table, api_name, field_name):
        super().__init__(table, api_name, field_name, STRING)

class _Column(Comparable):
    def __init__(self, table, api_name, field_name, field_constructor, flag):
        super().__init__(table, api_name, field_name, field_constructor)
        self.flag = flag

    def get_from(self, dict):
        if self.api_name in dict:
            return self.build_from(dict[self.api_name])
        return None

    def build_from(self, value):
        if value is not None:
            return self.field_constructor(value)
        return None

    def set_on(self, obj, value):
        setattr(obj, self.field_name, value)

class ComparableBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.api_name = None

    def with_name(self, name):
        self.api_name = name
        return self

    def build(self, table, name):
        api_name = self.api_name or name
        return self.build_comparable(table, api_name, name)

    @abstractmethod
    def build_comparable(self, table, api_name, name):
        pass

class SearchBuilder(ComparableBuilder):
    def build_comparable(self, table, api_name, name):
        return _Search(table, api_name, name)

class Search(SearchBuilder):
    pass

class ColumnBuilder(ComparableBuilder):
    def __init__(self, field_constructor, flag):
        super().__init__()
        self.field_constructor = field_constructor
        self.flag = flag

    def build_comparable(self, table, api_name, name):
        return _Column(
            table, api_name, name, self.field_constructor, self.flag)

class TableMeta(type):
    def __new__(cls, name, bases, attributes):
        column_builders = cls.extract_builders(attributes, ColumnBuilder)
        search_builders = cls.extract_builders(attributes, SearchBuilder)
        table = super().__new__(cls, name, bases, attributes)
        cls._init_table(table, name, column_builders, search_builders)
        return table

    @staticmethod
    def extract_builders(attributes, builder_class):
        builders = {}
        for key, value in attributes.items():
            if not isinstance(value, builder_class):
                continue
            builders[key] = value
        for key in builders:
            del attributes[key]
        return builders

    @classmethod
    def _init_table(cls, table, name, column_builders, search_builders):
        columns = cls.build_comparables(table, column_builders)
        searchs = cls.build_comparables(table, search_builders)
        cls.add_comparable_attributes(table, columns)
        cls.add_comparable_attributes(table, searchs)
        table.table_name = cls.get_table_name(table, name)
        table.columns = columns
        table.searchs = searchs
        table.flags = cls.get_flags(columns)

    @classmethod
    def build_comparables(cls, table, column_builders):
        return [
            column_builder.build(table, key)
            for key, column_builder in column_builders.items()
        ]

    @classmethod
    def add_comparable_attributes(cls, table, comparables):
        for comparable in comparables:
            setattr(table, comparable.field_name, comparable)

    @staticmethod
    def get_table_name(table, name):
        if hasattr(table, 'table_name'):
            return table.table_name
        return name.lower()

    @staticmethod
    def get_flags(columns):
        flags = set()
        for column in columns:
            if column.flag.value is not None:
                flags.add(column.flag)
        return flags

    @staticmethod
    def adapt_constructor(constructor):
        if isinstance(constructor, TableMeta):
            return constructor.build
        return constructor

    @classmethod
    def unbuild_value(cls, value):
        if value is None:
            return value
        if isinstance(value, (Table, TableFromArray)):
            return value.unbuild()
        if isinstance(value, list):
            return [
                cls.unbuild_value(element)
                for element in value
            ]
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, (bool, int, float, str)):
            return value
        return str(value)

class Table(metaclass=TableMeta):
    @classmethod
    def build(cls, dict):
        instance = cls()
        for column in cls.columns:
            value = column.get_from(dict)
            column.set_on(instance, value)
        return instance

    def unbuild(self):
        dict = {}
        for column in self.columns:
            value = getattr(self, column.field_name)
            value = TableMeta.unbuild_value(value)
            if value is not None:
                dict[column.api_name] = value
        return dict

class TableFromArray(metaclass=TableMeta):
    @classmethod
    def build(cls, list):
        instance = cls()
        for column, element in zip(cls.columns, list):
            value = column.build_from(element)
            column.set_on(instance, value)
        return instance

    def unbuild(self):
        return [
            TableMeta.unbuild_value(getattr(self, column.field_name))
            for column in self.columns
        ]

del Table.table_name
del TableFromArray.table_name
