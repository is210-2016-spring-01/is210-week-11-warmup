#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrating has-a and is-a concept thru subclass."""

import car


class CustomCar(car.Car):
    """Child class of car.Car"""

    def __init__(self, color='red', tires=None):
        """ Constructor for CustomCar

        Args:
            tires (list): List of CustomTire objects.

        Attributes:
            tires:  If none will append up to 4.
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
