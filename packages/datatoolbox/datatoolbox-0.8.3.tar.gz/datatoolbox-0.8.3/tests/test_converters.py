#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:48:08 2022

@author: ageiges
"""

import copy
import datatoolbox as dt

from util_for_testing import df, df2, sourceMeta

dt.admin.switch_database_to_testing()


def test_to_xdataset():
    idf = dt.findp(source="Numbers_2020").as_pyam()

    ds1 = dt.converters.to_xdataset(idf)

    tables = dt.findp(source="Numbers_2020").load()

    ds2 = dt.converters.to_xdataset(tables)


def test_to_pyam():
    tables = dt.findp(source="Numbers_2020").load()

    for table in tables:
        table.meta["model"] = "test"

    ds = dt.converters.to_xdataset(tables)

    idf1 = dt.converters.to_pyam(ds)

    idf2 = dt.converters.to_pyam(ds["Numbers|Ones"])

    idf3 = dt.converters.to_pyam(tables)

    assert all(idf1.timeseries() == idf3.timeseries())


def test_to_tableset():
    idf = dt.findp(source="Numbers_2020").as_pyam()

    ts1 = dt.converters.to_tableset(idf, additional_meta={"source": "test"})

    wdf = dt.findp(source="Numbers_2020").as_wide_dataframe()
    ts2 = dt.converters.to_tableset(wdf)
