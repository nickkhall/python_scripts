#!/usr/bin/env python

import pysftp

class Client:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd

    # def connect_to_server():
    #     with pysftp.Connection(host, username=)
