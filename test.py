import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

arr1 = [1,0,0,0]
arr2 = [0,1,0,0]
arr3 = [0,0,1,0]
arr4 = [0,0,0,1]
#GPIO.output(pin, 0 or 1)
i = 0
print "before loop"
while True:

    GPIO.output(4, 1)
    GPIO.output(17, 1)
    GPIO.output(27, 0)
    GPIO.output(22, 0)
    
    time.sleep(0.001);
    
    GPIO.output(4, 0)
    GPIO.output(17, 1)
    GPIO.output(27, 1)
    GPIO.output(22, 0)

    time.sleep(0.001);
    
    GPIO.output(4, 0)
    GPIO.output(17, 0)
    GPIO.output(27, 1)
    GPIO.output(22, 1)

    time.sleep(0.001);
    
    GPIO.output(4, 1)
    GPIO.output(17, 0)
    GPIO.output(27, 0)
    GPIO.output(22, 1)

    time.sleep(0.001);
