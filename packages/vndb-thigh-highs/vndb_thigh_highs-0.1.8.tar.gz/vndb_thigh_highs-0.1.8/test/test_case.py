import os
import json
import logging
import unittest
from context import abspath
from vndb_thigh_highs import VNDB, Config
from vndb_thigh_highs.get_command import GetCommandFactory
from vndb_thigh_highs.set_command import SetCommandFactory
from mock_socket import MockSocket, ResponseTestMockSocket
from response_factory import ResponseFactory

LOGIN_PATH = abspath('../data/login.json')

class TestCase(unittest.TestCase):
    pass

class CommandTest(TestCase):
    def setUp(self):
        self.config = Config()
        self.config.client_version = "0.x-test"
        self.config.set_log_level(logging.ERROR)
        self.socket = MockSocket(self.config.logger)
        self.get_factory = GetCommandFactory(self.socket)
        self.set_factory = SetCommandFactory(self.socket)

class ResponseTest(TestCase):
    use_mock_socket = True

    def setUp(self):
        self.config = Config()
        self.config.set_log_level(logging.ERROR)
        self.socket = ResponseTestMockSocket(self.config.logger)
        if self.use_mock_socket:
            self.vndb = VNDB(config=self.config, socket=self.socket)
        else:
            self.vndb = VNDB(config=self.config)
        self.response_factory = ResponseFactory()

    def tearDown(self):
        self.vndb.disconnect()

@unittest.skipUnless(
    ResponseTest.use_mock_socket or os.path.isfile(LOGIN_PATH),
    "Missing data")
class ResponseTestWithPassword(ResponseTest):
    def setUp(self):
        super().setUp()
        with open(LOGIN_PATH) as login_file:
            data = json.load(login_file)
        if data['password'] is None and not ResponseTest.use_mock_socket:
            raise unittest.SkipTest("Password not set")
        self.username = data['username']
        self.password = data['password']

class LoggedInResponseTest(ResponseTestWithPassword):
    def setUp(self):
        super().setUp()
        self.config.set_login(self.username, self.password)
