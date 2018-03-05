import socket
import sys

if not len(sys.argv) == 3:
    print('Please enter a host and port number')
    print('USAGE: python ./tcp_server.py 127.0.0.1 444')
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

    # Let user know we are listening for a connection
    print('Listening for connection on port ' + str(port))

    # Accept connection and data from client
    connection, address = server_socket.accept()


if __name__ == '__main__':
    Main()
