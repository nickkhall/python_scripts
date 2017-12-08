#!/usr/bin/python

# python packet sniffer
import socket
import sys
from struct import *

# convert str of a 6 char length of ethernet addr into a - separated HEX str
def eth_addr(addr):
    b = "%.2x: %.2x: %.2x: %.2x: %.2x: %.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b

# create a AF_PACKET type for raw socket
try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except socket.error, msg:
    print('Socket could not be created. Error code: ' + str(msg[0]) + '\n' + msg[1])
    sys.exit()

# receive a packet
while True:
    packet = s.recvfrom(65565)
    # packet str from tuple
    packet = packet[0]
    # parse ethernet header
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sh', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print('[ + ] Destination MAC: ' + eth_addr(packet[0:6])) + '\n[ ++ ] Source MAC: ' + eth_addr(packet[6:12]) + '\nProtocol: ' + str(eth_protocol)
