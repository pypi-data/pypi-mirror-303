#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:30:40 2020

@author: ageiges
"""

import datatoolbox as dt
import numpy as np
from pandas.testing import assert_frame_equal
import pandas as pd
from util_for_testing import df1


def test_info():
    df1.info() == "4x4 Datatable with 10 entries, index from ARG to GBR and time from 2010 to 2010"


def test_yearly_change():
    table = df1.yearlyChange()


def test_meta_update():
    metaDict = {
        "source": "TEST",
        "entity": "values",
        "category": "cat1",
        "scenario": "#1",
        "unit": "m",
    }
    new_meta = dt.core._update_meta(metaDict)

    exp = dt.config.SUB_SEP["variable"].join(
        metaDict[x] for x in ["entity", "category"]
    )
    obs = new_meta["variable"]
    assert exp == obs


def test_creation():
    metaDict = {"source": "TEST", "entity": "values", "unit": "m"}
    metaDict2 = {"source": "TEST2", "entity": "area", "unit": "km"}

    data = np.asarray(
        [
            [1, 2.2, 3, 4],
            [2.3, np.nan, 3.4, np.nan],
            [1.3, np.nan, np.nan, np.nan],
            [np.nan, 3.4, 2.4, 3.2],
        ]
    )

    data2 = np.asarray(
        [
            [1, 2.2, 3, 4.5],
            [2.3, np.nan, 3.4, np.nan],
            [1.1, np.nan, np.nan, np.nan],
            [np.nan, 3.3, 2.4, np.nan],
        ]
    )

    df = dt.Datatable(
        data,
        meta=metaDict,
        columns=[2010, 2012, 2013, 2015],
        index=["ARG", "DEU", "FRA", "GBR"],
    )
    df2 = dt.Datatable(
        data2,
        meta=metaDict2,
        columns=[2009, 2012, 2013, 2015],
        index=["ARG", "DEU", "FRA", "GBR"],
    )

    assert isinstance(df, dt.Datatable)
    assert isinstance(df2, dt.Datatable)


def test_append():
    metaDict = {
        "source": "TEST",
        "scenario": "scen1",
        "entity": "Population",
        "unit": "m",
    }

    data = np.asarray(
        [
            [1, 2.2, 3, 4],
            [2.3, np.nan, 3.4, np.nan],
            [1.3, np.nan, np.nan, np.nan],
            [np.nan, 3.4, 2.4, 3.2],
        ]
    )

    metaDict2 = {"source": "TEST2", "entity": "area", "scenario": "scen2", "unit": "km"}
    data2 = np.asarray(
        [
            [1, 2.2, 3, 4.5],
            [2.3, np.nan, 3.4, np.nan],
            [1.1, np.nan, np.nan, np.nan],
            [np.nan, 3.3, 2.4, np.nan],
        ]
    )

    metaDict3 = {
        "source": "TEST2",
        "entity": "Population",
        "scenario": "scen3",
        "unit": "km",
    }
    data3 = np.asarray([[1, 2.2, 3, 4.5], [2.3, np.nan, 3.4, np.nan]])

    df = dt.Datatable(
        data,
        meta=metaDict,
        columns=[2010, 2012, 2013, 2015],
        index=["ARG", "DEU", "RUS", "IND"],
    )
    df2 = dt.Datatable(
        data2,
        meta=metaDict2,
        columns=[2009, 2012, 2013, 2015],
        index=["ARG", "DEU", "FRA", "GBR"],
    )
    df3 = dt.Datatable(
        data3, meta=metaDict3, columns=[2009, 2012, 2013, 2015], index=["FRA", "GBR"]
    )

    dt_merge = df.append(df3)
    obs_vlues = np.array(
        [
            [np.nan, 1.0e00, 2.2e00, 3.0e00, 4.0e00],
            [np.nan, 2.3e00, np.nan, 3.4e00, np.nan],
            [np.nan, 1.3e00, np.nan, np.nan, np.nan],
            [np.nan, np.nan, 3.4e00, 2.4e00, 3.2e00],
            [1.0e03, np.nan, 2.2e03, 3.0e03, 4.5e03],
            [2.3e03, np.nan, np.nan, 3.4e03, np.nan],
        ]
    )

    assert (dt_merge.values == obs_vlues)[~np.isnan(dt_merge.values)].all()
    assert dt_merge.meta["scenario"] == "computed: scen1+scen3"


def test_clean():
    metaDict2 = {"source": "TEST2", "entity": "area", "unit": "km"}

    data2 = np.asarray(
        [
            [1, 2.2, 3, np.nan],
            [2.3, np.nan, 3.4, np.nan],
            [1.1, np.nan, np.nan, np.nan],
            [np.nan, 3.3, 2.4, np.nan],
        ]
    )

    df2 = dt.Datatable(
        data2,
        meta=metaDict2,
        columns=[2009, 2012, 2013, 2015],
        index=["ARG", "DEU", "FRA", "USSDR"],
    )
    exp = dt.Datatable(
        data2,
        meta=metaDict2,
        columns=[2009, 2012, 2013, 2015],
        index=["ARG", "DEU", "FRA", "USSDR"],
    )
    # exp = exp.drop('UDSSR')
    exp = exp.drop(2015, axis=1)
    df2_clean = df2.clean()
    df2_clean == df2.clean()
    assert assert_frame_equal(df2_clean, exp) is None


def test_consistent_meta():
    df = dt.Datatable(
        data=np.asarray([[2.2, 3.4], [2.3, 3.4]]),
        meta={
            "source": "TEST",
            "entity": "Area",
            "category": "Forestery",
            "scenario": "Historic",
            "unit": "m",
        },
        columns=[2010, 2012],
        index=["ARG", "DEU"],
    )

    df.generateTableID()

    assert df.meta["variable"] == "Area|Forestery"
    assert df.meta["pathway"] == "Historic"

    # check removal of empty meta
    df.meta["category"] = np.nan
    df.meta["model"] = ""
    df.meta["description"] = ""
    df.generateTableID()

    assert "category" not in df.meta.keys()
    assert "model" not in df.meta.keys()
    assert "description" not in df.meta.keys()


def test_csv_write():
    df = dt.Datatable(
        data=np.asarray([[2.2, 3.4], [2.3, 3.4]]),
        meta={
            "source": "TEST",
            "entity": "Area",
            "category": "Forestery",
            "scenario": "Historic",
            "unit": "m",
        },
        columns=[2010, 2012],
        index=["ARG", "DEU"],
    )

    df.to_csv("temp.csv")

    fid = open("temp.csv")

    content = fid.readlines()

    fid.close()

    exp = [
        "### META ###\n",
        "ID,Area|Forestery__Historic__TEST\n",
        "_timeformat,%Y\n",
        "category,Forestery\n",
        "entity,Area\n",
        "pathway,Historic\n",
        "scenario,Historic\n",
        "source,TEST\n",
        "unit,m\n",
        "variable,Area|Forestery\n",
        "### DATA ###\n",
        "region,2010,2012\n",
        "ARG,2.2,3.4\n",
        "DEU,2.3,3.4\n",
    ]

    for obs_line, exp_line in zip(content, exp):
        assert obs_line == exp_line


def test_loss_less_csv_write_read():
    df = dt.Datatable(
        data=np.asarray([[2.2, 3.4], [2.3, 3.4]]),
        meta={
            "source": "TEST",
            "entity": "Area",
            "category": "Forestery",
            "scenario": "Historic",
            "unit": "m",
        },
        columns=[2010, 2012],
        index=["ARG", "DEU"],
    )

    df.to_csv("temp.csv")

    obs = dt.read_csv("temp.csv")

    # assert (df == obs).all()
    from pandas.testing import assert_frame_equal

    assert assert_frame_equal(df, obs) is None

    def test_loss_less_interpolate_reduce():
        from util import df, df2

        df = df.loc[:, df.columns.sort_values()]
        df_int = df.interpolate()
        df_obs = df_int.reduce()

        assert assert_frame_equal(df, df_obs) is None

        df2 = df2.loc[:, df2.columns.sort_values()]
        df_int = df2.interpolate()
        df_obs = df_int.reduce()

        assert assert_frame_equal(df2, df_obs) is None


def test_blow_index():
    df = df1.copy()

    mi_df = dt.indexing.blow_index(
        df, levels_to_add=["variable", "pathway", "source", "unit"]
    )

    assert all(
        [
            x in ["region", "source", "unit", "variable", "pathway"]
            for x in mi_df.index.names
        ]
    )


def test_slim_index():
    sectors = ["IPC0", "IPC1", "IPC2", "IPC1a", "IPC2a", "IPC1b", "IPC2b"]
    gases = ["Emissions|CO2"]
    test_df = pd.DataFrame(
        index=pd.MultiIndex.from_product(
            [sectors, gases], names=["sector", "variable"]
        ),
        data=1,
        columns=[2020, 2030],
    )

    slim_df = dt.indexing.slim_index(dt.Datatable(test_df))
    assert "Emissions|CO2" == slim_df.meta["variable"]


if __name__ == "__main__":
    test_creation()
    test_append()
    test_clean()
    test_consistent_meta()
    test_csv_write()
    test_loss_less_csv_write_read()
