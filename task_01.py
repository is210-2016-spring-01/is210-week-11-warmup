#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 11 Warmup Tasks. """

import produce


TOMATO = produce.Produce()
EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
