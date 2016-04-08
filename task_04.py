#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module demonstrates the has-a and is -a concepts."""

import car


class CustomCar(car.Car):
    """A type of the car class"""

    def __init__(self, color='blue', tires=None):
        """A creator of the CustomCar class

        Args:
            tires(int): The number of tires used on the car

        Attributes:
            tires: If none will append up to 4.
        """
        car.Car.__init__(self, color)
        if tires is None:
            tires = []
            while len(tires) < 4:
                tires.append(CustomTire())
        self.tires = tires


class CustomTire(car.Tire):
    """Child class of car.Tire."""
    __maximum_miles = 500
