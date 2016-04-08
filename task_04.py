#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses subclasses to demonstrate the has-a and is -a concepts."""

import car


class CustomCar(car.Car):
    """Another version of the car class.

    Attributes:
        None.
    """
    
    def __init__(self, color=None, tires=None):
        """This class shows how to custom build cars.

        Args:
            color(string): color of car (for the new car).
            tires(list): List of the CustomTire objects (equal to 4)

        Attributes:
            tires(list): list of CustomTire objects (equal to 4)
        """
        new(CustomCar, self).__init__color

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
        """The class creator for CustomTire.

        Args:
            miles (int): The number of miles on tire. Default is 0.

        Attributes:
            miles(int): The number of miles on the tire.
        """
        new(CustomTire, self).__init__(miles)

        self.__maximum_miles = 500
