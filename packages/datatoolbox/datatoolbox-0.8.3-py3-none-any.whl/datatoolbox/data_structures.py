#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic data structures that allow more efficient handling of year-country
based data sets.

Datatables are based on pandas dataframes and enfore regions as index
and years as columns. It uses meta data and provides full unit handling
by any computations using datatables.
"""

import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import xarray as xr

from copy import copy, deepcopy
import ast
from . import core
from . import indexing
from . import config
import traceback
from . import util
import os

# from . import tools
from . import converters
from time import time

pint = core.LazyLoader("pint", globals(), "pint")

# %% Functions


def interpolate(datatable, method="linear"):
    datatable = copy(datatable)

    if method == "linear":
        from scipy import interpolate
        import numpy as np

        if pd.api.types.is_datetime64_any_dtype(datatable.columns.dtype):
            xData = (
                datatable.columns.values.astype(int) // 10**9
            )  # timestamp in seconds
        elif pd.api.types.is_integer_dtype(
            datatable.columns.dtype
        ):  # assuming year as int
            xData = datatable.columns.values.astype(float)
        else:
            raise (
                BaseException(
                    "Expecting column dtype to be integer for years or datetime"
                )
            )

        yData = datatable.values
        for row in yData:
            idxNan = np.isnan(row)
            if sum(~idxNan) < 2:
                continue
            interpolator = interpolate.interp1d(
                xData[~idxNan], row[~idxNan], kind="linear"
            )
            col_idx = xData[idxNan].astype(int)
            col_idx = col_idx[col_idx > xData[~idxNan].min()]
            col_idx = col_idx[col_idx < xData[~idxNan].max()]
            new_idx = (
                idxNan & (xData > xData[~idxNan].min()) & (xData < xData[~idxNan].max())
            )
            row[new_idx] = interpolator(col_idx)
        return datatable
    else:
        raise (NotImplementedError())


def aggregate_region(table, mapping, skipna=False):
    table = copy(table)
    missingCountryDict = dict()

    for region in mapping.keys():
        missingCountries = set(mapping[region]) - set(table.index)
        #                print('missing countries: {}'.format(missingCountries))
        missingCountryDict[region] = list(missingCountries)
        availableCountries = set(mapping[region]).intersection(table.index)
        if len(availableCountries) > 0:
            table.loc[region, :] = table.loc[list(availableCountries), :].sum(
                axis=0, skipna=skipna
            )

    return table, missingCountryDict


def growth_rate(datatable):
    """
    Computes the growth rates for the given datatable
    """
    #    tempTable = copy(datatable)
    #    years = tempTable.columns
    #    completeYears = list(range(years.min() - periods, years.max()))
    #    for year in set(completeYears).difference(tempTable.columns):
    #        tempTable.loc[:,year] = np.nan
    #    tempTable =tempTable.loc[:,completeYears]
    #    growth_rates = tempTable.diff(axis=1,periods=periods).iloc[:,periods+1:] / tempTable.iloc[:,periods:-1].values
    #    growth_rates = growth_rates.loc[~growth_rates.isnull().all(axis=1),:]
    #    growth_rates = growth_rates.loc[:,~growth_rates.isnull().all(axis=0)]
    #
    #    return growth_rates

    # t0 = tempTable.loc[:,years[1:]]
    # t1 = tempTable.loc[:,[x-period for x in years if x-period in tempTable.columns]]
    tempTable = copy(datatable)
    growth_rates = tempTable.loc[:, tempTable.columns] * np.nan
    for i_year in range(1, len(tempTable.columns)):
        t0 = tempTable.columns[i_year - 1]
        t1 = tempTable.columns[i_year]

        diff = tempTable.loc[:, t1].values - tempTable.loc[:, t0].values
        growth_rate = diff / tempTable.loc[:, t0]
        growth_rates.loc[:, t1] = growth_rate
    return growth_rates


def composite_dataframe(tablePrioryList):
    newColumns = set()
    newIndex = set()
    for table in tablePrioryList:
        newColumns = newColumns.union(table.columns)
        newIndex = newIndex.union(table.index)

    newTable = Datatable(data=None, columns=newColumns, index=newIndex)

    metaCollection = dict()
    for table in tablePrioryList:
        newTable = newTable.combine_first(table)

        for key in table.meta.keys():
            if key not in metaCollection.keys():
                metaCollection[key] = set()

            metaCollection[key] = metaCollection[key].union([table.meta[key]])

    for key in metaCollection.keys():
        if len(metaCollection[key]) == 1:
            newTable.meta[key] = list(metaCollection[key])[0]
        else:
            newTable.meta[key] = "merged - meta quantity"
    return newTable


def to_XDataArray(tableSet, dimensions=["region", "time", "pathway"]):
    #    dimensions = ['region', 'time', 'scenario', 'model']

    #    metaDict = dict()

    dimSize, dimList = core.get_dimension_extend(tableSet, dimensions)
    metaCollection = core.get_meta_collection(tableSet, dimensions)

    xData = xr.DataArray(np.zeros(dimSize) * np.nan, coords=dimList, dims=dimensions)

    for table in tableSet:
        indexTuple = list()
        for dim in dimensions:
            if dim == "region":
                indexTuple.append(list(table.index))
            elif dim == "time":
                indexTuple.append(list(table.columns))
            else:
                indexTuple.append(table.meta[dim])

        #        xx = (table.index,table.columns,table.meta['pathway'])
        xData.loc[tuple(indexTuple)] = table.values

    # only implemented for homgeneous physical units
    assert len(metaCollection["unit"]) == 1
    xData.attrs["unit"] = list(metaCollection["unit"])[0]

    for metaKey, metaValue in metaCollection.items():
        if len(metaValue) == 1:
            xData.attrs[metaKey] = metaValue.pop()
        else:
            print("Warning, dropping meta data: " + metaKey + " " + str(metaValue))

    return xData


def to_XDataSet(tableSet, dimensions=["region", "time"]):
    """
    Convert datatoolbox tableSet to a xarray data set

    Parameters
    ----------
    tableSet : datatoolbox.Tableset
        DESCRIPTION.
    dimensions : list of str
        Full dimensions of the xarray array. Other remaining dimensions will be
        added as dict like elements.

    Returns
    -------
    dSet : xarray.Dataset
        DESCRIPTION.

    """
    dimSize, dimList = core.get_dimension_extend(tableSet, dimensions=dimensions)

    # dimensions= ['region', 'time']

    dSet = xr.Dataset(coords={key: val for (key, val) in zip(dimensions, dimList)})

    for key, table in tableSet.items():
        dSet[key] = table
        dSet[key].attrs = table.meta

    return dSet


def _get_unique_labels(table, dim):
    if isinstance(dim, tuple):
        unique_lables = [
            tuple(_get_unique_labels(table, sub_dim)[0] for sub_dim in dim)
        ]
        # unique_lables = [tuple(d for sub_dim in dim for d in _get_unique_labels(table, sub_dim))] # todo find better way
    elif dim == table.index.name:
        unique_lables = table.index
    elif dim == table.columns.name:
        unique_lables = table.columns
    elif dim in table.meta.keys():
        unique_lables = [table.meta[dim]]
    else:
        # raise(Exception(f'Dimension {dim} not available'))
        unique_lables = [np.nan]

    return unique_lables


def get_dimension_indices(table, dimensions):
    ind = list()
    for dim in dimensions:
        if isinstance(dim, tuple):
            index = [
                tuple(_get_unique_labels(table, sub_dim)[0] for sub_dim in dim)
            ]  # todo find better way
        elif dim == table.index.name:
            index = list(table.index)
        elif dim == table.columns.name:
            index = list(table.columns)
        elif dim in table.attrs.keys():
            index = [table.attrs[dim]]
        ind.append(index)

    return ind


def key_set_to_xdataset(
    dict_of_data,
    dimensions=["model", "scenario", "region", "time"],
    stacked_dims={"pathway": ("model", "scenario")},
):
    """
    Returns xarry dataset converted from a dict of pandas dataframes  or dt.TableSet. Differenty variables
    are stored as key variables. The xarray dimensions (coordiantes) are defined
    by the provided dimensions. A multi-index for a coordinate can be created
    by using stacked_dims.

    Usage:
    -------
    dimensions :  Iterable[str]]
        Dimensions of the shared yarray dimensions / coordinates
    stacked_dims : Dict[str]]
        Dictionary of all mutli-index coordinates and their sub-dimensions

    Returns
    -------
    matches : xarray.Dataset + pint quantification
    """

    dim_to_sort = "variable"
    sort_dict = dict()
    for key, table in dict_of_data.items():
        var = table.meta["variable"]

        if var in sort_dict.keys():
            sort_dict[var].append(table)
        else:
            sort_dict[var] = [table]

    variables = sort_dict.keys()

    data = list()
    for variable in variables:
        tables = sort_dict[variable]

        xarray = _to_xarray(tables, dimensions, stacked_dims)
        data.append(xr.Dataset({variable: xarray}))

    ds = xr.merge(data)

    return ds


def get_dimensions(table_iterable, dimensions):
    dims = dict()

    for table in table_iterable:
        for dim in dimensions:
            dims[dim] = dims.get(dim, set()).union(_get_unique_labels(table, dim))
    return dims


def _to_xarray(tables, dimensions, stacked_dims):
    """
    Return a database query result as an xarray . This constuctor allows only for
    one unit, since the full array is quantified using pint-xarray.
    The xarray dimensions (coordiantes) are defined
    by the provided dimensions. A multi-index for a coordinate can be created
    by using stacked_dims.

    Usage:
    -------
    tables : Iterable[[dt.Datatable]]
    dimensions :  Iterable[str]]
        Dimensions of the shared yarray dimensions / coordinates
    stacked_dims : Dict[str]]
        Dictionary of all mutli-index coordinates and their sub-dimensions

    Returns
    -------
    matches : xarray.Dataset + pint quantification
    """
    tt = time()
    metaCollection = core.get_meta_collection(tables, dimensions)
    if config.DEBUG:
        print(f"ime required for meta collection: {time()-tt:2.2f}s")

    tt = time()
    final_dims = dimensions.copy()
    xdims = dimensions.copy()
    for st_dim, sub_dims in stacked_dims.items():
        [xdims.remove(dim) for dim in sub_dims]
        xdims.append(sub_dims)

        [final_dims.remove(dim) for dim in sub_dims]
        final_dims.append(st_dim)

    dims = get_dimensions(tables, xdims)
    if config.DEBUG:
        print(dims)
    coords = {x: sorted(list(dims[x])) for x in dims.keys()}
    labels = dict()
    for st_dim, sub_dims in stacked_dims.items():
        coords[st_dim] = range(len(coords[sub_dims]))
        sub_labels = list()
        for i_dim, sub_dim in enumerate(sub_dims):
            sub_labels.append(
                pd.Index([x[i_dim] for x in coords[sub_dims]], name=sub_dim)
            )
        labels[st_dim] = pd.MultiIndex.from_arrays(sub_labels, names=sub_dims)
        del coords[sub_dims]

    dimSize = [len(labels) for dim, labels in dims.items()]

    if config.DEBUG:
        print(f"Get timension: {time()-tt:2.2f}s")

    tt = time()
    xData = xr.DataArray(np.zeros(dimSize) * np.nan, coords=coords, dims=final_dims)

    for key in labels.keys():
        mindex_coords = xr.Coordinates.from_pandas_multiindex(labels[key], key)
        xData = xData.assign_coords(mindex_coords)

    tt = time()
    for table in tables:
        ind = get_dimension_indices(table, xdims)
        # xData.loc[tuple(ind)] = table.values.reshape(len(table.index),len(table.columns),1)

        xData.loc[tuple(ind)] = table.values.reshape(*[len(x) for x in ind])
    if config.DEBUG:
        print(f"Time required for xr data filling: {time()-tt:2.2f}s")
    tt = time()
    metaCollection["unit"] = list(metaCollection["unit"])[0]
    xData = xData.pint.quantify(metaCollection["unit"])
    for key in labels.keys():
        mindex_coords = xr.Coordinates.from_pandas_multiindex(labels[key], key)
        xData = xData.assign_coords(mindex_coords)

    xData.attrs = metaCollection

    return xData


def load_as_xdataset(
    query_results,
    dimensions=["model", "scenario", "region", "time", "source"],
    stacked_dims={"pathway": ("model", "scenario")},
    native_regions=False,
):
    """
    Returns xarry dataset pruduced from a database result. Differenty variables
    are stored as key variables. The xarray dimensions (coordiantes) are defined
    by the provided dimensions. A multi-index for a coordinate can be created
    by using stacked_dims.

    Usage:
    -------
    dimensions :  Iterable[str]]
        Dimensions of the shared yarray dimensions / coordinates
    stacked_dims : Dict[str]]
        Dictionary of all mutli-index coordinates and their sub-dimensions
    native_regions : bool, optional
        Load native region defintions if available. The default is False.

    Returns
    -------
    matches : xarray.Dataset + pint quantification
    """

    variables = query_results.variable.unique()

    data = list()
    for variable in variables:
        tables = [
            core.DB.getTable(x, native_regions)
            for x in query_results.filterp(variable=variable).index
        ]

        xarray = _to_xarray(tables, dimensions, stacked_dims)
        data.append(xr.Dataset({variable: xarray}))

    ds = xr.merge(data)

    return ds


# %% Classes
class Datatable(pd.DataFrame):
    """
    Datatable


    Datatable is derrived from pandas dataframe.  Datatables contain the
    addition meta attribute and have autotmated unit conversions
    """

    _metadata = ["meta", "ID", "attrs"]

    # magicc methods
    def __init__(self, *args, **kwargs):
        # pop meta out of kwargs since pandas is not expecting it
        overwrite_meta = kwargs.pop(
            "meta", {}
        )  # return empty dict if no meta is provide

        super(Datatable, self).__init__(*args, **kwargs)

        if len(args) > 0 and hasattr(args[0], "meta"):
            # print(args)
            meta = args[0].meta

        elif "data" in kwargs.keys() and hasattr(kwargs["data"], "meta"):
            meta = kwargs["data"].meta

        else:
            meta = {}

        meta.update(overwrite_meta)

        # append metaDict to datatable
        self.__appendMetaData__(meta)

        try:
            self.generateTableID()
        except Exception:
            self.ID = None

        if config.AVAILABLE_XARRAY:
            self.to_xarray = self._to_xarray

        self.columns.name = config.DATATABLE_COLUMN_NAME
        self.index.name = config.DATATABLE_INDEX_NAME

        if ("_timeformat" in self.meta.keys()) and (
            self.meta["_timeformat"] != "%Y" and self.meta["_timeformat"] != "Y"
        ):
            self.columns_to_datetime()

        self.attrs = self.meta

    def __add__(self, other):
        """
        Private function to add two dataframes. The added table is converted to
        the unit of first table.

        Parameters
        ----------
        other : datatble
            Data to add.

        Returns
        -------
        out : datatable
            DESCRIPTION.

        """
        if isinstance(other, (Datatable, pint.Quantity)):
            if self.meta["unit"] == other.units:
                factor = 1
            else:
                factor = core.getUnit(other.units).to(self.meta["unit"]).m
            if isinstance(other, pint.Quantity):
                rhs = other.m
            else:
                rhs = pd.DataFrame(other * factor)
            out = Datatable(super(Datatable, self.copy()).__add__(rhs))

            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"

        # elif isinstance(ur(df1.meta['unit']),pint.Quantity):

        else:
            out = Datatable(super(Datatable, self).__add__(other))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        return out

    __radd__ = __add__

    def __finalize__(self, other, method=None, **kwargs):
        """propagate metadata from other to self"""
        # merge operation: using metadata of the left object
        if method == "merge":
            for name in self._metadata:
                object.__setattr__(self, name, copy(getattr(other.left, name, None)))
        # concat operation: using metadata of the first object
        elif method == "concat":
            for name in self._metadata:
                object.__setattr__(self, name, copy(getattr(other.objs[0], name, None)))
        else:
            for name in self._metadata:
                # print(other)
                object.__setattr__(self, name, copy(getattr(other, name, None)))
        return self

    def __appendMetaData__(self, metaDict):
        """
        Private function to append meta data.

        Parameters
        ----------
        metaDict : dict
            New meta data.


        """

        for metaKey in config.REQUIRED_META_FIELDS:
            if (
                metaKey not in metaDict.keys()
                or metaDict[metaKey] == ""
                or pd.isna(metaDict[metaKey])
            ):
                # Overwrite with default or empty string
                if metaKey in config.META_DEFAULTS:
                    metaDict[metaKey] = config.META_DEFAULTS[metaKey]
                else:
                    metaDict[metaKey] = ""

        self.__setattr__("meta", metaDict.copy())

        assert core.getUnit(self.meta["unit"])

    def __sub__(self, other):
        """
        Private function to subract two dataframes. The subracted table is converted to
        the unit of first table.

        Parameters
        ----------
        other : datatble
            Data to substract.

        Returns
        -------
        out : datatable
            DESCRIPTION.

        """
        if isinstance(other, (Datatable, pint.Quantity)):
            if self.meta["unit"] == other.units:
                factor = 1
            else:
                factor = core.getUnit(other.units).to(self.meta["unit"]).m
            if isinstance(other, pint.Quantity):
                rhs = other.m
            else:
                rhs = pd.DataFrame(other * factor)
            out = Datatable(super(Datatable, self).__sub__(rhs))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        else:
            out = Datatable(super(Datatable, self).__sub__(other))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        return out

    def __rsub__(self, other):
        """
        Equivalent to __sub__
        """
        if isinstance(other, (Datatable, pint.Quantity)):
            if self.meta["unit"] == other.units:
                factor = 1
            else:
                factor = core.getUnit(other.units).to(self.meta["unit"]).m
            if isinstance(other, pint.Quantity):
                other = other.m
            out = Datatable(super(Datatable, self).__rsub__(other * factor))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        else:
            out = Datatable(super(Datatable, self).__rsub__(other))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        return out

    def __mul__(self, other):
        if isinstance(other, (Datatable, pint.Quantity)):
            newUnit = core.getUnit(self.meta["unit"]) * core.getUnit(other.units)
            if isinstance(other, pint.Quantity):
                other = other.m
            out = Datatable(super(Datatable, self).__mul__(other))
            out.meta["unit"] = str(newUnit.u)
            out.meta["source"] = "calculation"
            out.values[:] *= newUnit.m
        else:
            out = Datatable(super(Datatable, self).__mul__(other))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        return out

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (Datatable, pint.Quantity)):
            newUnit = core.getUnit(self.meta["unit"]) / core.getUnit(other.units)
            if isinstance(other, pint.Quantity):
                other = other.m
            out = Datatable(super(Datatable, self).__truediv__(other))
            out.meta["unit"] = str(newUnit.u)
            out.meta["source"] = "calculation"
            out.values[:] *= newUnit.m
        else:
            out = Datatable(super(Datatable, self).__truediv__(other))
            out.meta["unit"] = self.meta["unit"]
            out.meta["source"] = "calculation"
        return out

    #    __rtruediv__ = __truediv__
    def __rtruediv__(self, other):
        if isinstance(other, (Datatable, pint.Quantity)):
            newUnit = core.getUnit(other.units) / core.getUnit(self.meta["unit"])
            if isinstance(other, pint.Quantity):
                other = other.m
            out = Datatable(super(Datatable, self).__rtruediv__(other))
            out.meta["unit"] = str(newUnit.u)
            out.meta["source"] = "calculation"
            out.values[:] *= newUnit.m
        else:
            out = Datatable(super(Datatable, self).__rtruediv__(other))
            out.meta["unit"] = str((core.getUnit(self.meta["unit"]) ** -1).u)
            out.meta["source"] = "calculation"
        return out

    def __repr__(self):
        outStr = """"""
        if "ID" in self.meta.keys():
            outStr += "=== Datatable - " + self.meta["ID"] + " ===\n"
        else:
            outStr += "=== Datatable ===\n"
        for key in self.meta.keys():
            if self.meta[key] is not None and not str(self.meta[key]).startswith("_"):
                outStr += key + ": " + str(self.meta[key]) + " \n"
        outStr += super(Datatable, self).__repr__()
        return outStr

    def _repr_html_(self):
        outStr = """"""
        if "ID" in self.meta.keys():
            outStr += "=== Datatable - " + self.meta["ID"] + " ===<br/>\n"
        else:
            outStr += "=== Datatable ===<br/>\n"
        for key in self.meta.keys():
            if self.meta[key] is not None and not str(self.meta[key]).startswith("_"):
                outStr += key + ": " + str(self.meta[key]) + " <br/>\n"
        outStr += super(Datatable, self)._repr_html_()
        return outStr

    # private methods
    @property
    def _constructor(self):
        return Datatable

    def _to_xarray(self):
        return core.xr.DataArray(
            self.values,
            coords=[self.index, self.columns],
            dims=["space", "time"],
            attrs=self.meta,
        )

    def _update_meta(self):
        self.meta = core._update_meta(self.meta)

    # public methods

    def add(self, other, **kwargs):
        table = Datatable(super(Datatable, self).add(other, **kwargs))

        table.meta.update(self.meta)
        return table

    def aggregate_region(self, mapping, skipna=False):
        """
        This functions added the aggregates to the table according to the provided
        mapping.( See datatools.mapp.regions)

        Returns the result, but does not inplace add it.
        """
        # from datatoolbox.tools.for_datatables import aggregate_region

        return aggregate_region(self, mapping, skipna)

    def append(self, other, **kwargs):
        """
        Append data to the datatable

        Parameters
        ----------
        other : datatable
            New data that will be added to the datatable.
        kwargs : TYPE
            Default pandas append arguments.

        Returns
        -------
        datatable

        """
        kwargs.setdefault("sort", True)

        if isinstance(other, Datatable):
            if other.meta["entity"] != self.meta["entity"]:
                #                print(other.meta['entity'] )
                #                print(self.meta['entity'])
                raise (BaseException("Physical entities do not match, please correct"))
            if other.units != self.meta["unit"]:
                other = other.convert(self.meta["unit"])

        out = pd.concat([self, other], **kwargs)

        # only copy required keys
        out.meta = {
            key: value
            for key, value in self.meta.items()
            if key in config.REQUIRED_META_FIELDS
        }

        # overwrite scenario
        out.meta["scenario"] = (
            "computed: " + self.meta["scenario"] + "+" + other.meta["scenario"]
        )
        return out

    def clean(self):
        """
        Clean up the dataframe to only recogniszed regions, years and numeric values.
        Removed columns and rows with only nan values.

        Returns
        -------
        datatable
            DESCRIPTION.

        """
        return util.cleanDataTable(self)

    def copy(self, deep=True):
        """
        Make a copy of this Datatable object Parameters

        ----------
        deep : boolean, default True
            Make a deep copy, i.e. also copy data
        Returns
        -------
            copy : Datatable
        """
        data = self._mgr
        if deep:
            data = data.copy(deep=True)
        return Datatable(data).__finalize__(self)

    def columns_to_datetime(self):
        self.columns = pd.to_datetime(self.columns, format=self.meta["_timeformat"])

    def diff(self, periods=1, axis=0):
        """
        Compute the difference between different years in the datatable
        Equivalent do pandas diff but return datatable.

        Parameters
        ----------
        periods : int, optional
            DESCRIPTION. The default is 1.
        axis : int, optional
            DESCRIPTION. The default is 0.

        Returns
        -------
        out : TYPE
            DESCRIPTION.

        """
        out = super(Datatable, self).diff(periods=periods, axis=axis)
        out.meta["unit"] = self.meta["unit"]

        return out

    @property
    def units(self):
        return self.meta["unit"]

    def info(self):
        """
        Returns information about the dataframe like shape, index and column
        extend and the number of non-nan entries.

        Returns
        -------
        str
            Information about datatable.

        """
        shp = self.shape
        if (len(self.index) == 0) or (len(self.columns) == 0):
            return "Empty Datatable"
        idx_ext = self.index[0], self.index[-1]
        time_ext = self.columns[0], self.columns[-1]
        n_entries = (~self.isnull()).sum().sum()
        return f"{shp[0]}x{shp[1]} Datatable with {n_entries} entries, index from {idx_ext[0]} to {idx_ext[1]} and time from {time_ext[0]} to {time_ext[0]}"

    @classmethod
    def from_multi_indexed_dataframe(cls, df):
        """
        Class function to create a datatable from a multi-indexed dataframe

        Parameters
        ----------
        df : multi index dataframe

        Returns
        -------
        table : Datatable

        """
        # find unique index
        idx_ames_to_meta = [
            x
            for x in df.index.names
            if (len(df.index.unique(x)) == 1) and x != "region"
        ]
        table = cls(df.copy())
        table.meta = {x: df.index.unique(x)[0] for x in idx_ames_to_meta}
        table.index = table.index.droplevel(idx_ames_to_meta)
        return table

    @classmethod
    def from_pyam(cls, idf, **kwargs):
        """
        Create a datatable from an iam dataframe.

        Parameters
        ----------
        cls : datatable class
            DESCRIPTION.
        idf : pyam dataframe
            dataframe that contrains the data that is used to create the datatable.
        kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        datatatble : datatoolbox datatable
            Datatable with original unit and related meta data.

        """
        import pyam

        if kwargs:
            idf = idf.filter(**kwargs)

        assert len(idf.variable) == 1, (
            f"Datatables cannot represent more than one variable, "
            f"but there are {', '.join(idf.variable)}"
        )

        def extract_unique_values(df, fields, ignore):
            meta = {}
            for fld in set(fields).difference(ignore):
                values = df[fld].unique()
                assert len(values) == 1, (
                    f"Datatables can only represent unique meta entries, "
                    f"but {fld} has {', '.join(values)}"
                )
                meta[fld] = values[0]
            return meta

        meta = {
            **extract_unique_values(idf.data, pyam.IAMC_IDX, ["region"]),
            **extract_unique_values(idf.meta, idf.meta.columns, ["exclude"]),
        }

        data = idf.data.pivot_table(
            index=["region"],
            columns=idf.time_col,
            aggfunc="sum",
        ).value.rename_axis(  # column name
            columns=None
        )

        return cls(data, meta=meta)

    @classmethod
    def from_excel(cls, filepath, sheetName=None):
        """
        Create a dataframe from a suitable excel file that is saved by datatoolbox.

        Parameters
        ----------
        cls : class

        filepath : str
            Path to the file.
        sheetName : str, optional
            Sheetn ame that is read in. The default is None.

        Returns
        -------
        datatable
            DESCRIPTION.
        """
        if sheetName is None:
            sheetNames = None
        else:
            sheetNames = [sheetNames]
        return read_excel(filepath, sheetNames=sheetNames)

    def reduce(self, method="linear_piece_wise", eps=1e-6):
        """
        Reduce data that is piecewise linear to the core data points (kinks).
        """

        # assert monotonic incease of decrease
        assert self.columns.is_monotonic

        # initial value of last year (set to first year)
        last_year = self.columns[0]
        last_yearly_change = np.nan  # initial value

        reduced_data = self.copy() * np.nan

        for year in self.columns[1:]:
            # assert year == last_year+1
            n_years = year - last_year

            change = self.loc[:, year] - self.loc[:, last_year]

            # find where is a kink
            idx = (change - last_yearly_change * n_years).abs() > eps

            reduced_data.loc[idx, last_year] = self.loc[idx, last_year]

            # overwrite last values
            last_yearly_change = change / n_years
            last_year = year

        # set first and last values
        for coISO in self.index:
            value_columns = self.columns[self.loc[coISO, :].notna()]
            idx_min = value_columns.min()
            idx_max = value_columns.max()
            reduced_data.loc[coISO, idx_min] = self.loc[coISO, idx_min]
            reduced_data.loc[coISO, idx_max] = self.loc[coISO, idx_max]

        return reduced_data

    def to_excel(self, fileName=None, sheetName="Sheet0", writer=None, append=False):
        """
        Save datatable to excel.

        Parameters
        ----------
        fileName : str, optional
            Relative file path. If None is provide, a writer is expected. The default is None.
        sheetName : str, optional
            Sheet name that is read in. The default is "Sheet0".
        writer : pandas excel writer, optional
            Pandas writer that is used instead opening a new one. The default is None.
        append : bool, optional
            If true, data is appended to the writer. The default is False.

        Returns
        -------
        None.

        """

        if fileName is not None:
            if append:
                writer = pd.ExcelWriter(
                    fileName,
                    engine="openpyxl",
                    mode="a",
                    datetime_format="mmm d yyyy hh:mm:ss",
                    date_format="mmmm dd yyyy",
                )
            else:
                writer = pd.ExcelWriter(
                    fileName,
                    engine="xlsxwriter",
                    datetime_format="mmm d yyyy hh:mm:ss",
                    date_format="mmmm dd yyyy",
                )

        metaSeries = pd.Series(
            data=[""] + list(self.meta.values()) + [""],
            index=["###META###"] + list(self.meta.keys()) + ["###DATA###"],
        )

        metaSeries.to_excel(writer, sheet_name=sheetName, header=None, columns=None)
        super(Datatable, self).to_excel(
            writer, sheet_name=sheetName, startrow=len(metaSeries)
        )

        if fileName is not None:
            writer.close()

    def to_csv(self, fileName=None):
        """
        Save the datatable to an annotated csv file.

        Parameters
        ----------
        fileName : str, optional
            Path to file. The default is None.

        Returns
        -------
        None.

        """
        if fileName is None:
            fileName = "|".join([self.meta[key] for key in config.ID_FIELDS]) + ".csv"
        else:
            assert fileName[-4:] == ".csv"

        core.csv_writer(fileName, pd.DataFrame(self), self.meta)

    def to_pyam(self, **kwargs):
        """
        Conversion to pyam dataframe.

        Parameters
        ----------
        kwargs : TYPE
            DESCRIPTION.

        Raises
        ------
        AssertionError
            DESCRIPTION.

        Returns
        -------
        idf : pyam dataframe
            DESCRIPTION.

        """
        from pyam import IamDataFrame

        meta = {**self.meta, **kwargs}

        try:
            idf = IamDataFrame(
                pd.DataFrame(self).rename_axis(index="region").reset_index(),
                model=meta.get("model", ""),
                scenario=meta["scenario"],
                variable=meta["variable"],
                unit=meta["unit"],
            )
        except KeyError as exc:
            raise AssertionError(f"meta does not contain {exc.args[0]}")

        # Add model, scenario meta fields
        for field in ("pathway", "source", "source_name", "source_year"):
            if field in meta:
                idf.set_meta(meta[field], field)

        return idf

    def to_IamDataFrame(self, **kwargs):
        """
        Function to sustain backwars compatibility
        Depreciated.

        """

        return self.to_pyam(**kwargs)

    def squeeze_index_to_attrs(self):
        """
        Does move all unique index  levels to attrs.

        Returns
        -------
        Datatable
            Datatable with only index levels that are non-unique. All other levels are in
            attrs.
            This operation can be reversed with table.to_multi_index_dataframe()

        """

        return indexing.slim_index(self)

    def to_multi_index_dataframe(
        self,
        meta_keys=None,
        exclude_meta=["ID", "creator", "source_name", "source_year", "_timeformat"],
    ):
        """
        Return a new datatable with a mult-index that has all meta data assigned

        Parameters
        ----------
            exclude_meta: optinal list of meta keys that should be ignored

        Returns
        -------
            Datatable
                New Datatable with multi_index and not meta data.

        """

        from pandas_indexing import assignlevel

        if meta_keys is None:
            meta_for_index = {
                x: self.meta[x]
                for x in sorted(self.meta.keys())
                if x not in exclude_meta
            }
        else:
            meta_for_index = {
                x: self.meta[x] for x in sorted(meta_keys) if x != "region"
            }

        return assignlevel(self.copy(), **meta_for_index)

    def convert(self, newUnit, context=None, suffix_dict=dict(), **new_meta):
        """
        Convert datatable to different unit and returns converted datatable.

        Parameters
        ----------
        newUnit : str
            New unit string in which the datatable should be converted.
        context : str, optional
            Optional context (e.g. GWPAR4). The default is None.

        Returns
        -------
        datatable
            Datatable converted in the new unit.

        """
        if self.meta["unit"] == newUnit:
            for key, suffix in suffix_dict.items():
                self.meta[key] = self.meta[key] + suffix
            self.meta.update(new_meta)
            return self

        dfNew = self.copy()

        factor = core.conversionFactor(self.meta["unit"], newUnit, context)

        dfNew.loc[:] = self.values * factor
        dfNew.meta["unit"] = newUnit
        dfNew.meta["modified"] = core.get_time_string()
        for key, suffix in suffix_dict.items():
            dfNew.meta[key] = dfNew.meta[key] + suffix
        dfNew.meta.update(new_meta)

        return dfNew

    def interpolate(self, method="linear", add_missing_years=False):
        """
        Interpoltate missing data between year with the option to add
        missing years in the columns.

        Parameters
        ----------
        method : sting, optional
            Interpolation method. The default is "linear".
            - linear
        add_missing_years : bool, optional
            If true, missing years within the time value range are added to
            the dataframe. The default is False.

        Returns
        -------
        datatable
            Interpolated dataframe.

        """
        # from datatoolbox.tools.for_datatables import interpolate

        if add_missing_years:
            for col in list(range(self.columns.min(), self.columns.max() + 1)):
                if col not in self.columns:
                    self.loc[:, col] = np.nan
            self = self.loc[:, list(range(self.columns.min(), self.columns.max() + 1))]

        return interpolate(self, method)

    def filter(self, spaceIDs):
        """
        Filter dataframe based on a list of spatial IDs.

        Parameters
        ----------
        spaceIDs : iterable of str
            DESCRIPTION.

        Returns
        -------
        datatable
            DESCRIPTION.

        """
        mask = self.index.isin(spaceIDs)
        return self.iloc[mask, :]

    def yearlyChange(self, forward=True):
        """
        :noindex:
        This methods returns the yearly change for all years (t1) that reported
        and and where the previous year (t0) is also reported

        Parameters
        ----------
        forward : bool
            If true, the yearly change is computed in the forward direction, otherwise
            backwards.
            Default is forward.

        """

        if forward:
            t0_years = self.columns[:-1]
            t1_years = self.columns[1:]
            index = self.index
            t1_data = self.iloc[:, 1:].values
            t0_data = self.iloc[:, :-1].values

            deltaData = Datatable(
                index=index,
                columns=t0_years,
                meta={key: self.meta[key] for key in config.REQUIRED_META_FIELDS},
            )
            deltaData.meta["entity"] = "delta_" + deltaData.meta["entity"]
            deltaData.loc[:, :] = t1_data - t0_data
        else:
            t1_years = self.columns[1:]
            index = self.index
            t1_data = self.iloc[:, 1:].values
            t0_data = self.iloc[:, :-1].values

            deltaData = Datatable(
                index=index,
                columns=t1_years,
                meta={key: self.meta[key] for key in config.REQUIRED_META_FIELDS},
            )
            deltaData.meta["entity"] = "delta_" + deltaData.meta["entity"]
            deltaData.loc[:, :] = t1_data - t0_data

        return deltaData

    def generateTableID(self):
        """
        Generates the table ID based on the meta data of the table.

        Returns
        -------
        datatable
            DESCRIPTION.

        """
        # update meta data required for the ID
        self.meta = core._update_meta(self.meta)
        self.ID = core._createDatabaseID(self.meta)
        self.meta["ID"] = self.ID
        return self.ID

    def getTableFilePath(self):
        """
        Returns path to data on hard disk

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        source = self.meta["source"]
        fileName = core.generate_table_file_name(self.ID)
        return os.path.join(
            config.PATH_TO_DATASHELF, "database/", source, "tables", fileName
        )

    def getTableFileName(self):
        """
        For compatibility to windows based sytems, the pipe symbols is replaces
        by double underscore for the csv filename.
        """
        self.generateTableID()

        return core.generate_table_file_name(self.ID)

    def source(self):
        """
        Return the source of the table
        """
        return self.meta["source"]


