#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a new class"""

import time


class Snapshot(object):
    """A docstring for a class that uses an object to get a timestamp.

    Returns the current Unix timestamp.

    Args:

    Attributes:
        created (numeric): The current Unix timestamp
    """

    def created(self):
        """Returns the current timestamp.

        Returns:
            integer: The current Unix timestamp.

        Examples:

            >>> stamp = Snapshot()

            >>> stamp.created()
            1459807619.273144
        """
        self.created = time.time()
