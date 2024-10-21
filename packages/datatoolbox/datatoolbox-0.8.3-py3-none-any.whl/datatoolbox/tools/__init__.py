#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:05:30 2020

@author: ageiges
"""

import time as _time

tt = _time.time()
from datatoolbox import config as _config


# %% optional
if _config.AVAILABLE_XARRAY:
    from . import xarray
    import pint_xarray
    from datatoolbox.core import unit_registry

    pint_xarray.accessors.setup_registry(unit_registry.ur)
    pint_xarray.unit_registry = unit_registry.ur
    pint_xarray.accessors.default_registry = unit_registry.ur

from . import pyam

from . import word

if _config.DEBUG:
    print("Tools initialised in {:2.4f} seconds".format(_time.time() - tt))
