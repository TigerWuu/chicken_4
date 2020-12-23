#!/usr/bin/env python

import serial

COM_PORT = '/dev/ttyACM0'  
BAUD_RATES = 9600

ser = serial.Serial(COM_PORT, BAUD_RATES)


cmdd="000,000,0,0000000000".encode()
ser.write(cmdd)
