#!/usr/bin/env python
# Simple CLI arduino serial debug read/write
# (c)2010, Guyzmo <guyzmo{at}hackable-devices.org>

import sys, serial, fcntl, os

fd = sys.stdin.fileno()
fl = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

try:
    ser = serial.Serial(sys.argv[1], baudrate = 9600)
except:
    print("Please use a tty port available. Like /dev/ttyUSB0")
    exit(1)

c = None
while True:
    sys.stdout.write(ser.read(1))
    sys.stdout.flush()
    try: 
        c = sys.stdin.read(1)
        ser.write(c)
        ser.flush()
        c=None
    except: 
        continue
