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
    data = readData(dataIn.strip())
    
    print "**** start ****"
    print "raw Data: " + str(dataIn)
    print "data: " + str(data)
    print "***** end *****"        
    
    #dataOut = str(data).strip()
    
    dataOut = "0,50"
    
    #for item in data:
    #   dataOut = dataOut + str(data)
    
    # write data
    
    print "Data out " + str(dataOut)
    
    serialport.write(dataOut)
    sleep(0.125)
    

serial.close()



