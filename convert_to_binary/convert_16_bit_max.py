#!/usr/bin/python

import sys
import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('int')
    args = parser.parse_args()
except ValueError as err:
    print('[-] ERROR:\nPlease provide a valid number between 1 and 256 to convert to binary.')
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
        for i in range(1, (int(args.int) + 1)):
            # for cool stuff, remove `+ ' - ' + str(i)` down below B|
            print(convert_to_binary(i) + ' - ' + str(i))
    except ValueError as err:
        print('Error: ' + str(err))

if __name__ == '__main__':
    main()
