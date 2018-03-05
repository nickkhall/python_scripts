import socket
import sys

def Main():
    if not len(sys.argv) >= 3:
        print('Please enter a host and port number')
        print('USAGE: python ./tcp_client.py 127.0.0.1 444')
        quit()
    else:
        host = sys.argv[1]
        port = sys.argv[2]
        print('1st:', sys.argv[0], '2nd:', host, '3rd:', port)

if __name__ == '__main__':
    Main()
