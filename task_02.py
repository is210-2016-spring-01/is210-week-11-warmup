#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides functions specifically related to time."""

import time


class Snapshot(object):
    """This class produces a Unix Timestamp.
    Attributes: None
    """
    def __init__(self):
        """A constructor for the class Snapshot.

        Arguments:
            time(mix): A timestamp from a Unix clock

        Attributes:
            time(mix): A time span from a Unix clock
        """
        self.created = time.time()
