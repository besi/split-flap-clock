from uln2003 import Stepper, HALF_STEP, FULL_ROTATION
import time
HALL_ACTIVE = 0

class Digit():
    def __init__(self, stepper, sensor, labels = [], offset = 0, direction = 1, label =''):
        self.stepper = stepper
        self.sensor = sensor
        self.labels = labels
        self.direction = direction
        self.position = -99999
        self.offset = offset
        self.label = label
        self.magnet_range = 0

    def advance_to(self, position):
        print(f"Advance from {self.position} to {position}")
        if position > self.position:
            print(f"Advance {position - self.position}")
            self.advance(position - self.position)
        elif position == self.position:
            print("Already there")
        else:
            print(f"Advance over zero to {FULL_ROTATION - self.position + position}")
            self.advance(FULL_ROTATION - self.position + position) 

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

    def calibrate(self, move_to_first = False):
        print(f"Calibrating the {self.label} digit")
        print(f"{self.labels}")

        if self.sensor() == HALL_ACTIVE:
            i = 0
            while self.sensor() == HALL_ACTIVE:
                self.stepper.step(1, -self.direction)
                i += 1
            print(f"moved {i} out of the magnet area")

        i = 0
        print(f"Starting calibration")
        while self.sensor() != HALL_ACTIVE:
            self.stepper.step(1, self.direction)
            i += 1
            
        print(f"Found the magnet after {i} steps")
        i = 0
        while self.sensor() == HALL_ACTIVE:
            i += 1
            self.stepper.step(1,self.direction)
        print(f"Reached end of hall sensor at {i}")
        self.magnet_range = i
        # Go to the magnet center
        self.stepper.step(int(i / 2), -self.direction)
        print("Set the absolute zero relative to the offset")
        self.position = FULL_ROTATION - self.offset
            
        if move_to_first:
            print("Go to offset")
            self.advance(self.offset)
        
        print(f"calibration ended at position {self.position}")
