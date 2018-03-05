import socket
import sys

if not len(sys.argv) == 3:
    print('Please enter a host and port number')
    print('USAGE: python ./tcp_client.py 127.0.0.1 4532')
    quit()
else:
    host = sys.argv[1]
    port = int(sys.argv[2])
    if port <= 1024:
        print('You must enter a port number above 1024')
        quit()
    print('file:', sys.argv[0], 'host:', host, 'port:', port)

def Main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        msg = input('WTF BRO THIS IS FRUSTRATING UGHH')
        client_socket.sendall(msg)

        data = client_socket.recv(1024)
        formatted_data = data.format(data)
        print(str(data))

    client_socket.close()
    quit()

if __name__ == '__main__':
    Main()
