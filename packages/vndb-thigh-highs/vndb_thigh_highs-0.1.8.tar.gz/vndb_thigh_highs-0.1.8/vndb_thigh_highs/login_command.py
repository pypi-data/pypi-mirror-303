import json
from .command import ConnectCommand
from .response_parser import response_parser_factory

class LoginConfig:
    def __init__(self, config):
        self.config = config
        self.username = None
        self.password = None
        self.session_token = None
        self.create_session = None

    def set_login(self, username, password):
        self.username = username
        self.password = password

    def set_create_session(self, create_session):
        self.create_session = create_session

    def set_session(self, username, session_token):
        self.username = username
        self.session_token = session_token

    def make_login_dict(self):
        args = {
            'protocol': self.config.protocol_version,
            'client': self.config.client_name,
            'clientver': self.config.client_version,
        }
        if self.username is not None:
            args['username'] = self.username
        if self.password is not None:
            args['password'] = self.password
        if self.create_session is not None:
            args['createsession'] = self.create_session
        if self.session_token is not None:
            args['sessiontoken'] = self.session_token
        return args

class LoginCommand(ConnectCommand):
    def __init__(self, socket, login_config):
        super().__init__(socket, response_parser_factory.for_login())
        self.config = login_config
        self.logged_in = False

    def is_logged_in(self):
        return self.logged_in

    def login(self):
        if not self.is_connected():
            self.connect()
        command = self.make_login_command()
        result = self.communicate(command)
        self.logged_in = True
        return result

    def logout(self):
        command = self.make_logout_command()
        self.communicate(command)
        self.disconnect()

    def disconnect(self):
        self.logged_in = False
        super().disconnect()

    def make_login_command(self):
        login_dict = self.config.make_login_dict()
        command = "login %s" % json.dumps(login_dict)
        return command

    def make_logout_command(self):
        return "logout"
