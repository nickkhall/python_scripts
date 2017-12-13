#!usr/bin/python

import sys
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('int')
    args = parser.parse_args()
except ValueError as err:
    print('[-] ERROR:\nPlease provide a valid number between 1 and 65,535 to convert to binary.')
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
    try:
        if (int(args.int) + 1) > -1:
            return_number = convert_to_binary(int(args.int))
            print('Binary: ' + return_number)
        else:
            print('[-] ERROR:\nPlease provide a valid number between 1 and 65,535 to convert to binary. fucking idiot')
            print('Usage: python 16_bit_binary.py 1337')
    except ValueError as err:
        print('Error: ' + str(err))

if __name__ == '__main__':
    main()
