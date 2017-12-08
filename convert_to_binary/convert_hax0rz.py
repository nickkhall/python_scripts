#!/usr/bin/python

# WARNING: I AM NOT RESPONSIBLE FOR ANY DAMAGES CAUSED BY RUNNING THIS SCRIPT

import sys
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('int')
    args = parser.parse_args()
except ValueError as err:
    print('[-] ERROR:\nPlease provide a valid number between 1 and 256 to convert to binary.')
    print('Usage: python 16_bit_binary.py 1337')
    quit()


def convert_to_binary(num):
    bin_arr = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    res_num = num
    result = ''

    for bin in bin_arr:
        if res_num / bin >= 1 and res_num / bin < 2:
            result += '1'
            res_num = res_num - bin
        else:
            result += '0'

    return result

def main():
    counter = 0

    # change '50' below to change how long the script runs for
    while counter < 50:
        try:
            for i in range(1, (int(args.int) + 1)):
                print(convert_to_binary(i))
            counter += 1
        except ValueError as err:
            print('Error: ' + str(err))

if __name__ == '__main__':
    main()
