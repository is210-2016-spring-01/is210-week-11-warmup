#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates subclasses."""

import produce


class Apple(produce.Produce):
    """An object which stores the apples produced.
    Arguments:
        Produce(object): Amount of produce
    Attribute:
        duration(int): Duration for apple production
    """
    duration = 5356800
