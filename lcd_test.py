import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import I2C_driver as LCD
import time

Switch= 10
LED = 12
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
mylcd = LCD.lcd()

while True:
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
        mylcd.lcd_clear()
        mylcd.lcd_display_string("LED ON",1)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        
    else:
        print("Button was not pushed!")
        mylcd.lcd_clear()
        mylcd.lcd_display_string("LED OFF",1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)

