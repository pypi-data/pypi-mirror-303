#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:49:32 2024

@author: andreasgeiges
"""

import numpy as np
from datatoolbox import mapping as mapp
import pandas_indexing as pix

# %% import functionality from pandas_indexing
from pandas_indexing import isin, ismatch


def convert_idx_string_to_iso(index, iso_type="alpha3"):
    from datatoolbox.util import identifyCountry

    """
    Convert index of a dataframe into iso codes.

    Parameters
    ----------
    index : pandas.Index or similar
        Index of thos table consists of country strings.
    iso : TYPE, optional
        Either 'alpha3', alpha2 or numISO. The default is 'alpha3'.

    Returns
    -------
    insdex :  pandas.Index or 
        Return new iso index.

    """
    replaceDict = dict()

    for idx in index:
        iso = identifyCountry(idx)
        if iso is not None:
            replaceDict[idx] = iso
    iso_index = index.map(replaceDict)

    if iso_type == "alpha2":
        iso_index = mapp.countries.codes.loc[iso_index, "alpha2"]
    elif iso_type == "numISO":
        iso_index = mapp.countries.codes.loc[iso_index, "numISO"].astype(int)
    return iso_index


def slim_index(df):
    """
    Function to move all unique index levels to the meta of the dataframe

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe to squeeze.

    Returns
    -------
    df : pd.Dataframe
        resulting dataframe with squeezed index and filled meta.

    """

    levels_to_squeeze = [
        x.name
        for x in df.index.levels
        if len(pix.projectlevel(df.index, x.name).unique()) == 1
    ]
    level_values = [x[0] for x in df.index.levels if x.name in levels_to_squeeze]

    for level, value in zip(levels_to_squeeze, level_values):
        df.meta[level] = value

    df = df.droplevel(levels_to_squeeze)

    return df


def blow_index(df, levels_to_add=None):
    """
    Unsqueeze levels from meta into the (multi-index) of the dataframe.

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe with levels squeezed to meta.
    levels_to_add : list, optional
        Optional parameter to restrict the unsqueezed levels to the given list. The default is None.

    Returns
    -------
    df : pd.Dataframe
        resulting dataframe with unsqueezed meta.


    """

    # check that values are str
    idx_meta = {x: y for x, y in df.meta.items() if isinstance(y, (int, float, str))}

    if levels_to_add is not None:
        idx_meta = {x: y for x, y in idx_meta.items() if x in levels_to_add}
    df = pix.assignlevel(df, **idx_meta)

    return df


def year_indexes_only(index):
    """
    Extracts from any given index only the index list that can resemble
    as year

    e.g. 2001
    """

    import re

    REG_YEAR = re.compile("^[0-9]{4}$")

    newColumns = []
    for col in index:
        if REG_YEAR.search(str(col)) is not None:
            newColumns.append(col)
        else:
            try:
                if ~np.isnan(col) and REG_YEAR.search(str(int(col))) is not None:
                    #   test float string
                    newColumns.append(col)
            except Exception:
                pass
    return newColumns
