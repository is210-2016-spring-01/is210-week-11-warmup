#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


import time


class Snapshot(object):
    """Object that stores Snapshot data."""

    def __init__(self, created=time.time()):
        self.created = created
