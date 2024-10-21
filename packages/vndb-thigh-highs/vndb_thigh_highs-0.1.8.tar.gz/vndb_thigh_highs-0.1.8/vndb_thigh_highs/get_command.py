import json
from collections import UserList
from .command import TableCommand
from .response_parser import response_parser_factory
from .error import TableUsedError, InvalidFlagError
from .models import (
    Flag, Comparable, Operator, Filter,
    VN, Release, Producer, Character, Staff, User, UserLabel, UserVN, Quote
)

class GetCommandOption:
    def __init__(self, api_name, name=None, *, transform=None):
        self.api_name = api_name
        self.name = name or api_name
        self.transform = transform or (lambda x: x)

    def init_attribute(self, obj):
        setattr(obj, self.name, None)

    def add_value_to_dict(self, obj, options_dict):
        value = getattr(obj, self.name)
        if value is not None:
            options_dict[self.api_name] = self.transform(value)

class GetCommandOptions:
    send_options = (
        GetCommandOption('page'),
        GetCommandOption('results', 'max_results'),
        GetCommandOption('sort', transform=str),
        GetCommandOption('reverse'),
    )

    def __init__(self):
        self.limit = float("inf")
        for send_option in self.send_options:
            send_option.init_attribute(self)

    def make_options_dict(self):
        options_dict = {}
        for send_option in self.send_options:
            send_option.add_value_to_dict(self, options_dict)
        return options_dict

    def start_pagination(self):
        self.page = 1

    def next_page(self):
        self.page += 1

    def check_table_used(self, table):
        self.check_sort_table_used(table)

    def check_sort_table_used(self, table):
        if (self.sort is not None
            and isinstance(self.sort, Comparable)
            and self.sort.table != table):
            raise TableUsedError(self.sort, table)

class GetCommandResult(UserList):
    def __init__(self, items, more):
        super().__init__(items)
        self.more = more

    def extend(self, result):
        super().extend(result)
        self.more = self.more and result.more

    def has_reached_limit(self, limit):
        return not self.more or len(self) >= limit

    @classmethod
    def empty(cls):
        return cls([], True)

class GetCommand(TableCommand):
    def __init__(self, socket, table):
        super().__init__(socket, response_parser_factory.for_get(), table)

    def get(self, filter_, flags=None, options=None):
        command = self.make_command(filter_, flags, options)
        response_dict = self.communicate(command)
        return self.parse_response_dict(response_dict)

    def get_all(self, filter_, flags=None, options=None):
        options = self.analyse_options(options)
        options.start_pagination()
        main_result = GetCommandResult.empty()
        while True:
            result = self.get(filter_, flags, options)
            main_result.extend(result)
            if main_result.has_reached_limit(options.limit):
                break
            options.next_page()
        return main_result

    def make_command(self, filter_, flags=None, options=None):
        filter_ = self.analyse_filter(filter_)
        flags = self.analyse_flags(flags)
        options = self.analyse_options(options)
        options_dict = options.make_options_dict()
        command = "get %s %s (%s) %s" % (
            self.get_name(),
            ",".join([str(flag) for flag in flags]),
            str(filter_),
            json.dumps(options_dict) if options_dict else "",
        )
        return command.rstrip()

    def analyse_filter(self, filter_):
        if isinstance(filter_, Filter):
            filter_.check_table_used(self.table)
        return filter_

    def analyse_flags(self, flags):
        if flags is None:
            flags = self.table.flags
        elif isinstance(flags, Flag):
            flags = [flags]
        error_flags = set(flags) - self.table.flags
        if error_flags:
            raise InvalidFlagError("Invalid flag usage in '%s'" % str(error_flags))
        return sorted(flags)

    def analyse_options(self, options):
        if options is None:
            return GetCommandOptions()
        options.check_table_used(self.table)
        return options

    def parse_response_dict(self, response_dict):
        items = [
            self.table.build(item)
            for item in response_dict['items']
        ]
        return GetCommandResult(items, response_dict['more'])

class GetCommandWithCache(GetCommand):
    def __init__(self, socket, table, cache):
        super().__init__(socket, table)
        self.cache = cache

    def communicate(self, command):
        if command in self.cache:
            return self.cache.get(command)
        data = super().communicate(command)
        self.cache.add(command, data)
        return data

class GetCommandFactory:
    def __init__(self, socket, cache=None):
        self.socket = socket
        self.cache = cache
        self.tables = [
            VN,
            Release,
            Producer,
            Character,
            Staff,
            User,
            UserLabel,
            UserVN,
            Quote,
        ]

    def all_commands(self):
        return [
            self.create_command(table)
            for table in self.tables
        ]

    def create_command(self, table):
        if self.cache is None:
            return GetCommand(self.socket, table)
        return GetCommandWithCache(self.socket, table, self.cache)
