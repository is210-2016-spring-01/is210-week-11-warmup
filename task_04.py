#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 4 docstring."""


import car


class CustomCar(car.Car):
    """Child-class of car.Car."""

    def __init__(self, color='black', tires=None):
        """Constructor for CustomCar class.

        Args:
            color (string): The color of the car.
            tires (int): The number of tires.

        Attributes:
            color (string): The color of the car.
            tires (int): The number of tires.
        """
        car.Car.__init__(self, color)
        self.color = color
        if tires is None:
            tires = []
            while len(tires) < 4:
                tires.append(CustomTire())
        self.tires = tires


class CustomTire(car.Tire):
    """Child-class of car.Tire."""

    __maximum_miles = 500
