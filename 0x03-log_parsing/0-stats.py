#!/usr/bin/python3

import sys
import signal

total_file_size = 0
codes_num = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
itr = 0


def printOut():
    global file_size
    global codes_num
    print(f"File size: {total_file_size}")
    sorted_keys = sorted(codes_num.keys())
    for key in sorted_keys:
        if codes_num[key] > 0:
            print(f"{key}: {codes_num[key]}")


def terminate_handle(signum, frame):
    printOut()
    sys.exit()


signal.signal(signal.SIGINT, terminate_handle)

for line in sys.stdin:
    try:
        if itr == 10:
            printOut()
            itr = 0

        inArr = line.strip().split(" ")
        if len(inArr) != 9:
            continue

        total_file_size += int(inArr[8])
        code = inArr[7]

        if code in codes_num:
            codes_num[code] += 1

        itr += 1
    except(ValueError, IndexError):
        continue
