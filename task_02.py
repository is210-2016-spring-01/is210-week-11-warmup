#!/usr/bin/ env python
# -*- coding: utf-8 -*-
"""Task 02: timestamps"""


import time


class Snapshot(object):
    """timestamps"""

    def __init__(self):
        """constructor"""
        self.created = time.time()
