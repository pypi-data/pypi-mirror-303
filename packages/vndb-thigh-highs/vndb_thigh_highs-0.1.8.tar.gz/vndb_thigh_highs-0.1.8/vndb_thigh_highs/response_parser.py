import json
from enum import Enum
from abc import ABCMeta, abstractmethod
from .error import ErrorResponseError, ErrorResponseErrorId, ResponseError

class ResponseKey(Enum):
    OK = 'ok'
    SESSION = 'session'
    ERROR = 'error'
    DBSTATS = 'dbstats'
    RESULTS = 'results'

class ResponseParserFactory:
    def __init__(self):
        self.common_error_ids = [
            ErrorResponseErrorId.PARSE,
            ErrorResponseErrorId.MISSING,
            ErrorResponseErrorId.BAD_ARG,
            ErrorResponseErrorId.NEED_LOGIN,
            ErrorResponseErrorId.THROTTLED,
        ]

    def for_login(self):
        return ResponseParser({
            ResponseKey.OK: NoResponseBodyParser(),
            ResponseKey.SESSION: TextResponseBodyParser(),
            ResponseKey.ERROR: ErrorResponseBodyParser(
                self.common_error_ids + [
                    ErrorResponseErrorId.AUTH,
                    ErrorResponseErrorId.LOGGED_IN,
                ]
            ),
        })

    def for_get(self):
        return ResponseParser({
            ResponseKey.RESULTS: JsonResponseBodyParser(),
            ResponseKey.ERROR: ErrorResponseBodyParser(
                self.common_error_ids + [
                    ErrorResponseErrorId.GET_TYPE,
                    ErrorResponseErrorId.GET_INFO,
                    ErrorResponseErrorId.FILTER,
                ]
            ),
        })

    def for_set(self):
        return ResponseParser({
            ResponseKey.OK: NoResponseBodyParser(),
            ResponseKey.ERROR: ErrorResponseBodyParser(
                self.common_error_ids + [
                    ErrorResponseErrorId.SET_TYPE,
                ]
            ),
        })

    def for_dbstats(self):
        return ResponseParser({
            ResponseKey.DBSTATS: JsonResponseBodyParser(),
            ResponseKey.ERROR: ErrorResponseBodyParser(
                self.common_error_ids
            ),
        })

class ResponseParser:
    def __init__(self, response_body_parsers):
        self.response_body_parsers = response_body_parsers

    def parse(self, response):
        parts = response.split(maxsplit=1)
        response_key = parts[0]
        response_body = parts[1] if len(parts) == 2 else None
        for key, parser in self.response_body_parsers.items():
            if response_key == key.value:
                return parser.parse_response_body(response_body)
        raise ResponseError("Unknown response '%s'" % response)

class ResponseBodyParser(metaclass=ABCMeta):
    @abstractmethod
    def parse_response_body(self, response_body):
        pass

class NoResponseBodyParser(ResponseBodyParser):
    def parse_response_body(self, response_body):
        return

class TextResponseBodyParser(ResponseBodyParser):
    def parse_response_body(self, response_body):
        return response_body

class JsonResponseBodyParser(ResponseBodyParser):
    def parse_response_body(self, response_body):
        return json.loads(response_body)

class ErrorResponseBodyParser(ResponseBodyParser):
    def __init__(self, error_ids):
        self.error_ids = error_ids

    def parse_response_body(self, response_body):
        error_dict = json.loads(response_body)
        error_id = ErrorResponseErrorId.from_id(error_dict['id'])
        raise error_id.create_error(error_dict)

response_parser_factory = ResponseParserFactory()
