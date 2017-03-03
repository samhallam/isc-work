#serial port access session

#!/usr/bin/python2.7

from datetime import datetime
import serial, io

outfile = '/tmp/serial-temperature.tsv'

ser = serial.Serial(
    port ='/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE
)


sio = io.TextIOWrapper(
    io.BufferedRWPair(ser, ser,1),
    encoding='ascii', newline = '\r'
)

#  "8" here is specific to the Papouch thermometer device

with open(outfile,'a') as f: #appends to existing file
    while ser.isOpen():
        datastring = sio.readline()
        #\t is tab; \n is line separator
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')

        f.flush() #included to force the stystem to write to disk
        #print  datetime.utcnow().isoformat(), datastring

ser.close()

# tail- f  '/tmp/serial-temperature.tsv'


import csv

with open('/tmp/serial-temperature.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print row


