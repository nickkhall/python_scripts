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
    print('file:', sys.argv[0], 'host:', host, 'port:', port)

def Main():
    # Create server socket obj
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket obj to port
    server_socket.bind((host, port))

    # Listen for connections
    server_socket.listen(1)

    while True:
        # Let user know we are listening for a connection
        print('Listening for connection on port ' + str(port))

        # Accept connection and data from client
        connection, address = server_socket.accept()

        try:
            print('Connection from: ' + str(address))

            while True:
                conn_data = connection.recv(1024)
                data = conn_data.decode('utf-8')
                if data:
                    print('data: ', data)
                    matched_data = re.match(r'giveme\s(.+\..+)', str(data))
                    if matched_data:
                        filename = matched_data.group(1)
                        print('Filename: ' + str(filename))
                        run_cmd = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE)
                        print('returncode: ', run_cmd.returncode)
                        print('Have {} bytes in the stdout:\n{}'.format(len(run_cmd.stdout), run_cmd.std.decode('utf-8')))

                        # connection.sendall(filename.encode('utf-8'))
                else:
                    print('No more data.')
                    break

        finally:
            # Close the connection
            connection.close()


if __name__ == '__main__':
    Main()
