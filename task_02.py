#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 11 warmup task 1 that crreates and modifieds two objects."""

import time


class Snapshot(object):
    """A generic class to timestamp a "Snapshot".

    Attributes:
        none.
    """

    def __init__(self):
        """class constructor that stores the created time of the object.

        Args:
            none.

        Attributes:
            created (numeric): The time the object was created in a Unix
                                timestamp.
        """
        self.created = time.time()
