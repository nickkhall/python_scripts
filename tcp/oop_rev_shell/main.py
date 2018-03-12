#!/usr/bin/env python

from src.client import Client
from src.server import Server

def Main():
    main_client = Client('127.0.0.1', 3333)
    print('main_client: ', main_client)
    main_server = Server('127.0.0.1', 3333)
    print('main_server: ', main_server)

if __name__ == '__main__':
    Main()
