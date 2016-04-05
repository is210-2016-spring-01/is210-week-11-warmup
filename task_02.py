#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a class from the ground-up."""

import time


class Snapshot(object):
    """ Object that returns Unix Timestamp

    Attributes:
        None.
    """
    def __init__(self):
        """ Constructor for Snapshot

        Args:
            None.

        Attributes:
        created (str):  returns time.
        """
        self.created = time.time()
