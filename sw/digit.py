from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION, Driver, Command
import time
HALL_ACTIVE = 0

class Digit():
    def __init__(self, stepper, sensor, labels = [], offset = 0, direction = 1):
        self.stepper = stepper
        self.sensor = sensor
        self.labels = labels
        self.direction = direction
        scelf.position = -1
        self.offset = offset

    def calibrate(self):
        print(f"{self.labels}")

        print(f"Starting calibration")
        while self.sensor() != HALL_ACTIVE:
            self.stepper.step(1, self.direction)
            self.position = 2
            
        time.sleep(.5)        
        print(f"Starting at position {self.position}")
        while self.sensor() == HALL_ACTIVE:
            self.position += 1
            self.stepper.step(1,self.direction)
            print(f"fine tune {self.position}")
        
        print("Go to center")
        self.stepper.step(int(self.position /2), -self.direction)
        print("Go to offset")
        self.stepper.step(self.offset-5, self.direction)
        self.stepper.step(5, self.direction)
        print(f"calibration ended at position {self.position}")
                

if __name__ == '__main__':
    from machine import Pin
    d = 0.001

    s1 = Stepper(HALF_STEP, Pin( 4, Pin.OUT), Pin( 2, Pin.OUT), Pin(15, Pin.OUT), Pin(32, Pin.OUT), d)
    hall1 = Pin(34, Pin.IN)
    d1 = Digit(s1,hall1, ['Mo','Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'],46,1)
    d1.calibrate()
    
    s2 = Stepper(HALF_STEP, Pin(33, Pin.OUT), Pin(25, Pin.OUT), Pin(26, Pin.OUT), Pin(27, Pin.OUT), d)
    hall2 = Pin(35,Pin.IN)
    d2 = Digit(s2,hall2, [0,1,2,3,4,5,6,7,8,9],490,-1)
    d2.calibrate()
                  