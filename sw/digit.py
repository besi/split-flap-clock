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
        self.correction = 0
        self.is_calibrated = False
    
    def hall_active(self):
        return self.sensor() == HALL_ACTIVE

    def advance_to(self, position):
        position = round(position)
        print(f"Advance from {self.position} to {position}")
        if position > self.position:
            self.advance(position - self.position)
        elif position == round(self.position):
            print("Already there")
        else:
            print(f"Advance over zero to {FULL_ROTATION - self.position + position}")
            self.advance(FULL_ROTATION - self.position + position) 

    def show(self, label):
        if label in self.labels and self.is_calibrated:
            i = self.labels.index(label)
            self.advance_to(i * FULL_ROTATION / len(self.labels))

    def advance(self, steps):
        steps_left = round(steps - self.correction) % FULL_ROTATION
        self.correction = 0
        old = self.position
        self.position += steps
        if self.position < 0:
            self.position += FULL_ROTATION
            print(f"Added FULL_ROTATION to get to {self.position}")
        if self.position >= FULL_ROTATION:
            self.position -= FULL_ROTATION
            print(f"Removed FULL_ROTATION to get to {self.position}")
        start = -1
        end = -1
        
        while steps_left > 0:
            i = steps - steps_left
            self.stepper.step(1, self.direction)
            if self.hall_active() and start == -1:
               start = old + i
            if not self.hall_active() and start != -1:
                end = old + i 
                self.correction = round(FULL_ROTATION - (end - (end-start) / 2) - self.offset) % FULL_ROTATION
                start = -1
            steps_left -= 1
        correction_string = f"correction of {self.correction}" if abs(self.correction) > 0 else ''
        print(f"Went: {steps} steps from: {old} to: {self.position} {correction_string}") 


    def calibrate(self, move_to_first = False):
        print(f"Calibrating the {self.label} digit")
        print(f"{self.labels}")

        if self.hall_active():
            i = 0
            while self.hall_active():
                self.stepper.step(1, -self.direction)
                i += 1
            print(f"moved {i} out of the magnet area")

        i = 0
        print(f"Starting calibration")
        while not self.hall_active():
            self.stepper.step(1, self.direction)
            i += 1
            
        print(f"Found the magnet after {i} steps")
        i = 0
        while self.hall_active():
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
        self.position = self.position % FULL_ROTATION
        print(f"calibration ended at position {self.position}")
        self.is_calibrated = True

if __name__ == '__main__':
    from machine import Pin  
    s1 = Stepper(HALF_STEP, Pin(10, Pin.OUT), Pin(9, Pin.OUT), Pin(3, Pin.OUT), Pin(8, Pin.OUT), 0.001)
    d1 = Digit(s1, Pin(18, Pin.IN), list(range(0,12)), -10, 1, label='Weekdays')
    d1.calibrate()
    d1.show(0)
