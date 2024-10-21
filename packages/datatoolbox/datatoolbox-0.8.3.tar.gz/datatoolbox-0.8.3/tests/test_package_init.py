#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:56:28 2024

@author: andreasgeiges
"""
import datatoolbox as dt


def test_tools():
    
    dt.tools.pint_xarray
    dt.tools.pyam
    dt.tools.xarray
    
    
def test_ur_lazy_import():
    dt.core.unit_registry.ur
    
def test_interfaces_lazy_import():
    dt.interfaces