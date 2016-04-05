#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing existing class to alter its properties."""

import produce


class Apple(produce.Produce):
    """ Updating subclass attribute.

    Attributes:
        duration (int):
    """
    duration = 5356800
