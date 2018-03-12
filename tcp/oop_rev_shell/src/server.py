#!/usr/bin/env python

import socket as sock
import sys

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
        self.address = None
        self.cmd = None

        self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print('Server is listening on port ' + str(self.port))


    def connect_to_client(self):
        self.connection, self.address = self.socket.accept()
        if self.connection and self.address:
            print('Successfully connected to ' + str(self.address[0]))

    def communicate_with_client(self):
        while True:
            self.cmd = input('> ')

            if cmd == 'quit':
                self.kill_connection()
                sys.exit()

            if len(str.encode(self.cmd)) > 0:
                self.connection.send(str.encode(self.cmd))
                print(str(self.connection.recv(65535), "utf-8"), end="")

    def kill_connection(self):
        if self.connection:
            self.connection.close()
        self.socket.close()
