import logging
from .login_command import LoginConfig

class Config:
    def __init__(self):
        self.client_name = "VNDB Thigh-highs"
        self.client_version = "0.1.8"
        self.protocol_version = 1
        self.log_level = logging.WARNING
        self.logger = self.create_logger(self.client_name)
        self.login = LoginConfig(self)
        self.cache = None

    def create_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(self.log_level)
        if not logger.handlers:
            handler = logging.StreamHandler()
            logger.addHandler(handler)
        return logger

    def set_log_level(self, log_level):
        self.log_level = log_level
        self.logger.setLevel(self.log_level)

    def set_login(self, username, password):
        self.login.set_login(username, password)

    def set_create_session(self, create_session):
        self.login.set_create_session(create_session)

    def set_session(self, username, session_token):
        self.login.set_session(username, session_token)
