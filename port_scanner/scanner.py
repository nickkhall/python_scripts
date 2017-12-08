#!usr/bin/python

import socket
import sys

try:
    passed_host = sys.argv[1]
    passed_ports = sys.argv[2]
    if len(passed_ports.split(',')) < 2:
        quit()
except:
    print('You need to pass in a host and port')
    print('\nUsage: python scanner.py 192.168.0.1 0,1024')
    quit()

def scan_ports(host, port_start, port_end):
    for port in range(port_start, (port_end + 1)):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = socket.gethostbyname(host.strip())

            sock.connect((ip, int(port)))
            sock.send('scanning \n')

            data = sock.recv(1024)

            if data:
                print('[+] Port ' + str(port) + 'is open' + '\nData recv: ' + data)
                socket.close()

        except ValueError as error:
            print('Error: ' + error)
            pass

def main():
    global passed_host
    global passed_ports

    try:
        scan_ports(passed_host, int(passed_ports.split(',')[0]), int(passed_ports.split(',')[1]))
    except ValueError as e:
        print('Error: ' + str(e))
        quit()

if __name__ == '__main__':
    main()
