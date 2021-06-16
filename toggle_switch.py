import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

Switch= 10
LED = 12
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

while True:
    if GPIO.input(Switch) == GPIO.HIGH:
        time.sleep(0.2)
        while True:
            #print("Button was pushed!")
            GPIO.output(LED, GPIO.HIGH)
            if GPIO.input(Switch) == GPIO.HIGH:
                time.sleep(0.2)
                break
                
    else:
        #print("Button was not pushed!")
        GPIO.output(LED, GPIO.LOW)
        

