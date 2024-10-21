#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:57:45 2024

@author: ageiges
"""

import datatoolbox as dt
import numpy as np
import pandas as pd
import os

dt.admin.switch_database_to_testing()


def year_indexes_only():
    years = dt.idx.year_indexes_only(pd.Index(["2032", "Dec, 23", 1990]))

    assert years == ["2032", 1990]


def test_string_index_to_iso():
    index = pd.Index(['Germany', 'United States of America',' CubA'])
    
    assert (dt.idx.convert_idx_string_to_iso(index) == pd.Index(['DEU', 'USA', 'CUB'])).all()
    
    assert (dt.idx.convert_idx_string_to_iso(index, iso_type='alpha2') == pd.Index(['DE', 'US', 'CU'])).all()
    
    assert (dt.idx.convert_idx_string_to_iso(index, iso_type ='numISO') == pd.Index(['276', '840', '192'])).all()
    index = pd.Index(['Test_fail'])
    
    assert pd.isna(dt.idx.convert_idx_string_to_iso(index)[-1])
