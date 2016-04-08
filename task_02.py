#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 11 Warmup Tasks. """

import time


class Snapshot(object):
    """generic Object class"""
    def __init__(self):
        self.created = time.time()
