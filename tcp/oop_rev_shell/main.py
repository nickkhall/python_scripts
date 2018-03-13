#!/usr/bin/env python

from src.client import Client
from src.server import Server
import sys

if not len(sys.argv) == 3:
    print('-' * 50)
    print('[-] ERROR: Please enter a host and port number   |')
    print('    USAGE: python ./tcp_server.py 127.0.0.1 4532 |')
    print('-' * 50)
    quit()
else:
    host = sys.argv[1]
    port = int(sys.argv[2])
    if port <= 1024:
        print('You must enter a port number above 1024')
        quit()

class Main():
    def __init__(self, host, port):
        self.server = Server(host, port)
        while self.server.connect_to_client() == True:
            self.server.communicate_with_client()

        # self.server.kill_connection()


if __name__ == '__main__':
    Main(host, port)
