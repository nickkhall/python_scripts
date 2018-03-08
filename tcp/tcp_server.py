#!/usr/bin/env python

import socket
import sys
import re
import subprocess

if not len(sys.argv) == 3:
    print('Please enter a host and port number')
    print('USAGE: python ./tcp_server.py 127.0.0.1 4532')
    quit()
else:
    host = sys.argv[1]
    port = int(sys.argv[2])
    if port <= 1024:
        print('You must enter a port number above 1024')
        quit()

def Main():
    # Create server socket obj
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket obj to port
    server_socket.bind((host, port))

    # Listen for connections
    server_socket.listen(1)

    # Let user know we are listening for a connection
    print('Listening for connection on port ' + str(port))

    # Accept connection and data from client
    connection, address = server_socket.accept()

    if connection and address:
        print('Successfully connected to', str(address[0]))

    while True:
        cmd = input()
        if cmd == 'quit':
            connection.close()
            client_socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            print(str(connection.recv(1024), "utf-8"), end="")

    connection.close()
    server_socket.close()
    sys.exit()


if __name__ == '__main__':
    Main()
