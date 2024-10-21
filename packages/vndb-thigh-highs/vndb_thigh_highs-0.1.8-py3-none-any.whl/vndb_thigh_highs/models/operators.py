import json
from abc import ABCMeta, abstractmethod
from enum import Enum

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def check_table_used(self, table):
        pass

class VariableExpression(Expression):
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return json.dumps(self.variable)

    def check_table_used(self, table):
        pass

class Filter(Expression):
    def __init__(self, operator, expressions):
        self.operator = operator
        self.expressions = [
            expression
            if isinstance(expression, Expression) else
            VariableExpression(expression)
            for expression in expressions
        ]

    @classmethod
    def binary(cls, left, operator, right):
        return cls(operator, [left, right])

    def __str__(self):
        operator = " %s " % self.operator
        strs = []
        for expression in self.expressions:
            string = str(expression)
            if (isinstance(expression, Filter)
                and expression.operator.need_paren()):
                string = "(%s)" % string
            strs.append(string)
        return operator.join(strs)

    def check_table_used(self, table):
        for expression in self.expressions:
            expression.check_table_used(table)

class Operator(Enum):
    EQ = '='
    NE = '!='
    LE = '<='
    LT = '<'
    GE = '>='
    GT = '>'

    SEARCH = '~'
    AND = 'and'
    OR = 'or'

    def __str__(self):
        return self.value

    def join(self, iterable):
        return self.value.join(iterable)

    def need_paren(self):
        return self == Operator.AND or self == Operator.OR

def and_(*args):
    return Filter(Operator.AND, args)

def or_(*args):
    return Filter(Operator.OR, args)

def search(left, right):
    return Filter.binary(left, Operator.SEARCH, right)
