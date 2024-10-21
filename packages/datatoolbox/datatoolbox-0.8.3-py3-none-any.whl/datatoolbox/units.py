#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:38:11 2022

@author: ageiges
"""

from . import core


# conversion factor between two units
conversionFactor = core.conversionFactor

getUnit = core.getUnit
getUnitWindows = core.getUnitWindows


def is_valid_unit(unit_str, ur=None):
    if ur is None:
        # unit registry
        ur = core.unit_registry.ur

    try:
        ur(unit_str)
        return True
    except Exception:
        return False
