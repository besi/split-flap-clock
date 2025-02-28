from machine import Pin
from machine import ADC
import machine
import time
import neopixel

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION, Driver, Command
from machine import Pin

def combinations(arr, path=[]):
    # Base case
    if len(path) == len(arr):
        print(path)
        stepper = make_stepper(path)
        stepper.step(44)
    
    # Recursive case
    for num in arr:
        if num not in path:
            combinations(arr, path + [num])

def make_stepper(pins):
    return Stepper(HALF_STEP, Pin(pins[0], Pin.OUT), Pin(pins[1], Pin.OUT), Pin(pins[2], Pin.OUT), Pin(pins[3], Pin.OUT), 0.001)

#combinations([23,22,21,19]) # stepper 1
#combinations([18,05,17,16]) # stepper 2
combinations([4,2,15,32]) # stepper 3
combinations([33,25,26,27]) # stepper 4
