#!/usr/bin/env python

import paramiko

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ssh = paramiko.SSHClient()

        print('self.ssh: ', self.ssh)
