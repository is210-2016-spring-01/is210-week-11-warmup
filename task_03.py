#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercising with subclasses."""

import produce


class Apple(produce.Produce):
    """A subclass of Produce.

    Returns the duration of the produce.

    Args:

    Attributes:
        duration (numeric): Time produce is good to eat.
    """
    duration = 5356800
