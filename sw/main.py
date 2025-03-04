from machine import Pin
from machine import ADC
import machine
import time
from digit import Digit
import neopixel

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION, Driver, Command
from machine import Pin

d = 0.001

s1 = Stepper(HALF_STEP, Pin(23, Pin.OUT), Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(19, Pin.OUT), d)
h1 = Pin(36, Pin.IN)
d1 = Digit(s1, h1, [0,1,2,3,4,5,6,7,8,9], 35, 1, label='Weekdays')
d1.calibrate()

s2 = Stepper(HALF_STEP, Pin(18, Pin.OUT), Pin( 5, Pin.OUT), Pin(17, Pin.OUT), Pin(16, Pin.OUT), d)
h2 = Pin(39,Pin.IN)
d2 = Digit(s2, h2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 35, 1, label='Days10')
d2.calibrate()

s3 = Stepper(HALF_STEP, Pin( 4, Pin.OUT), Pin( 2, Pin.OUT), Pin(15, Pin.OUT), Pin(32, Pin.OUT), d)
h3 = Pin(34, Pin.IN)
d3 = Digit(s3, h3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 25, -1, label='Days')
d3.calibrate()

s4 = Stepper(HALF_STEP, Pin(33, Pin.OUT), Pin(25, Pin.OUT), Pin(26, Pin.OUT), Pin(27, Pin.OUT), d)
h4 = Pin(35, Pin.IN)
d4 = Digit(s4, h4, [1,2,3,4,5,6,7,8,9,10,11,12], 480, -1, label='Months')
d4.calibrate()


# Buttons
mode = Pin(0, Pin.IN)
button_a = Pin(14, Pin.IN)
button_b = Pin(12, Pin.IN)
buttons = [mode, button_a, button_b]

# I2C
from machine import Pin, SoftI2C
scl = Pin(14, Pin.IN, Pin.PULL_UP)
sda = Pin(12, Pin.IN, Pin.PULL_UP)
i2c = SoftI2C(scl,sda)

np = neopixel.NeoPixel(machine.Pin(13),2)
#np.fill((1,1,1))
#np.write()

def showTime():
    (year,month,mday,h,m,s,weekday,yearday) = utime.localtime()
    d1.show(weekday)
    d2.show(int(mday/10))
    d3.show(mday%10)
    d4.show(month)

while True:
    
    showTime()
    time.sleep(60)