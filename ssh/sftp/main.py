#!/usr/bin/env python

import sys

from src.client import Client

if not len(sys.argv) == 4:
    print('-' * 74)
    print('[-] ERROR: Please enter a host, username and password       |')
    print('[+] USAGE: python ./tcp_server.py 127.0.0.1 johnathan imabitch      |')
    print('-' * 74)
    quit()
else:
    host = sys.argv[1]
    user = sys.argv[2]
    pwd = sys.argv[3]

def Main():
    client = Client(host, user, pwd)
    # client.connect_to_server()

if __name__ == '__main__':
    Main()
