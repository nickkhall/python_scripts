#!/usr/bin/env python
from pymsgbox import *
import time
import datetime
import re

now = datetime.datetime.now()
parseddate = re.match('([0-9]+)-([0-9]+)-([0-9]+)\s([0-9]+):([0-9]+):([0-9])+', str(now))

def get_time(line):
    if parseddate:
        hour = int(parseddate.group(4))
        min = int(parseddate.group(5))
        dictionary = [line]
        if dictionary:
            for l in dictionary:
                recordedtime = re.match('(.+)\s([0-9]+)\s([0-9]+):([0-9]+):([0-9]+)', str(l))
                loghour = int(recordedtime.group(3))
                logmin = int(recordedtime.group(4))
                if hour >= loghour:
                    if hour == loghour:
                        if min >= logmin:
                            showalert()
                    if hour > loghour:
                        if min + logmin >= min + logmin - 15:
                            showalert(l)

def check():
    with open('/var/log/syslog', 'r') as file:
        for line in file:
            if 'Started Session' in line:
                get_time(line)

def showalert(line):
    alert(title='POSSIBLE INTRUSION:', text=line, button='fuck')
check()
