#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for subclassing"""

import car


class CustomCar(car.Car):
    """A docstring for a Car class instance."""

    def __init__(self, color='green', tires=None):
        """A docstring using a Car class and a list of tires.
        Args:
            color (str): Color of car. Default is green.
            tires (int): Number of tires. Default is None.
        Attributes:
           tires (list): List of tires.
        """
        self.color = color
        if tires is None:
            self.tires = []
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
        else:
            self.tires = tires
            car.Car.__init__(self, color)


class CustomTire(car.Tire):
    """A docstring for a Tire class instance."""
    __maximum_miles = 500
