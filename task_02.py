#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Second Task of Week 11"""

import time


class Snapshot(object):
    """Returns timestamp (Unix)

    Attributes: None
    """

    def __init__(self):
        """What creates the Class Snapshot
        Arguments:
            time(mixed): timestamp of current time
        Attributes:
            time(mixed): timestamp of current time
        """
        self.created = time.time()
