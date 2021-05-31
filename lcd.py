import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import I2C_driver as LCD
from time import *

GPIO.setmode(GPIO.BOARD)
Switch= 10
LED = 12
mylcd = LCD.lcd()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(LED, GPIO.HIGH)
        mylcd.lcd_display_string("LED ON",1)
        time.sleep(3)
        mylcd.lcd_clear()
        sleep(0.2)
    else:
        print("Button was not pushed!")
        GPIO.output(LED, GPIO.LOW)
        mylcd.lcd_display_string("LED OFF",1)
        time.sleep(1)
        mylcd.lcd_clear()
        sleep(0.2)

