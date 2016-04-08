#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


import car

class CustomCar(car.Car):
    """a child class of car.Car"""
    def __init__(self, color=None, tires=None):
        """constructor. argument/attribute: tires.
        returns a list of car tires."""
        self.tires = tires
        car.Car.__init__(self, tires)
        self.tires = tires
        tires = CustomTire()
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tires)
                

class CustomTire(car.Tire):
    """a child class of car.Tire"""
        __maximum_miles = 500

