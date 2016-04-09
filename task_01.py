#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""First Task of Week 11"""

import produce

TOMATO = produce.Produce()
EGGPLANT = produce.Produce(1311210802)
TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
