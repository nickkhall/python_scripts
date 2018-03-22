#!/usr/bin/env python

import sys

from src.client import Client

if not len(sys.argv) == 5:
    print('-' * 74)
    print('[-] ERROR: Please enter a host, port number, username and password       |')
    print('[+] USAGE: python ./tcp_server.py 127.0.0.1 4532 johnathan imabitch      |')
    print('-' * 74)
    quit()
else:
    host = sys.argv[1]
    port = int(sys.argv[2])
    user = sys.argv[3]
    pwd = sys.argv[4]
    if port <= 1024:
        print('-' * 50)
        print('[-] ERROR: You must enter a port number above 1024')
        print('-' * 50)
        quit()

print('host: {0}, port: {1}, user: {2}, pwd: {3}'.format(host, port, user, pwd))

def Main():
    client = Client(host, port, user, pwd)

if __name__ == '__main__':
    Main()
