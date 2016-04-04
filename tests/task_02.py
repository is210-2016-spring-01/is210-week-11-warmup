#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TimeStamp"""

import time


class Snapshot(object):
    """Class Snapshot that returns the current Unix Timestamp.

    Attributes: None
    """

    def __init__(self):
        """A Constructor for the class Snapshot

        Arguments:
            time(mix): A timestamp from the unix system clock
        Attributes:
            time(mix): A timestamp from the unix system clock
        """

        self.created = time.time()
