# ADC
from machine import Pin
from machine import ADC
adc = ADC(0)
ir = Pin(2,Pin.OUT)
ir.value(0) # Enable IR diode so that we can receive what is reflected back
print(f"Distance Sensor: {adc.read()}")


# Read temperature and Humidity
from machine import Pin, SoftI2C
from hdc1080 import HDC1080

scl = Pin(5, Pin.IN, Pin.PULL_UP)
sda = Pin(4, Pin.IN, Pin.PULL_UP)
i2c = SoftI2C(scl,sda)
temp = HDC1080(i2c)
print(f"Temperature {temp.temperature()}°C")
print(f"Humidity {temp.humidity()}%")

import machine
import time

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION
from machine import Pin

stepper = Stepper(HALF_STEP, Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT), delay=.003 )  
mode = Pin(0, Pin.IN)

MARGIN = 0.9
ACTIVE = 0

# Nod hello
clockwise = 1
dir = 1
stepper.step(7, dir)
dir = dir * -1
stepper.step(7, dir)
dir = clockwise
correction = 0
while True:
    # Rotate in steps
    # Change direction when button is pressed
    if mode() == ACTIVE:
        
        correction += 1
        stepper.step(int(FULL_ROTATION/10), dir)
        time.sleep(.2)
        if correction%10 == 0:
            stepper.step(3, dir) # Add the missing 3 steps (513/10 = 51.3) .3*10 = 3
    
        

