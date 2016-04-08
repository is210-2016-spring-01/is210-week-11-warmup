#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses subclasses to demonstrate the has-a and is -a concepts."""

import car


class CustomCar(car.Car):
    """A childclass of carCar."""


def __init__(self, color='pink', tires=None):
    """ Constructor for custom car
    Args:
        tires (list): list of CustomTire objects.
    Attributes:
        tires: if none will append up to 8
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
