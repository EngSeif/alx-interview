#!/usr/bin/python3
"""
!a script that reads stdin line by line and computes metrics:

*Input format:
*   <IP Address> - <date> "GET/projects/260HTTP/1.1" <status code> <file size>
*   (if the format is not this one, the line must be skipped)

* After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
    *Total file size: File size: <total size>
        *where <total size> is the sum of all previous
        <file size> (see input format above)
    *Number of lines by status code:
        *possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    *if a status code doesn’t appear or is not an integer,
    don’t print anything for this status code
    *format: <status code>: <number>
    *status codes should be printed in ascending order
"""
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
