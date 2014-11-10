import serial
import string
from time import sleep


# Specify your serial port path (/dev/ttyAMA0 is default for Raspberry Pi)
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0)

def readData(data):
    dataItems = data.split(",")
    
    return dataItems


while True:
    # read data
    
    dataIn = serialport.read(30)
    p = readData(dataIn.strip())
    
    print "**** start ****"
    print p
    print "***** end *****"        
    
    # write data
    
    dataOut=dataIn
    
    serialport.write(dataOut)
    sleep(0.125)
    

serial.close()



