#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating our own class."""


# Python libs
import time


class Snapshot(object):
    """A custom class to capture timestamp.

    Returns the current Unix timestamp.

    Args:

    Attributes:
        created (numeric): The Unix timestamp when run.
    """

    def __init__(self):
        """Returns the current timestamp.

        Returns:
            integer: The current Unix timestamp.

        Examples:

            >>> stamp = Snapshot()
            >>> stamp.created()
            1459807619.273144
        """
        self.created = time.time()
