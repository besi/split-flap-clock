from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION, Driver, Command
import time
HALL_ACTIVE = 0

class Digit():
    def __init__(self, stepper, sensor, labels = [], offset = 0, direction = 1, label =''):
        self.stepper = stepper
        self.sensor = sensor
        self.labels = labels
        self.direction = direction
        self.position = -1
        self.offset = offset
        self.label = label

    def calibrate(self):
        print(f"Calibrating the {self.label} digit")
        print(f"{self.labels}")

        if self.sensor() == HALL_ACTIVE:
            self.position = 0 
            while self.sensor() == HALL_ACTIVE:
                self.stepper.step(1, -self.direction)
                self.position += 1
            print(f"moved {self.position} out of the magnet area")

        self.position = 0
        print(f"Starting calibration")
        while self.sensor() != HALL_ACTIVE:
            self.stepper.step(1, self.direction)
            self.position +=1
            
        print(f"Found the magnet after {self.position} steps")
        self.position = 0
        print(f"Starting at position {self.position}")
        while self.sensor() == HALL_ACTIVE:
            self.position += 1
            self.stepper.step(1,self.direction)
        print(f"Reached end of hall sensor at {self.position}")
        
        print("Go to center of magnet")
        self.stepper.step(int(self.position / 2), -self.direction)
        self.position = 0
        print("Go to offset")
        self.stepper.step(self.offset-5, self.direction)
        time.sleep(0.5)
        self.stepper.step(5, self.direction)
        self.positon = self.offset
        print(f"calibration ended at position {self.position}")
                

if __name__ == '__main__':
    from machine import Pin
    d = 0.001

    s1 = Stepper(HALF_STEP, Pin( 4, Pin.OUT), Pin( 2, Pin.OUT), Pin(15, Pin.OUT), Pin(32, Pin.OUT), d)
    hall1 = Pin(34, Pin.IN)
    d1 = Digit(s1,hall1, ['Mo','Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'],32,1, label='Weekdays')
    d1.calibrate()
    
    s2 = Stepper(HALF_STEP, Pin(33, Pin.OUT), Pin(25, Pin.OUT), Pin(26, Pin.OUT), Pin(27, Pin.OUT), d)
    hall2 = Pin(35,Pin.IN)
    d2 = Digit(s2,hall2, [1,2,3,4,5,6,7,8,9,0],33,-1, label='Days')
    d2.calibrate()
                  