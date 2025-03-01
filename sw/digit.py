from uln2003 import Stepper, HALF_STEP, FULL_ROTATION
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
        self.magnet_range = 0

    def advance_to(self, position):
        print(f"Advance from {self.position} to {position}")
        if position > self.position:
            print(f"a: advance {position - self.position}")
            self.advance(position - self.position)
        elif position == self.position:
            print("bAlready there")
        else:
            print(f"c: advance {FULL_ROTATION - self.position + position}")
            self.advance(FULL_ROTATION - self.position+position) 

    def show(self, label):
        if label in self.labels:
            i = self.labels.index(label)
            self.advance_to(i * FULL_ROTATION / len(self.labels))

    def advance(self, steps):
        steps = steps % FULL_ROTATION
        self.stepper.step(steps, self.direction)
        old = self.position
        self.position += steps
        if self.position < 0:
            self.position += FULL_ROTATION
            print(f"Added FULL_ROTATION to get to {self.position}")
        if self.position >= FULL_ROTATION:
            self.position -= FULL_ROTATION
            print(f"Removed FULL_ROTATION to get to {self.position}")
        print(f"Went {steps} steps from {old} to {self.position}") 

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
        self.magnet_range = self.position
        print("Go to center of magnet")
        self.stepper.step(int(self.position / 2), -self.direction)
        self.position = 0
        print("Go to offset")
        self.stepper.step(self.offset-5, self.direction)
        time.sleep(0.1)
        self.stepper.step(5, self.direction)
        self.positon = self.offset
        print(f"calibration ended at position {self.position}")
                

if __name__ == '__main__':
    from machine import Pin
    d = 0.001

    s1 = Stepper(HALF_STEP, Pin( 4, Pin.OUT), Pin( 2, Pin.OUT), Pin(15, Pin.OUT), Pin(32, Pin.OUT), d)
    hall1 = Pin(34, Pin.IN)
    d1 = Digit(s1, hall1, ['Mo','Di', 'Mi', 'Do', 'Fr', 'Sa', 'So', '','',''], 32, 1, label='Weekdays')
    d1.calibrate()

    s2 = Stepper(HALF_STEP, Pin(33, Pin.OUT), Pin(25, Pin.OUT), Pin(26, Pin.OUT), Pin(27, Pin.OUT), d)
    hall2 = Pin(35, Pin.IN)
    d2 = Digit(s2, hall2, [1,2,3,4,5,6,7,8,9,0], 32, -1, label='Days')
    d2.calibrate()