class TableSet(dict):
    """
    Class TableSet that is inherited from the dict class. It organized multiple
    heterogeneous datatbles into one structure.
    """

    def __init__(self, IDList=None):
        """
        Create tableset from a given list of table IDs. All tables are loaded from
        the database.

        Parameters
        ----------
        IDList : list, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        super(dict, self).__init__()
        self.inventory = pd.DataFrame(columns=["key"] + config.INVENTORY_FIELDS)

        if IDList is not None:
            for tableID in IDList:
                self.add(core.DB.getTable(tableID))

    def __getitem__(self, key):
        item = super(TableSet, self).__getitem__(key)

        # load datatable if necessary
        if item is None:
            item = core.DB.getTable(key)
            self[key] = item

        return item

    def __setitem__(self, key, datatable):
        super(TableSet, self).__setitem__(key, datatable)

        if datatable.ID is None:
            try:
                datatable.generateTableID()
            except Exception:
                #                print('Could not generate ID, key used instead')
                datatable.ID = key

        data = [key] + [datatable.meta.get(x, None) for x in config.INVENTORY_FIELDS]
        self.inventory.loc[datatable.ID] = data

    def __iter__(self):
        return iter(self.values())

    def _add_list(self, tableList):
        for table in tableList:
            tableID = table.generateTableID()

            if tableID in self.keys():
                self._update(table, tableID)
            else:
                self.__setitem__(tableID, table)

    def _add_TableSet(self, tableSet):
        for tableID, table in tableSet.items():
            if tableID in self.keys():
                self._update(table, tableID)
            else:
                self.__setitem__(tableID, table)

    def _add_single_table(self, table):
        tableID = table.generateTableID()
        if tableID in self.keys():
            self._update(table, tableID)
        else:
            self.__setitem__(tableID, table)

    def _add_tableID(self, tableID):
        self[tableID] = None
        self.inventory.loc[tableID] = [None for x in config.ID_FIELDS]

    def _update(self, table, tableKey):
        # make sure the data is compatible
        #        print(table.meta)
        #        print(self[tableKey].meta)
        if table.meta != self[tableKey].meta:
            raise (BaseException("Trying to update table with different meta"))

        # update data
        self[tableKey] = pd.concat([self[tableKey], table])

    def add(self, datatables=None, tableID=None):
        """
        Add new tables to table set. Either datatables or table IDs should be given.

        Parameters
        ----------
        datatables : list of datatables, optional
            DESCRIPTION. The default is None.
        tableID : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """

        # assert only on parameter is None
        assert not ((datatables is None) and (tableID is None))

        if datatables is not None:
            if isinstance(datatables, list):
                self._add_list(datatables)

            elif isinstance(datatables, TableSet):
                self._add_TableSet(datatables)

            elif isinstance(datatables, Datatable):
                self._add_single_table(datatables)

            else:
                print("Data type not recognized.")

        elif tableID is not None:
            self._add_tableID(tableID)

    def convert(self, newUnit):
        """
        Convert all tables to a new Unit. Returns a copy of the old tableSet

        Parameters
        ----------
        newUnit : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        tables = self.copy()

        for tableKey in tables.keys():
            tables[tableKey].convert(newUnit)
            tables[tableKey].meta["unit"] = newUnit
            tables.inventory.loc[tableKey, "unit"] = newUnit

        return tables

    def copy(self, deep=False):
        if deep:
            return deepcopy(self)
        else:
            return copy(self)

    def remove(self, tableID):
        """
        Remove table form tableSet.

        Parameters
        ----------
        tableID : str
            TableID.

        Returns
        -------
        None.

        """
        del self[tableID]
        self.inventory.drop(tableID, inplace=True)

    def filterp(self, level=None, regex=False, **filters):
        """
        Future defaulf find method that allows for more
        sophisticated syntax in the filtering

        Usage:
        -------
        filters : Union[str, Iterable[str]]
            One or multiple patterns, which are OR'd together
        regex : bool, optional
            Accept plain regex syntax instead of shell-style, default: False

        Returns
        -------
        matches : pd.Series
        Mask for selecting matched rows
        """

        # filter by columns and list of values
        keep = True

        for field, pattern in filters.items():
            # treat `col=None` as no filter applied
            if pattern is None:
                continue

            if field not in self.inventory:
                raise ValueError(f"filter by `{field}` not supported")

            keep &= util.pattern_match(self.inventory[field], pattern, regex=regex)

        if level is not None:
            keep &= self.inventory["variable"].str.count(r"\|") == level

        return self.inventory if keep is True else self.inventory.loc[keep]

    def filter(self, **kwargs):
        """
        Filter tableSet based on the given table inventory columns. (see config.INVENTORY_FIELDS)

        Parameters
        -------
        kwargs : dict-like
            Filter arguments as string that need to be contained in the fields.

        Returns
        -------
        newTableSet : tableSet
            DESCRIPTION.

        """
        inv = self.inventory.copy()
        for key in kwargs.keys():
            # table = table.loc[self.inventory[key] == kwargs[key]]
            mask = self.inventory[key].str.contains(kwargs[key], regex=False)
            mask[pd.isna(mask)] = False
            mask = mask.astype(bool)
            inv = inv.loc[mask].copy()

        newTableSet = TableSet()
        for key in inv.index:
            newTableSet[key] = self[key]

        return newTableSet

    @classmethod
    def from_converter(cls, data):
        return converters.to_tableset(data)

    @classmethod
    def from_list(cls, tableList):
        """
        Create tableSet form list of datatables.

        Parameters
        -------
        cls : TYPE
            DESCRIPTION.
        tableList : list
            List of datatables.

        Returns
        -------
        tableSet : tableset
            DESCRIPTION.

        """
        tableSet = cls()
        for table in tableList:
            tableSet.add(table)

        return tableSet

    def aggregate_to_region(self, mapping):
        """
        This functions added the aggregates to the output according to the provided
        mapping.( See datatools.mapp.regions)

        Returns the result, but does not inplace add it.
        """
        return util.aggregate_tableset_to_region(self, mapping)

    def to_compact_excel(
        self, writer, sheet_name="Sheet1", include_id=False, meta_columns=None
    ):
        """
        writes an excel file with a wide data format and a leadin meta header

        Parameters
        -------
        writer : TYPE
            DESCRIPTION.
        sheet_name : TYPE, optional
            DESCRIPTION. The default is "Sheet1".
        include_id : TYPE, optional
            DESCRIPTION. The default is False.
        meta_columns : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """

        use_index = include_id

        if isinstance(writer, pd.ExcelWriter):
            need_close = False
        else:
            writer = pd.ExcelWriter(pd.io.common.stringify_path(writer))
            need_close = True

        long, metaDict = self.to_compact_long_format(
            include_id, meta_columns=meta_columns
        )

        if meta_columns is not None:
            for metaKey in meta_columns:
                if metaKey not in long.columns:
                    long.loc[:, metaKey] = metaDict[metaKey]
            years = util.yearsColumnsOnly(long)
            long = long.loc[:, meta_columns + years]

        core.excel_writer(
            writer,
            long,
            metaDict,
            sheet_name=sheet_name,
            index=use_index,
            engine="xlsxwriter",
        )

        if need_close:
            writer.close()

    def to_excel(self, fileName, append=False, compact=False):
        """
        Sace TableSet as excel file with individual datatables in individual sheets.

        Parameters
        -------
        fileName : str
            File path.
        append : bool, optional
            If true, try to append data. The default is False.

        Returns
        -------
        None.

        """

        if append:
            writer = pd.ExcelWriter(
                fileName,
                engine="openpyxl",
                mode="a",
                datetime_format="mmm d yyyy hh:mm:ss",
                date_format="mmmm dd yyyy",
            )
        else:
            writer = pd.ExcelWriter(
                fileName,
                engine="xlsxwriter",
                datetime_format="mmm d yyyy hh:mm:ss",
                date_format="mmmm dd yyyy",
            )

        for i, eKey in enumerate(self.keys()):
            table = self[eKey].dropna(how="all", axis=1).dropna(how="all", axis=0)
            sheetName = str(i) + table.meta["ID"][:25]
            #            print(sheetName)
            table.to_excel(writer=writer, sheetName=sheetName)

        writer.close()

    def create_country_dataframes(self, countryList=None, timeIdxList=None):
        # using first table to get country list
        if countryList is None:
            countryList = self[list(self.keys())[0]].index

        coTables = dict()

        for country in countryList:
            coTables[country] = pd.DataFrame(
                [], columns=["entity", "unit", "source"] + list(range(1500, 2100))
            )

            for eKey in self.keys():
                table = self[eKey]
                if country in table.index:
                    coTables[country].loc[eKey, :] = table.loc[country]
                else:
                    coTables[country].loc[eKey, :] = np.nan
                coTables[country].loc[eKey, "source"] = table.meta["source"]
                coTables[country].loc[eKey, "unit"] = table.meta["unit"]

            coTables[country] = coTables[country].dropna(axis=1, how="all")

            if timeIdxList is not None:
                containedList = [
                    x for x in timeIdxList if x in coTables[country].columns
                ]
                coTables[country] = coTables[country][
                    ["source", "unit"] + containedList
                ]

        return coTables

    def variables(self):
        return list(self.inventory.variable.unique())

    def pathways(self):
        return list(self.inventory.pathway.unique())

    def entities(self):
        return list(self.inventory.entity.unique())

    def scenarios(self):
        return list(self.inventory.scenario.unique())

    def sources(self):
        return list(self.inventory.source.unique())

    def sum(self, new_meta={}):
        """
        This will sum up all tables in the tableSet if units do allow it. The user
        needs to make sure that the computation does make sense.

        If meta data is provided, the new table will be updated using this meta

        Returns
        -------
        resultTable : TYPE
            DESCRIPTION.

        """
        keyList = list(self.keys())

        # copy first element
        resultTable = self[keyList[0]].copy()

        # loop over remainen elements
        for key in keyList[1:]:
            resultTable = resultTable + self[key]

        # updating with new meta data if provided
        resultTable.meta.update(new_meta)

        return resultTable

    def get_all_meta_keys(self):
        meta_columns = set()
        for key in self.keys():
            meta = self[key].meta

            meta_columns = meta_columns.union(meta.keys())
        return list(meta_columns)

    def to_compact_long_format(self, include_id=False, meta_columns=None):
        if meta_columns is None:
            meta_columns = ["region"] + self.get_all_meta_keys()
        # meta_columns = ['region'] + config.INVENTORY_FIELDS
        if include_id:
            meta_columns.append("ID")

        long = self.to_LongTable(meta_list=meta_columns)

        single_meta = dict()
        multi_meta = list()
        columns_to_drop = list()

        for column in meta_columns:
            unique_entries = long.loc[:, column].unique()
            if len(unique_entries) == 1:
                if unique_entries[0] != "":
                    single_meta[column] = unique_entries[0]

                columns_to_drop.append(column)
            else:
                multi_meta.append(column)
        long = long.drop(columns_to_drop, axis=1)

        metaDict = dict()
        metaDict.update(single_meta)
        metaDict.update({"meta_columns": multi_meta})

        if include_id:
            long = long.set_index("ID")

        return long, metaDict

    def to_csv(self, filename):
        """
        Conversion to compact lone csv format

        Parameters
        ----------
        filename : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        long, metaDict = self._compact_to_long_format()

        core.csv_writer(filename, long, metaDict, index=None)

    def to_xarray(self, dimensions=None):
        """
        Convert tableset to and xarray with the given dimenions. Requires xarray installed

        Parameters
        ----------
        dimensions : list of str
            List of xarray dimensions.

        Returns
        -------
        xr.xarray
            DESCRIPTION.

        """
        if dimensions is None:
            dimensions = ["region", "time"]
            for col in config.ID_FIELDS + ["unit"]:
                if len(self.inventory.loc[:, col].unique()) > 1:
                    dimensions.append(col)

        if "unit" in dimensions:
            raise (
                BaseException(
                    "Different units in dataset can not be merged in one xarray"
                )
            )

        if not config.AVAILABLE_XARRAY:
            raise (BaseException("module xarray not available"))
        return to_XDataArray(self, dimensions)

    def to_xset(self, dimensions=["region", "time"]):
        """
        Convert table set to an xarray data set.

        Parameters
        ----------
        dimensions : list, optional
            DESCRIPTION. The default is ['region', 'time'].

        Returns
        -------
        xr.Dataset
            DESCRIPTION.

        """
        dimensions = ["region", "time"]
        if not config.AVAILABLE_XARRAY:
            raise (BaseException("module xarray not available"))
        return to_XDataSet(self, dimensions)

    def to_list(self):
        """
        Convert to list of tables

        Returns
        -------
        list
            List of datatables.

        """
        return [self[key] for key in self.keys()]

    def to_LongTable(
        self,
        native_regions=False,
        meta_list=["variable", "region", "scenario", "model", "unit"],
    ):
        tables = []

        for variable, df in self.items():
            if df.empty:
                continue
            inp_dict = dict()

            if isinstance(df.index, pd.MultiIndex):
                if native_regions:
                    df = df.reset_index("standard_region", drop=True)
                else:
                    df = df.reset_index("region", drop=True)

            for metaKey in meta_list:
                if metaKey == "region":
                    inp_dict[metaKey] = df.index
                else:
                    inp_dict[metaKey] = df.meta.get(metaKey, "")

            try:
                df = pd.DataFrame(df.assign(**inp_dict)).reset_index(drop=True)

            except KeyError as exc:
                raise AssertionError(
                    f"meta of {variable} does not contain {exc.args[0]}"
                )

            tables.append(df)

        long_df = pd.concat(tables, ignore_index=True, sort=False)

        # move id columns to the front
        id_cols = pd.Index(meta_list)
        long_df = long_df[list(id_cols) + list(long_df.columns.difference(id_cols))]
        long_df = pd.DataFrame(long_df)
        return long_df

    def to_pyam(self):
        import pyam

        long_table = self.copy(deep=True).to_LongTable()
        long_table.index.name = None

        # make sure that region does not contain any nan values
        na_mask = long_table["region"].isnull()
        if config.DEBUG and (sum(na_mask) > 0):
            print(f"Removing {sum(na_mask)} nan items in region index")
        long_table = long_table[~na_mask]

        idf = pyam.IamDataFrame(pd.DataFrame(long_table))

        meta = pd.DataFrame([df.meta for df in self.values()])
        if "model" not in meta:
            meta["model"] = ""
        if "scenario" not in meta:
            meta["scenario"] = ""
        meta = (
            meta[
                pd.Index(["model", "scenario", "pathway"]).append(
                    meta.columns[meta.columns.str.startswith("source")]
                )
            ]
            .set_index(["model", "scenario"])
            .drop_duplicates()
        )

        idf.meta = meta
        # idf.reset_exclude()

        return idf

    # Alias for backwards-compatibility
    to_IamDataFrame = to_pyam

    def plotAvailibility(self, regionList=None, years=None):
        avail = 0
        for table in self:
            #            print(table.ID)
            table.meta["unit"] = ""
            temp = avail * table
            temp.values[~pd.isnull(temp.values)] = 1
            temp.values[pd.isnull(temp.values)] = 0

            avail = avail + temp
        avail = avail / len(self)
        avail = util.cleanDataTable(avail)
        if regionList is not None:
            regionList = avail.index.intersection(regionList)
            avail = avail.loc[regionList, :]
        if years is not None:
            years = avail.columns.intersection(years)
            avail = avail.loc[:, years]

        plt.pcolor(avail)
        #        plt.clim([0,1])
        plt.colorbar()
        plt.yticks([x + 0.5 for x in range(len(avail.index))], avail.index)
        plt.xticks(
            [x + 0.5 for x in range(len(avail.columns))], avail.columns, rotation=45
        )


class DataSet(xr.Dataset):
    """
    Very simple class to allow initialization of xarray datasets from pyam, wide pandas dataframes
    and datatoolbox queries.
    """

    __slots__ = (
        "_attrs",
        "_cache",
        "_coord_names",
        "_dims",
        "_encoding",
        "_close",
        "_indexes",
        "_variables",
    )

    @classmethod
    def from_converter(cls, data):
        return converters.to_xdataset(data)

    @classmethod
    def from_wide_dataframe(
        cls, data, meta=None, stacked_dims={"pathway": ("model", "scenario")}
    ):
        to_merge = list()
        for (variable, unit), df_ in data.groupby(["variable", "unit"]):
            # print(df_)

            index = df_.index
            df_ = df_.reset_index(["variable", "unit"], drop=True)
            index, dims = _pack_dimensions(df_.index, **stacked_dims)
            da = (
                xr.DataArray(df_.set_axis(index).rename_axis(columns="year"))
                .unstack("dim_0")
                .pint.quantify(unit)
                .assign_coords(dims)
            )
            to_merge.append(xr.Dataset({variable: da}))
        self = xr.merge(to_merge)
        return self

    @classmethod
    def from_pyam(
        cls, data, meta_dims=None, stacked_dims={"pathway": ("model", "scenario")}
    ):
        if meta_dims is not None:
            meta = data.meta.loc[:, meta_dims]
            # data, stacked_dims = _add_meta(data, meta, stacked_dims)
        else:
            meta = None
        data = data.timeseries()
        if meta_dims is not None:
            data = _add_required_meta(data, meta, stacked_dims)

        return cls.from_wide_dataframe(data, meta, stacked_dims)

    @classmethod
    def from_query(cls, query, stacked_dims={"pathway": ("model", "scenario")}):
        # dimensions = ['model', 'scenario', 'region', 'variable', 'source', 'unit']
        # data = query.as_wide_dataframe(meta_list=dimensions)
        return load_as_xdataset(query, stacked_dims=stacked_dims)
        # return cls.from_wide_dataframe(data, meta=None, stacked_dims=stacked_dims)


class Visualization:
    """
    This class addes handy built-in visualizations to datatables
    """

    def __init__(self, df):
        self.df = df

    def availability(self, regions=None):
        if regions is not None:
            available_regions = self.df.index.intersection(regions)

            data = self.df.loc[available_regions, :]
        else:
            data = self.df

            availableRegions = data.index[~data.isnull().all(axis=1)]
        # print(availableRegions)
        plt.pcolormesh(data, cmap="RdYlGn_r")
        self._formatTimeCol()
        self._formatSpaceCol(data.index)
        return available_regions

    def _formatTimeCol(self):
        years = self.df.columns.values

        dt = int(len(years) / 10) + 1

        xTickts = np.array(range(0, len(years), dt))
        plt.xticks(xTickts + 0.5, years[xTickts], rotation=45)
        print(xTickts)

    def _formatSpaceCol(self, regions=None):
        if regions is None:
            locations = self.df.index.values
        else:
            locations = np.asarray(list(regions))

        # dt = int(len(locations) / 10)+1
        dt = 1
        yTickts = np.array(range(0, len(locations), dt))
        plt.yticks(yTickts + 0.5, locations[yTickts])

    def plot(self, **kwargs):
        if "ax" not in kwargs.keys():
            if "ID" in self.df.meta.keys():
                fig = plt.figure(self.df.meta["ID"])
            else:
                fig = plt.figure("unkown")
            ax = fig.add_subplot(111)
            kwargs["ax"] = ax
        self.df.T.plot(**kwargs)
        # print(kwargs['ax'])
        # super(Datatable, self.T).plot(ax=ax)
        kwargs["ax"].set_title(self.df.meta["entity"])
        kwargs["ax"].set_ylabel(self.df.meta["unit"])

    def html_line(self, fileName=None, paletteName="Category20", returnHandle=False):
        from bokeh.io import show
        from bokeh.plotting import figure
        from bokeh.resources import CDN
        from bokeh.models import ColumnDataSource
        from bokeh.embed import file_html
        from bokeh.embed import components
        from bokeh.palettes import all_palettes
        from bokeh.models import Legend

        tools_to_show = "box_zoom,save,hover,reset"
        plot = figure(
            plot_height=600,
            plot_width=900,
            toolbar_location="above",
            tools_to_show=tools_to_show,
            # "easy" tooltips in Bokeh 0.13.0 or newer
            tooltips=[("Name", "$name"), ("Aux", "@$name")],
        )
        # plot = figure()

        # source = ColumnDataSource(self)
        palette = all_palettes[paletteName][20]

        df = pd.DataFrame([], columns=["year"])
        df["year"] = self.df.columns
        for spatID in self.df.index:
            df.loc[:, spatID] = self.df.loc[spatID].values
            df.loc[:, spatID + "_y"] = self.df.loc[spatID].values

        source = ColumnDataSource(df)
        legend_it = list()
        import datatoolbox as dt

        for spatID, color in zip(self.df.index, palette):
            #            coName = mapp.countries.codes.name.loc[spatID]
            coName = dt.mapp.nameOfCountry(spatID)
            # plot.line(x=self.columns, y=self.loc[spatID], source=source, name=spatID)
            c = plot.line(
                "year",
                spatID + "_y",
                source=source,
                name=spatID,
                line_width=2,
                line_color=color,
            )
            legend_it.append((coName, [c]))
        plot.legend.click_policy = "hide"
        legend = Legend(items=legend_it, location=(0, 0))
        legend.click_policy = "hide"
        plot.add_layout(legend, "right")
        html = file_html(plot, CDN, "my plot")

        if returnHandle:
            return plot

        if fileName is None:
            show(plot)
        else:
            with open(fileName, "w") as f:
                f.write(html)

    def to_map(self, coList=None, year=None):
        # %%
        import matplotlib.pyplot as plt
        import cartopy.io.shapereader as shpreader
        import cartopy.crs as ccrs
        import matplotlib

        df = self.df
        if year is None:
            year = self.df.columns[-1]
        if coList is not None:
            df = df.loc[coList, year]
        cmap = matplotlib.cm.get_cmap("RdYlGn")

        #        rgba = cmap(0.5)
        norm = matplotlib.colors.Normalize(
            vmin=df.loc[:, year].min(), vmax=df.loc[:, year].max()
        )
        if "ID" in list(df.meta.keys()):
            fig = plt.figure(figsize=[8, 5], num=self.df.ID)
        else:
            fig = plt.figure(figsize=[8, 5])
        ax = plt.axes(projection=ccrs.PlateCarree())
        #        ax.add_feature(cartopy.feature.OCEAN)

        shpfilename = shpreader.natural_earth(
            resolution="110m", category="cultural", name="admin_0_countries"
        )
        reader = shpreader.Reader(shpfilename)
        countries = reader.records()

        for country in countries:
            if country.attributes["ISO_A3_EH"] in df.index:
                ax.add_geometries(
                    country.geometry,
                    ccrs.PlateCarree(),
                    color=cmap(norm(df.loc[country.attributes["ISO_A3_EH"], year])),
                    label=country.attributes["ISO_A3_EH"],
                    edgecolor="white",
                )
        #            else:
        #                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
        #                                  color = '#405484',
        #                                  label=country.attributes['ISO_A3_EH'])
        #        plt.title('Countries that accounted for 95% of coal emissions in 2016')

        ax2 = fig.add_axes([0.10, 0.05, 0.85, 0.05])
        #        norm = matplotlib.colors.Normalize(vmin=0,vmax=2)
        cb1 = matplotlib.colorbar.ColorbarBase(
            ax2, cmap=cmap, norm=norm, orientation="horizontal"
        )
        cb1.set_label(self.df.meta["unit"])
        plt.title(self.df.meta["entity"])
        plt.show()

    #        plt.colorbar()

    def html_scatter(self, fileName=None, paletteName="Category20", returnHandle=False):
        from bokeh.io import show
        from bokeh.plotting import figure
        from bokeh.resources import CDN
        from bokeh.models import ColumnDataSource
        from bokeh.embed import file_html
        from bokeh.embed import components
        from bokeh.palettes import all_palettes
        from bokeh.models import Legend

        tools_to_show = "box_zoom,save,hover,reset"
        plot = figure(
            plot_height=600,
            plot_width=900,
            toolbar_location="above",
            tools=tools_to_show,
            # "easy" tooltips in Bokeh 0.13.0 or newer
            tooltips=[("Name", "$name"), ("Aux", "@$name")],
        )
        # plot = figure()

        # source = ColumnDataSource(self)
        palette = all_palettes[paletteName][20]

        df = pd.DataFrame([], columns=["year"])
        df["year"] = self.df.columns

        for spatID in self.df.index:
            df.loc[:, spatID] = self.df.loc[spatID].values
            df.loc[:, spatID + "_y"] = self.df.loc[spatID].values

        source = ColumnDataSource(df)
        legend_it = list()
        import datatoolbox as dt

        for spatID, color in zip(self.df.index, palette):
            coName = dt.mapp.countries.codes.name.loc[spatID]
            # plot.line(x=self.columns, y=self.loc[spatID], source=source, name=spatID)
            c = plot.circle(
                "year", spatID + "_y", source=source, name=spatID, color=color
            )
            legend_it.append((coName, [c]))

        legend = Legend(items=legend_it, location=(0, 0))
        legend.click_policy = "hide"
        plot.add_layout(legend, "right")
        # p.circle(x, y, size=10, color='red', legend='circle')
        plot.legend.click_policy = "hide"
        html = file_html(plot, CDN, "my plot")

        if returnHandle:
            return plot
        if fileName is None:
            show(plot)
        else:
            with open(fileName, "w") as f:
                f.write(html)


def _try_number_format(x):
    try:
        return int(x)
    except Exception:
        try:
            return float(x)
        except Exception:
            return x


def read_csv(fileName, native_regions=False):
    """
    Load DataTable from csv file.

    Parameters
    ----------
    fileName : str
        Path of file.
    native_regions : bool, optional
            Load native region defintions if available. The default is False.


    Returns
    -------
    DataTable
        DataTable with data and meta.

    """

    fid = open(fileName, "r", encoding="UTF-8")

    assert (fid.readline()) == config.META_DECLARATION
    # print(nMetaData)

    meta = dict()
    while True:
        line = fid.readline()
        if line == config.DATA_DECLARATION:
            break
        try:
            key, val = line.replace("\n", "").split(",", maxsplit=1)
        except Exception:
            continue
        meta[key] = _try_number_format(val.strip())
        if "unit" not in meta.keys():
            meta["unit"] = ""

    if "timeformat" in meta.keys():
        meta["_timeformat"] = meta["timeformat"]
        del meta["timeformat"]
    # if meta['_timeformat'] == 'Y':
    #     meta['_timeformat'] = '%Y'
    # print(meta)

    df = pd.read_csv(fid)

    # fix for mutant pyam style files #TODO
    cols_to_keep = [x for x in df.columns if x not in meta.keys()]
    df = df.loc[:, cols_to_keep]

    if "standard_region" not in df.columns:
        # backward compatibility
        df = df.set_index(df.columns[0])
    else:
        # new datatable
        if native_regions:
            df = df.set_index(["region", "standard_region"])
            # if :
            # df = df.drop('standard_region',axis=1)
        else:
            df = df.set_index(["standard_region", "region"])
            df = df.reset_index("region", drop=True)
            df = df[~df.index.isnull()]
    fid.close()
    df = Datatable(df, meta=meta)

    if ("_timeformat" in meta.keys()) and (
        meta["_timeformat"] != "%Y" and meta["_timeformat"] != "Y"
    ):
        df.columns_to_datetime()
    else:
        df.columns = df.columns.astype(int)

    dupl_mask = df.index.duplicated()
    # removing duplicated entries that might results in different native and standart region definitions
    if sum(dupl_mask) > 0:
        if config.DEBUG:
            print(f"Removing duplicated {sum(dupl_mask)} entry(ies)")
        df = df.iloc[~dupl_mask, :]

    return df  # .drop_duplicates()


def read_excel(
    fileName, sheetNames=None, use_sheet_name_as_keys=False, force_tableSet=False
):
    if sheetNames is None:
        xlFile = pd.ExcelFile(fileName)
        sheetNames = xlFile.sheet_names
        xlFile.close()

    if len(sheetNames) > 1 or force_tableSet:
        out = TableSet()
        for sheet in sheetNames:
            fileContent = pd.read_excel(fileName, sheet_name=sheet, header=None)
            metaDict = dict()
            try:
                for idx in fileContent.index:
                    key, value = fileContent.loc[idx, [0, 1]]
                    if key == "###DATA###":
                        break

                    metaDict[key] = value
                columnIdx = idx + 1
                dataTable = Datatable(
                    data=fileContent.loc[columnIdx + 1 :, 1:].astype(float).values,
                    index=fileContent.loc[columnIdx + 1 :, 0],
                    columns=[int(x) for x in fileContent.loc[columnIdx, 1:]],
                    meta=metaDict,
                )

                if use_sheet_name_as_keys:
                    out[sheet] = dataTable
                else:
                    dataTable.generateTableID()
                    out.add(dataTable)

            except Exception:
                if config.DEBUG:
                    print(traceback.format_exc())
                print("Failed to read the sheet: {}".format(sheet))

    else:
        sheet = sheetNames[0]
        fileContent = pd.read_excel(fileName, sheet_name=sheet, header=None)
        metaDict = dict()
        if True:
            for idx in fileContent.index:
                key, value = fileContent.loc[idx, [0, 1]]
                if key == "###DATA###":
                    break

                metaDict[key] = value
            columnIdx = idx + 1
            dataTable = Datatable(
                data=fileContent.loc[columnIdx + 1 :, 1:].astype(float).values,
                index=fileContent.loc[columnIdx + 1 :, 0],
                columns=fileContent.loc[columnIdx, 1:],
                meta=metaDict,
            )
            if ("_timeformat" in dataTable.meta.keys()) and (
                dataTable.meta["_timeformat"] != "%Y"
            ):
                dataTable.columns_to_datetime()

            try:
                dataTable.generateTableID()
            except Exception:
                print("Warning: Meta data incomplete, table ID not generated")
            out = dataTable
    #        except Exception:
    #                print('Failed to read the sheet: {}'.format(sheet))

    return out


def read_compact_excel(file_name, sheet_name=None):
    """
    Reader that reads a wide data fromat excel with a leading meta header.

    Parameters
    ----------
    file_name : TYPE
        DESCRIPTION.
    sheet_name : TYPE, optional
        DESCRIPTION. The default is None.

    Raises
    ------

        DESCRIPTION.

    Returns
    -------
    out : TYPE
        DESCRIPTION.

    """
    # %%
    if sheet_name is None:
        xlFile = pd.ExcelFile(file_name)
        sheet_names = xlFile.sheet_names
        xlFile.close()

    out = TableSet()
    for sheet in sheet_names:
        fileContent = pd.read_excel(file_name, sheet_name=sheet, header=None)
        metaDict = dict()

        if fileContent.loc[0, 0] != "###META###":
            raise (BaseException("Undefined format"))

        # try:
        if True:
            for idx in fileContent.index[1:]:
                key, value = fileContent.loc[idx, [0, 1]]
                if key == "###DATA###":
                    break

                metaDict[key] = value
            columnIdx = idx + 1

            lDf = fileContent.loc[columnIdx + 1 :, :]
            lDf.columns = fileContent.loc[columnIdx, :]
            # lDf.index = fileContent.loc[columnIdx+1:, 0]

            if "ID" in metaDict["meta_columns"]:
                lDf.loc[:, "ID"] = fileContent.loc[columnIdx:, 0]

            try:
                meta_columns = ast.literal_eval(metaDict["meta_columns"])
            except Exception:
                meta_columns = metaDict["meta_columns"]
            if isinstance(meta_columns, str):
                meta_columns = meta_columns.split(", ")

            meta_columns.remove("region")

            for idx, line in lDf.iterrows():
                meta = {
                    x: metaDict[x] for x in metaDict.keys() if x not in ["meta_columns"]
                }

                for meta_col in meta_columns:
                    if meta_col in line.keys():
                        meta[meta_col] = line[meta_col]
                region = line.loc["region"]

                if "ID" in line.index:
                    ID = line.loc["ID"]
                else:
                    try:
                        meta = core._update_meta(meta)
                        ID = core._createDatabaseID(meta)
                    except Exception:
                        ID = config.ID_SEPARATOR.join(
                            [
                                meta[key]
                                for key in [
                                    x for x in config.ID_FIELDS if x in meta.keys()
                                ]
                            ]
                        )
                        print(
                            f"ID could not properly created, fallback to partial ID: {ID}"
                        )
                if config.DEBUG:
                    print(f"meta columns: {meta_columns}")
                    print(
                        f'numerical columns: {list(lDf.columns.difference(meta_columns + ["region"]))}'
                    )
                numerical_columns = list(
                    lDf.columns.difference(meta_columns + ["region"]).astype(int)
                )

                if ID not in out.keys():
                    table = Datatable(
                        columns=numerical_columns, index=[region], meta=meta
                    )

                    table.loc[region, numerical_columns] = line.loc[
                        numerical_columns
                    ].astype(float)
                    out[ID] = table

                else:
                    line.loc[numerical_columns].astype(float)
                    factor = core.conversionFactor(meta["unit"], out[ID].meta["unit"])
                    out[ID].loc[region, numerical_columns] = (
                        line.loc[numerical_columns].astype(float) * factor
                    )
                    #

    return out


# %%
class MetaData(dict):
    def __init__(self):
        super(MetaData, self).__init__()
        self.update({x: "" for x in config.REQUIRED_META_FIELDS})

    def __setitem__(self, key, value):
        super(MetaData, self).__setitem__(key, value)
        super(MetaData, self).__setitem__(
            "variable",
            "|".join(
                [self[key] for key in ["entity", "category"] if key in self.keys()]
            ),
        )
        super(MetaData, self).__setitem__(
            "pathway",
            "|".join(
                [self[key] for key in ["scenario", "model"] if key in self.keys()]
            ),
        )
        super(MetaData, self).__setitem__(
            "source",
            "_".join(
                [self[key] for key in ["institution", "year"] if key in self.keys()]
            ),
        )


# %% Test
def _add_required_meta(data, meta, stacked_dims):
    for key in stacked_dims.keys():
        dims_to_add = list()
        for dim in stacked_dims[key]:
            if dim in data.index.names:
                continue
            else:
                if dim in meta.columns:
                    dims_to_add.append(dim)
        data = data.join(meta.loc[:, dims_to_add])
        idx_names = set(data.index.names).union(dims_to_add)
        print(dims_to_add)
        print(idx_names)
        data = data.reset_index().set_index(list(idx_names))
        return data


def _add_meta(data, meta, stacked_dims):
    data = data.join(meta)

    stacked_dims.update({"meta": list(meta.columns)})
    idx_names = set(data.index.names).union(list(meta.columns))
    data = data.reset_index().set_index(list(idx_names))
    return data, stacked_dims


def _pack_dimensions(index, **stacked_dims):
    packed_labels = {}
    packed_values = {}
    drop_levels = []

    for dim, levels in stacked_dims.items():
        labels = pd.MultiIndex.from_arrays([index.get_level_values(x) for x in levels])
        packed_labels[dim] = labels_u = labels.unique()
        packed_values[dim] = pd.Index(labels_u.get_indexer(labels), name=dim)
        drop_levels.extend(levels)

    return (
        pd.MultiIndex.from_arrays(
            [index.get_level_values(x) for x in index.names.difference(drop_levels)]
            + list(packed_values.values())
        ),
        packed_labels,
    )


# def _pack_dimensions(index,
#                      meta = None,
#                      **stacked_dims):
#     packed_labels = {}
#     packed_values = {}
#     drop_levels = []

#     for dim, levels in stacked_dims.items():
#         labels = pd.MultiIndex.from_arrays([index.get_level_values(l) for l in levels])
#         packed_labels[dim] = labels_u = labels.unique()
#         packed_values[dim] = pd.Index(labels_u.get_indexer(labels), name=dim)
#         drop_levels.extend(levels)

#     #meta
#     if meta is not None:
#         for st_dim in stacked_dims.keys():
#             if st_dim in meta.columns:
#                 meta = meta.copy().drop(st_dim,axis= 1)
#         labels = pd.MultiIndex.from_arrays([index.get_level_values(l) for l in meta.index.names])
#         labels_u = labels.unique()
#         packed_values['meta'] = pd.Index(labels_u.get_indexer(labels), name='meta')
#         packed_labels['meta'] = pd.MultiIndex.from_arrays(meta.loc[labels_u,:].values.T, names = meta.columns)


#     return (
#         pd.MultiIndex.from_arrays(
#             [index.get_level_values(l) for l in index.names.difference(drop_levels)] +
#             list(packed_values.values())
#         ),
#         packed_labels
#     )


if __name__ == "__main__":
    meta = MetaData()
    meta["entity"] = "Emissions|CO2"
    meta["institution"] = "WDI"
    meta["year"] = "2020"
    # print(meta)
