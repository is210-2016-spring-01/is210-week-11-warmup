#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This modlue uses subclasses to demonstrate the has-a and is -a concepts."""

import car


class Custom(car.Car):
    """Another version of the car class."""

    def __init__(self, color='blue', tires=None):
        """This class shows how to custom build cars.
        Arguments:
            tires(int): The number of tires used on the car
        Attributes:
            None
        Returns:
            tires(list): The number of tires on the car
        Examples:
        >>> mycar = CustomCar()
        >>> len(mycar.tires)
        4
        """

    car.Car __init__(self, color):
    self.tires = tires
    if self.tires is None:
        self.tires = []
        while len(self.tires)<4:
            self.tires.append(CustomTire())


class  CustomTire(car.Tire):
    """Tire strength
    Arguments:
        max_miles(int): The maximum number of miles for which the tire functions.
    Attributes:
        None
    """
    _maximum_miles = 500
