#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04 Module"""

import car


class CustomCar(car.Car):
    """Creates a child class for Custom Cars.

        Attributes:
            None
    """

    def __init__(self, color=None, tires=None):
        """Constructur for CustomCar class

        Args:
            color (str): A string indicating the color of the car
            tires (list): A list of CustomTire objects

        Attributes:
            tires (list): A list of four CustomTire objects
        """
        car.Car.__init__(self, color)
        self.color = color
        if tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """Creates a child class for custom tires.

    Attributes:
        None
    """

    __maximum_miles = 500
