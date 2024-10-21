#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:36:58 2024

@author: andreasgeiges
"""

from datatoolbox import core


def test_valid_unit():
    assert core.unit_registry.is_valid_unit("Mt CO2")


def test_get_unit():
    ur = core.unit_registry.ur
    core.unit_registry.getUnit(ur("Mt CH4"))


def test_is_known_entity():
    assert core.is_known_entity("Emissions|CO2")
    assert core.is_known_entity("Emissions|HFCs")


def test_split_variable():
    from util_for_testing import df_var

    meta = core._split_variable(df_var.meta)
    assert meta["entity"] == "Emissions|CO2"
    assert meta["category"] == "Aviation"
