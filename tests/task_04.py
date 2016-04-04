#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom Cars"""

import car


class CustomCar(car.Car):
    """ A new and improved version of the car class"""

    def __init__(self, color='blue', tires=None):
        """A constructor of the CustomCar class

        Arguments:
            tires(int): The number of tires used on the car.

        Attributes:
            None

        Returns:
            tires(lists): The number of tires on the car.

        Example:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4
        """

        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """Tire strength

    Arguments:
        miles(int): Number of miles the tires can withstand

    Attributes:
        None
    """

    __maximum_miles = 500
