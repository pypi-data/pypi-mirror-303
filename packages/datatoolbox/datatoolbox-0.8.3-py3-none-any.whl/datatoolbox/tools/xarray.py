#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains all relevant tools regarding the use of xarray


@author: ageiges
"""

# from datatoolbox import core
import datatoolbox as dt

from time import time


# %%


load_as_xdataset = dt.data_structures.load_as_xdataset
key_set_to_xdataset = dt.data_structures.key_set_to_xdataset

if __name__ == "__main__":
    import datatoolbox as dt

    tt = time()
    # tbs = dt.getTables(dt.find(entity = 'Emissions|CO2', source='IAMC15_2019_R2').index[:])

    tbs = [
        dt.getTable(x)
        for x in dt.find(entity="Emissions|CO2", source="IAMC15_2019_R2").index
    ]
    print(f"Load data: {time()-tt:2.2f}s")
    dimensions = [
        "model",
        "scenario",
        "median warming at peak (MAGICC6)",
        "region",
        "time",
    ]
    stacked_dims = {
        "pathway": ("model", "scenario", "median warming at peak (MAGICC6)")
    }
    xData = _to_xarray(tbs, dimensions, stacked_dims)
