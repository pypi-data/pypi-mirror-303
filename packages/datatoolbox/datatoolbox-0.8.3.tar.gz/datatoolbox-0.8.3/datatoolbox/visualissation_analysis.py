#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:54:19 2024

@author: andreasgeiges
"""
import matplotlib.pyplot as plt
import datatoolbox as dt

def scatterIndicatorComparison(tableX, tableY):
    timeCol = list(set(tableY.columns).intersection(set(tableX.columns)))
    for ISOcode in tableX.index:
        coName = dt.mapping.countries.codes.name.loc[ISOcode]

        plt.scatter(
            tableX.loc[ISOcode, timeCol], tableY.loc[ISOcode, timeCol], s=100
        )

        plt.text(
            tableX.loc[ISOcode, timeCol] + 0.1,
            tableY.loc[ISOcode, timeCol] + 0.2,
            coName,
        )
    plt.xlabel(tableX.ID)
    plt.ylabel(tableY.ID)

    plt.xlim([0, 60])
    plt.ylim([0, 20])
    plt.tight_layout()