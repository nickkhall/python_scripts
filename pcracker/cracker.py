#!usr/bin/python
#encoding=utf8

import socket
import sys
import hashlib

args = sys.argv

try:
    hash = args[1]
except:
    print('You must enter in a MD5 hash')
    quit()

with open('path/to/dictionary/file', 'r') as file:
    print('Checking for matches...\n' + '-' * 35)

    for password in file:
        try:
            md5_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

            if md5_hash == hash:
                print('-' * 35 + '\n[+] PASSWORD FOUND: ' + password + '-' * 35)
                break
        except:
            print('[-] Warning: Unknown character found: ' + password)
            pass

# a4f839fdf23e2558d0bde3e14da5f7b6
