#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""

import time


class Snapshot(object):
    """A class that returns a Unix Timestamp.

    Attributes:
        None
    """

    def __init__(self):
        """A constructor for the Snapshot class

        Attributes:
            time (int): The current Unix Timestamp
        """

        self.created = time.time()
