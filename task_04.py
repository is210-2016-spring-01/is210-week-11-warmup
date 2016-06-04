#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing and extending the Car()."""

import car


class CustomCar(car.Car):
    """Custom instance of Car class."""

    def __init__(self, color='black', tires=None):
        """CustomCar() constructor with list of tires added.

        Args:
            color (str): Color of car. Default is black.
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
    """Custom instance of Tire class."""
    __maximum_miles = 500
