from machine import Pin
from machine import ADC
import machine
import time
import neopixel

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION, Driver, Command
from machine import Pin

# does not work
s1 = Stepper(HALF_STEP, Pin(23, Pin.OUT), Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(19, Pin.OUT), delay=.003 )

# does not work
s2 = Stepper(HALF_STEP, Pin(18, Pin.OUT), Pin( 5, Pin.OUT), Pin(17, Pin.OUT), Pin(16, Pin.OUT), delay=.003 )

s3 = Stepper(HALF_STEP, Pin( 4, Pin.OUT), Pin( 2, Pin.OUT), Pin(15, Pin.OUT), Pin(32, Pin.OUT), delay=.003 )
s4 = Stepper(HALF_STEP, Pin(33, Pin.OUT), Pin(25, Pin.OUT), Pin(26, Pin.OUT), Pin(27, Pin.OUT), delay=.003 )

# Buttons
mode = Pin(0, Pin.IN)
button_a = Pin(14, Pin.IN)
button_b = Pin(12, Pin.IN)

# Hall sensors
h1 = Pin(36,Pin.IN)
h2 = Pin(39,Pin.IN)
h3 = Pin(34,Pin.IN)
h4 = Pin(35,Pin.IN)

sensors = [h1, h2, h3, h4]
steppers = [s1, s2, s3, s4]
buttons = [mode, button_a, button_b]

mode = Pin(0, Pin.IN)

MARGIN = 0.9
ACTIVE = 0

clockwise = 1


# I2C
from machine import Pin, SoftI2C
scl = Pin(14, Pin.IN, Pin.PULL_UP)
sda = Pin(12, Pin.IN, Pin.PULL_UP)
i2c = SoftI2C(scl,sda)

# Neopixel does not work
np = neopixel.NeoPixel(machine.Pin(13),2)
np.fill((250,250,250))
np.write()
current = s4

runner = Driver()


while True:
    
    for button in buttons:
        if button() == 0:
            print(f"Button number {buttons.index(button)} pressed")
    
    for sensor in sensors:
        if sensor() == 4:
            index = sensors.index(sensor)
            current = steppers[index]
            print(f"Hall Sensor {index+1} activated starting motor {index + 1}")
            time.sleep(.5)
    for stepper in steppers:
        stepper.step(3,1)