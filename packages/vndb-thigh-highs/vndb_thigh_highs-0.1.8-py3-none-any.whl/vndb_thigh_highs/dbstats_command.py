from .command import Command
from .response_parser import response_parser_factory
from .models.dbstats import DBStats

class DBStatsCommand(Command):
    def __init__(self, socket):
        super().__init__(socket, response_parser_factory.for_dbstats())

    def get(self):
        command = self.make_command()
        response_dict = self.communicate(command)
        return self.parse_response_dict(response_dict)

    def make_command(self):
        return "dbstats"

    def parse_response_dict(self, response_dict):
        return DBStats.build(response_dict)
