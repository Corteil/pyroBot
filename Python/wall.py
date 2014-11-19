import serial
import string
import re
from time import sleep
from string import whitespace
import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15


# Specify your serial port path (/dev/ttyAMA0 is default for Raspberry Pi)
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0)
serialport.flushInput()

steer = 0
speed = 0
left = 0
right = 0

def readData(data):
    dataItems = data.split(",")
    
    return dataItems

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

def howFar():

    ADS1015 = 0x00  # 12-bit ADC
    ADS1115 = 0x01	# 16-bit ADC

# Select the gain
# gain = 6144  # +/- 6.144V
    gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Select the sample rate
# sps = 8    # 8 samples per second
# sps = 16   # 16 samples per second
# sps = 32   # 32 samples per second
# sps = 64   # 64 samples per second
# sps = 128  # 128 samples per second
    sps = 250  # 250 samples per second
# sps = 475  # 475 samples per second
# sps = 860  # 860 samples per second

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
    adc = ADS1x15(ic=ADS1115)

# Read channel 0 in single-ended mode using the settings above
    volts = adc.readADCSingleEnded(0, gain, sps) / 1000

# To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
# volts = adc.readADCSingleEnded(3, 1024, 860)

    print "%.6f" % (volts)    
    return volts
    
while True:
    # read data
    
    dataIn = serialport.read(30)
    data = readData(dataIn.strip())
    
    
    
    
    print "**** start ****"
    print data
    print len(data)
    print data[0]
    if len(data)>1:
        print data[1]
    print "***** end *****" 
    
    destance = howFar()
    if destance >= 2:
        left = 0
        right = 0
    else:
        left = 29
        right = 30
        
    
    
    '''
    if len(data[0]) >0:
        speed = int(data[0])
     
    
    if len(data) >1:
        steer = int(data[1])
        
    if speed > 50:
        speed = 50
        
    if speed < -50:
        speed = -50
    
     
    if steer == 0:
        left = speed
        right = speed
    if steer > 0:
        left = speed/3
        right = speed

    if steer < 0:   
        left = speed
        right = speed/3
 '''
    print "left: " + str(left) + " right: " + str(right)
    
    
    dataOut = str(left) + "," + str(right) +"\n"
    
    
    
    print "Data out " + "|" + dataOut + "|"
    
    serialport.write(dataOut)
    sleep(0.125)
    
    

serial.close()



