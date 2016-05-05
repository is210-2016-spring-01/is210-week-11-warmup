#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: instances and their values"""


import produce

TOMATO = produce.Produce('Tomato')

EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
