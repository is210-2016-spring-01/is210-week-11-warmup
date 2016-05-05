#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 11 warmup task 1 that crreates and modifieds two objects."""

import produce

TOMATO = produce.Produce()

EGGPLANT = produce.Produce(arrival=1311210802)

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
