#!/usr/bin/env python

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        print('Client __init__ ran')
