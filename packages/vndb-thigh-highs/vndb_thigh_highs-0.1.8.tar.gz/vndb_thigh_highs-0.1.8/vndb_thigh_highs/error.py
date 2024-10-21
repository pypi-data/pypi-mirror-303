import time
from enum import Enum

class SocketError(Exception):
    pass

class InvalidFlagError(Exception):
    pass

class TableUsedError(Exception):
    def __init__(self, used_table, expected_table):
        super().__init__()
        self.used_table = used_table
        self.expected_table = expected_table

    def __str__(self):
        return "Invalid table usage: %r used while expecting %r" % (
            self.used_table, self.expected_table
        )

class ResponseError(Exception):
    pass

class ErrorResponseError(ResponseError):
    def __init__(self, dict):
        super().__init__()
        self.id = ErrorResponseErrorId.from_id(dict['id'])
        self.msg = dict['msg']

    def __str__(self):
        return "%s: %s" % (self.id, self.msg)

class FieldError(ErrorResponseError):
    def __init__(self, dict):
        super().__init__(dict)
        self.field = dict['field']

    def __str__(self):
        return "%s: %s (field: '%s')" % (self.id, self.msg, self.field)

class ThrottledError(ErrorResponseError):
    def __init__(self, dict):
        super().__init__(dict)
        self.type = dict['type']
        self.minwait_time = dict['minwait']
        self.fullwait_time = dict['fullwait']

    def __str__(self):
        return "%s: %s (type: %s, min: %ss, full: %ss)" % (
            self.id, self.msg, self.type,
            self.minwait_time, self.fullwait_time
        )

    def wait_min(self):
        time.sleep(self.minwait_time)

    def wait_full(self):
        time.sleep(self.fullwait_time)

class GetInfoError(ErrorResponseError):
    def __init__(self, dict):
        super().__init__(dict)
        self.flag = dict['flag']

    def __str__(self):
        return "%s: %s (flag: '%s')" % (self.id, self.msg, self.flag)

class FilterError(FieldError):
    def __init__(self, dict):
        super().__init__(dict)
        self.operator = dict['op']
        self.value = dict['value']

    def __str__(self):
        return "%s: %s (%s %s %s)" % (
            self.id, self.msg, self.field, self.operator, self.value
        )

class ErrorResponseErrorId(Enum):
    def __init__(self, id, error_class):
        super().__init__()
        self.id = id
        self.error_class = error_class

    def __str__(self):
        return self.id

    def create_error(self, dict):
        return self.error_class(dict)

    PARSE = 'parse', ErrorResponseError
    MISSING = 'missing', FieldError
    BAD_ARG = 'badarg', FieldError
    NEED_LOGIN = 'needlogin', ErrorResponseError
    THROTTLED = 'throttled', ThrottledError
    AUTH = 'auth', ErrorResponseError
    LOGGED_IN = 'loggedin', ErrorResponseError
    GET_TYPE = 'gettype', ErrorResponseError
    GET_INFO = 'getinfo', GetInfoError
    FILTER = 'filter', FilterError
    SET_TYPE = 'settype', ErrorResponseError

    @classmethod
    def from_id(cls, id):
        for error_id in cls:
            if error_id.id == id:
                return error_id
        raise ValueError("'%s' is not a valid %s" % (id, str(cls)))
