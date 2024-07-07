import RPi.GPIO as GPIO                                          
import time


GPIO.setmode(GPIO.BCM)  #Access by BCM number                        
GPIO.setup(15,GPIO.OUT) #BCM : 15pin (Physical : 10pin)                                

try:
    while True:
        print("loop")
        
        GPIO.output(15,GPIO.HIGH)
        time.sleep(1.0)
        
        GPIO.output(15,GPIO.LOW)
        time.sleep(1.0)
                
except KeyboardInterrupt:
    GPIO.cleanup()