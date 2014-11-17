import serial
import string
import re
from time import sleep
from string import whitespace


# Specify your serial port path (/dev/ttyAMA0 is default for Raspberry Pi)
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0)
serialport.flushInput()

def readData(data):
    dataItems = data.split(",")
    
    return dataItems


while True:
    # read data
    
    dataIn = serialport.read(30)
    data = readData(dataIn.strip())
    
    
    steer = 0
    speed = 0
    
    print "**** start ****"
    print data
    print len(data)
    print data[0]
    if len(data)>1:
        print data[1]
    print "***** end *****" 
    
    
    
    
    
    if len(data[0]) >0:
        speed = int(data[0])
     
    
    if len(data) >1:
        steer = int(data[1])

    if (speed > 64) and (speed < 128):
        steer = (steer/3)
        print "between 64 & 127"
    
    if speed >= 128:
        steer = (steer/4)
        print "greater than 128"

    if steer == 0:
        left = speed
        right = speed
    
    if steer > 0:
        left = speed - steer
        right = speed + steer

    if steer < 0:   
        left = speed + steer
        right = speed - steer
 
    print "left: " + str(left) + " right: " + str(right)
    
    
    dataOut = str(left) + "," + str(right) +"\n"
    
    
    
    print "Data out " + "|" + dataOut + "|"
    
    serialport.write(dataOut)
    sleep(0.125)
    
    

serial.close()



