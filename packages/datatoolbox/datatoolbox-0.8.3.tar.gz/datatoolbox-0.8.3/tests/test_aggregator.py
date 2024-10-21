#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:04:10 2024

@author: andreasgeiges
"""

import pandas as pd
from datatoolbox import core

sectors = ["IPC0", "IPC1", "IPC2", "IPC1a", "IPC2a", "IPC1b", "IPC2b"]
gases = ["Emissions|CO2", "Emissions|CH4", "Emissions|N2O", "Emissions|F-Gases_AR4"]
test_df = pd.DataFrame(
    index=pd.MultiIndex.from_product([sectors, gases], names=["sector", "variable"]),
    data=1,
    columns=[2020, 2030],
)


def test_agg_print():
    agg = core.Aggregator()
    agg.add_relations(relations={"IPC1": ["IPC1a", "IPC1b"]})

    print(agg.tree)


def test_aggregator_sector():
    # expected a list of susequent aggregation mappings
    exp = [
        {"IPC1": ["IPC1a", "IPC1b"]},
        {"IPC2": ["IPC2a", "IPC2b"]},
        {"IPC0": ["IPC1", "IPC2"]},
    ]

    agg = core.Aggregator()
    agg.add_relations(relations={"IPC1": ["IPC1a", "IPC1b"]})

    agg.add_relations(relations={"IPC0": ["IPC1", "IPC2"]})
    agg.add_relations(relations={"IPC2": ["IPC2a", "IPC2b"]})
    # agg.add_relations(relations = {'IPC2a': ['IPC2_transport', 'IPC2_aviation']})
    # agg.add_relations(relations = {'IPC2_aviation': ['IPC2_aviation_national', 'IPC2_aviation_international']})

    agg.bottom_up_aggregations() == exp


def test_aggregator_gases():
    exp = [
        {
            "Emissions|Kyoto_Gases_AR4": [
                "Emissions|CO2",
                "Emissions|CH4",
                "Emissions|N2O",
                "Emissions|F-Gases_AR4",
            ]
        }
    ]
    agg = core.Aggregator()
    agg.add_relations(
        {
            "Emissions|Kyoto_Gases_AR4": [
                "Emissions|CO2",
                "Emissions|CH4",
                "Emissions|N2O",
                "Emissions|F-Gases_AR4",
            ]
        }
    )
    agg.bottom_up_aggregations() == exp
