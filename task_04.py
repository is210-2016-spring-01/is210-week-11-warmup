#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warmup Tasks."""

import car


class CustomCar(car.Car):
    """CustomCar class."""
    def __init__(self, color='red', tires=None):
        car.Car.__init__(self, color)
        if tires is None:
            self.tires = [CustomTire(), CustomTire(),
                          CustomTire(), CustomTire()]
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """CustomTire class."""
    __maximum_miles = 500
