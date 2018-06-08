#!/usr/bin/env python

import pysftp

class Client:
    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd = pwd
        # self.connection
        print(host)

    # def connect_to_server(self):
    #     try:
    #         self.connection = pysftp.Connection()
    #     catch:
    #
