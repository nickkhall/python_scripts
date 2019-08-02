#!usr/bin/python
#encoding=utf8

import socket
import sys
import hashlib

args = sys.argv
passwords_found = 0

try:
    hash = args[1]
    file = args[2]
except:
    print('You must enter in a MD5 hash and a word list.\n')
    print('Usage: python ./md5.py 34234234b23b4asdfj23j234j2 /usr/share/wordlists/my_word_list.txt')
    quit()

with open(file, 'r') as file:
    print('Checking for matches...\n' + '-' * 35)

    for password in file:
        try:
            md5_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
            
            if md5_hash == hash:
                print('-' * 35 + '\n[+] PASSWORD FOUND: ' + password + '-' * 35)
                passwords_found += 1
                break
        except:
            print('[-] Warning: Unknown character found: ' + password)
            pass

if passwords_found < 1:
    print('No matches found')
# a4f839fdf23e2558d0bde3e14da5f7b6
