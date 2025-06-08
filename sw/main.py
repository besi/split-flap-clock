from machine import Pin
from machine import ADC
import machine
import time
from digit import Digit
import neopixel

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION, Driver, Command
from machine import Pin

d = 0.001
BLANK=11

(year,month,mday,h,m,s,weekday,yearday) = time.localtime()

c1 = -10
s1 = Stepper(HALF_STEP, Pin(10, Pin.OUT), Pin(9, Pin.OUT), Pin(3, Pin.OUT), Pin(8, Pin.OUT), d)
h1 = Pin(18, Pin.IN)
d1 = Digit(s1, h1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], c1, 1, label='Weekdays')

c2 = -10
s2 = Stepper(HALF_STEP, Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(21, Pin.OUT), Pin(11, Pin.OUT), d)
h2 = Pin(12,Pin.IN)
d2 = Digit(s2, h2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], c2, 1, label='Days10')

c3 = -10
s3 = Stepper(HALF_STEP, Pin(40, Pin.OUT), Pin(39, Pin.OUT), Pin(38, Pin.OUT), Pin(6, Pin.OUT), d)
h3 = Pin(47, Pin.IN)
d3 = Digit(s3, h3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], c3, 1, label='Days')

c4 = -10
s4 = Stepper(HALF_STEP, Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(42, Pin.OUT), Pin(41, Pin.OUT), d)
h4 = Pin(48, Pin.IN)
d4 = Digit(s4, h4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], c4, 1, label='Months')

d1.calibrate()
d1.show(weekday)

d2.calibrate()
tens = int(mday/10)
if tens == 0: 
    d2.show(10) # blank
else:
    d2.show(tens)

d3.calibrate()
d3.show(mday%10)

d4.calibrate()
d4.show(month)


# Buttons
mode = Pin(0, Pin.IN)
button_a = Pin(17, Pin.IN)
button_b = Pin(16, Pin.IN)
buttons = [mode, button_a, button_b]

# I2C
from machine import Pin, SoftI2C
scl = Pin(17, Pin.IN, Pin.PULL_UP)
sda = Pin(16, Pin.IN, Pin.PULL_UP)
i2c = SoftI2C(scl,sda)

np = neopixel.NeoPixel(machine.Pin(13),2)
#np.fill((1,1,1))
#np.write()

def showTime():
    (year,month,mday,h,m,s,weekday,yearday) = time.localtime()
    d1.show(weekday)
    tens = int(mday/10)
    if tens == 0: 
        d2.show(10) # blank
    else:
        d2.show(tens)

    d3.show(mday%10)
    d4.show(month)

while True:
    showTime()
    time.sleep(60)
    