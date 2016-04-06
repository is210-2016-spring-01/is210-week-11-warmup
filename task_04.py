#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 11 warmup task 1 that crreates and modifieds two objects."""

import car


class CustomCar(car.Car):
    """A subclass of Car for Custom Cars

    Attributes:
        None.
    """

    def __init__(self, color=None, tires=None):
        """The class constructor for CustomCar

        Args:
            color (string): color of the car (for the super constructor).
            tires (list): list of the CustomTire objects (should be 4).

        Attributes:
            tires (list): list of the CustomTire objects (should be 4).
        """
        super(CustomCar, self).__init__(color)

        if tires is None:

            self.tires = []
            for i in xrange(4):

                self.tires.append(CustomTire(i-i))
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """A subclass of Tire for CustomTire

    Attributes:
        None.
    """

    def __init__(self, miles=0):
        """The class constructor for CustomTire

        Args:
            miles (int): The number of miles on the tire. Default is 0.

        Attributes:
            miles (int): The number of miles on the tire.
        """
        super(CustomTire, self).__init__(miles)

        self.__maximum_miles = 500
