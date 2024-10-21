##!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core contains some very basic functions that are used within the package
in various locations and tools.

@author: Andreas Geiges
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

tt = time.time()

import re
import numpy as np
import pandas as pd

from . import config

from . import naming_convention

pix_tt = time.time()
import pandas_indexing as pix

if config.DEBUG:
    print("└-- pandas indexing import in {:2.4f} seconds".format(time.time() - pix_tt))

# import pint

from copy import copy
from treelib import Tree as _Tree

import importlib
import types


if config.DEBUG:
    print("└-- Core import in {:2.4f} seconds".format(time.time() - tt))


"""A LazyLoader class."""


class LazyLoader(types.ModuleType):
    """Lazily import a module, mainly to avoid pulling in large dependencies.

    This code is mainly taken form https://github.com/tensorflow/tensorflow/blob/v2.5.0/tensorflow/python/util/lazy_loader.py
    and slightly addapted.
    """

    # The lint error here is incorrect.
    def __init__(self, local_name, parent_module_globals, name, warning=None):
        self._local_name = local_name
        self._parent_module_globals = parent_module_globals
        self._warning = warning

        super(LazyLoader, self).__init__(name)

    def _load(self):
        """Load the module and insert it into the parent's globals."""
        # Import the target module and insert it into the parent's namespace
        module = importlib.import_module(self.__name__)
        self._parent_module_globals[self._local_name] = module

        # Emit a warning if one was specified
        if self._warning:
            # logging.warning(self._warning)
            # Make sure to only warn once.
            self._warning = None

        # Update this object's dict so that if someone keeps a reference to the
        #   LazyLoader, lookups are efficient (__getattr__ is only called on lookups
        #   that fail).
        self.__dict__.update(module.__dict__)

        return module

    def __getattr__(self, item):
        module = self._load()
        return getattr(module, item)

    def __call__(self, *args):
        module = self._load()
        return module.__call__(*args)

    def __dir__(self):
        module = self._load()
        return dir(module)


# %% Unit registry
tt_pint = time.time()


class Unit_Registry:
    """
    Pint unit registry using openscm units with additional convenience functionality

    """

    def __init__(self):
        pass

    def __getattribute__(self, name):
        if name == "ur" not in self.__dict__:
            import pint
            from datatoolbox import config
            from openscm_units import unit_registry as ur

            # Pint unit handling

            gases = {
                "CO2eq": "carbon_dioxide_equivalent",
                # "CO2e": "CO2eq",
                "NO2": "NO2",
                "PM25": "PM25",
            }

            # self.ur = self_ur

            try:
                ur._add_gases(gases)

                ur.define("fraction = [] = frac")
                ur.define("percent = 1e-2 frac = pct")
                ur.define("sqkm = km * km")
                ur.define("none = dimensionless")

                ur.load_definitions(config.PATH_PINT_DEFINITIONS)
                ur.define("CO2eq = CO2")
            except pint.errors.DefinitionSyntaxError:
                # avoid double import of units defintions
                pass
            self.ur = ur

        return super().__getattribute__(name)

    def is_valid_unit(self, unit_str):
        ur = self.ur
        try:
            ur(unit_str)
            return True
        except Exception:
            return False

    def getUnit(self, unit_like, ur=None):
        """
        Return the pint unit for a given unit string. Compared to the original
        pint this functions replaces special characters $ € and % by a string
        reprentation.

        Parameters
        ----------
        unit_like : str or Unit
            unit string (e.g. "km / s" or "€  / capita")

        Returns
        -------
        unit : pint unit
        """

        if ur is None:
            ur = self.ur

        import pint

        # if not isinstance(string, str):
        #     string = str(string)
        # capture if already is pint unit
        if isinstance(unit_like, pint.Unit):
            unit_like = str(unit_like)
        elif isinstance(unit_like, pint.Quantity):
            unit_like = str(unit_like.u)

        if unit_like is None:
            unit_like = ""
        else:
            unit_like = (
                unit_like.replace("$", "USD")
                .replace("€", "EUR")
                .replace("%", "percent")
            )
        return ur(unit_like)

    def conversionFactor(self, unitFrom, unitTo, context=None):
        """
        Return the conversion factor from one unit to another.

        Parameters
        ----------
        unitFrom : str
            Original unit to convert.
        unitTo : str
            Unit to which it original unit should be converted.
        context : str, optional
            For some conversions, a specifice context is needed. Currently, only
            GWPAR4 is implemented. The default is None.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """

        if context == "GWPAR4":
            import warnings

            warnings.warn(
                'The context "AR4GWP" is depricated. Pleases use "AR4GWP100" instead'
            )
            context = "AR4GWP100"
        if context is None:
            return self.getUnit(unitFrom).to(self.getUnit(unitTo)).m

        else:
            with self.ur.context(context) as urc:
                factor = self.getUnit(unitFrom, ur=urc).to(self.getUnit(unitTo, ur=urc))

            return factor.m


unit_registry = Unit_Registry()
# = LazyLoader("unit_registry", globals(), "datatoolbox.unit_registry")

if config.DEBUG:
    print(
        "└-- pint unit handling initialised in core in {:2.4f} seconds".format(
            time.time() - tt_pint
        )
    )


# %% Aggregator class
class Aggregator:
    """
    This class is used to support aggregation of data according a constructed
    hierachical tree.
    The tree is constructe by added multiple mapping dictionaries with overlapping
    leaves.
    """

    def __init__(self):
        self.tree = None

        class bc:
            HEADER = "\033[95m"
            OKBLUE = "\033[94m"
            OKCYAN = "\033[96m"
            OKGREEN = "\033[92m"
            WARNING = "\033[93m"
            FAIL = "\033[91m"
            ENDC = "\033[0m"
            BOLD = "\033[1m"
            UNDERLINE = "\033[4m"

    def __str__(self):
        return self.tree.__str__()

    def _dict2tree(self, relation: dict):
        trees = list()
        for source, target in relation.items():
            tree = _Tree()
            root = tree.create_node(source, source)

            if isinstance(target, list):
                for target_node in target:
                    tree.create_node(target_node, target_node, parent=root)

            else:
                tree.create_node(target, target, parent=root)

            trees.append(tree)

        return trees

    def _add2tree(self, tree2add):
        if self.tree is None:
            self.tree = tree2add

        else:
            # check if root in existing tree

            if tree2add.root in self.tree:
                # new tree is child of existing tree

                for node in tree2add.children(tree2add.root):
                    sub_tree = tree2add.subtree(node.tag)
                    self.tree.paste(tree2add.root, sub_tree)

            elif self.tree.root in tree2add:
                # new tree is parent of existing tree

                old_tree = copy(self.tree)

                self.tree = tree2add

                for node in old_tree.children(old_tree.root):
                    sub_tree = old_tree.subtree(node.tag)
                    self.tree.paste(old_tree.root, sub_tree)

            else:
                raise (Exception("No connecting node found"))

    def add_relations(self, relations: dict):
        """
        Add mappings to existing tree


        Parameters
        ----------
        relations : dict
            mapping.

        Returns
        -------
        None.

        """
        trees = self._dict2tree(relations)

        for tree in trees:
            self._add2tree(tree)

    def _leave_to_dict(self, nid, mappings):
        self.tree.subtree(nid).to_dict()

        subtree = self.tree.children(nid)
        if len(subtree) > 0:
            mapping = {nid: []}
            for node in self.tree.children(nid):
                self._leave_to_dict(node.identifier, mappings)
                mapping[nid].append(node.identifier)

            mappings.append(mapping)
            return mappings

        else:
            return mappings

    def bottom_up_aggregations(self):
        """
        Generation of sequential mapping dictionaries for bottom up aggregation
        according to tree

        Returns
        -------
        mappings : TYPE
            DESCRIPTION.

        """

        root = self.tree.root

        mappings = list()

        self._leave_to_dict(root, mappings)

        return mappings

    # def show_availability_data(self, wdf, index_name):
    #     #%%
    #     wdf = all_data.copy().loc[pix.isin(entity='Emissions|CO2', region='POL')]

    #     string_lines = self.__str__()
    #     new_string_lines = list()
    #     for line in string_lines.split('\n'):
    #         sel_str = line.split('──')[-1].strip()
    #         data = wdf.loc[pix.isin(**{index_name: sel_str})]

    #         if len(data) == 0 or (data.isnull().all(axis=1).all()):
    #             new_string_lines.append(colored_string(line, color='r'))
    #         elif data.isnull().any(axis=1).any():
    #             new_string_lines.append(colored_string(line, color='y'))

    #         else:
    #             new_string_lines.append(colored_string(line, color='g'))

    #     new_string_lines = '\n'.join(new_string_lines)
    #     print(new_string_lines)


LOG = dict()
LOG["tableIDs"] = list()


# %% Functions


def is_known_entity(variable):
    for entity in naming_convention.entities:
        if variable.startswith(entity):
            return True

    return False


def _split_variable(metaDict):
    """
    Split variable into a known entity (see naming_converntion.py) and a
    category.

    Parameters
    ----------
    metaDict : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    # Find entity
    entity_matches = list()
    for entity in naming_convention.entities:
        if metaDict["variable"].startswith(entity):
            entity_matches.append(entity)

    if len(entity_matches) > 0:
        longest_matchg = max(entity_matches, key=len)
        metaDict["entity"] = longest_matchg

    else:
        if config.DEBUG:
            print(f'Warning: Entity could not be derived from {metaDict["variable"]}')

        # exit here
        return metaDict

    # derive or check category
    if "category" not in metaDict.keys():
        metaDict["category"] = (
            metaDict["variable"].replace(longest_matchg, "").strip("|")
        )
    else:
        if metaDict["category"] != metaDict["variable"].replace(
            longest_matchg, ""
        ).strip("|"):
            print(
                "Warming current category not fitting derived category, please review"
            )
    return metaDict


def _update_meta(metaDict):
    """
    Private funcion to update the meta data of a datatable


    Parameters
    ----------
    metaDict : dict
        new data to overwrite.

    Returns
    -------
    metaDict : dict

    """
    if "entity" not in metaDict.keys():
        metaDict = _split_variable(metaDict)

    for key in list(metaDict.keys()):
        if (metaDict[key] is np.nan) or metaDict[key] == "":
            if key != "unit":
                del metaDict[key]

    for id_field in config.ID_FIELDS:
        fieldList = [
            metaDict[key]
            for key in config.SUB_FIELDS[id_field]
            if key in metaDict.keys()
        ]
        if len(fieldList) > 0:
            new_value = (
                config.SUB_SEP[id_field].join([str(x) for x in fieldList]).strip("|")
            )
            if (
                config.DEBUG
                and id_field in metaDict.keys()
                and metaDict[id_field] != new_value
            ):
                print(
                    f"Warning: {id_field} will be overritten {metaDict[id_field]} -> {new_value}"
                )
            metaDict[id_field] = new_value

    return metaDict


def _fix_filename(name, max_length=255):
    """
    Replace invalid characters on Linux/Windows/MacOS with underscores.
    List from https://stackoverflow.com/a/31976060/819417
    Trailing spaces & periods are ignored on Windows.
    >>> fix_filename("  COM1  ")
    '_ COM1 _'
    >>> fix_filename("COM10")
    'COM10'
    >>> fix_filename("COM1,")
    'COM1,'
    >>> fix_filename("COM1.txt")
    '_.txt'
    >>> all('_' == fix_filename(chr(i)) for i in list(range(32)))
    True
    """
    return re.sub(
        r'[/\\:<>"?*\0-\x1f]|^(AUX|COM[1-9]|CON|LPT[1-9]|NUL|PRN)(?![^.])|^\s|[\s.]$',
        "_",
        name[:max_length],
        flags=re.IGNORECASE,
    )


def _validate_unit(table):
    """
    Testinf using pint if unit can be applied. Return False if error occured

    Parameters
    ----------
    table : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        is valid.

    """
    try:
        getUnit(table.meta["unit"])

        return True
    except Exception:
        return False


def generate_table_file_name(ID):
    """
    Generate table ID using the meta data and separators given in the config

    Parameters
    ----------
    ID : TYPE
        DESCRIPTION.

    Returns
    -------
    str
        ID

    """
    ID_for_filename = _fix_filename(ID)
    ID_for_filename = ID.replace("|", "-").replace("/", "-")
    return ID_for_filename + ".csv"


def _createDatabaseID(metaDict):
    ID = config.ID_SEPARATOR.join([metaDict[key] for key in config.ID_FIELDS])
    # ID = _fix_filename(ID)
    return ID


def csv_writer(filename, dataframe, meta, index=0):
    """
    wrapper to write csv file with head to contain meta data

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.
    dataframe : TYPE
        DESCRIPTION.
    meta : TYPE
        DESCRIPTION.
    index : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    fid = open(filename, "w", encoding="utf-8")
    fid.write(config.META_DECLARATION)

    for key, value in sorted(meta.items()):
        #            if key == 'unit':
        #                value = str(value.u)
        fid.write(key + "," + str(value) + "\n")

    fid.write(config.DATA_DECLARATION)
    if index == 0:
        dataframe.to_csv(fid, sep=",")
    elif index is None:
        dataframe.to_csv(fid, index=None, sep=";")
    fid.close()


def excel_writer(
    writer, dataframe, meta, sheet_name="Sheet1", index=False, engine=None
):
    """
    Excel writer to include head of meta data before the csv like data block.

    """
    if isinstance(writer, pd.ExcelWriter):
        need_save = False
    else:
        writer = pd.ExcelWriter(pd.io.common.stringify_path(writer), engine=engine)
        need_save = True

    metaSeries = pd.Series(
        data=[""] + list(meta.values()) + [""],
        index=["###META###"] + list(meta.keys()) + ["###DATA###"],
    )

    metaSeries.to_excel(writer, sheet_name=sheet_name, header=None, columns=None)
    pd.DataFrame(dataframe).to_excel(
        writer, sheet_name=sheet_name, index=index, startrow=len(metaSeries)
    )

    if need_save:
        writer.save()


def osIsWindows():
    """
    Checkes if operating system is windows based


    Returns
    -------
    bool

    """
    if (config.OS == "win32") | (config.OS == "Windows"):
        return True
    else:
        return False


def is_validt_unit(unit):
    """
    Function to test if unit string is a valid unit

    Parameters
    ----------
    unit : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    try:
        getUnit(unit)
    except Exception:
        return False
    else:
        return True


def getUnit(string, ur=None):
    """
    Return the pint unit for a given unit string. Compared to the original
    pint this functions replaces special characters $ € and % by a string
    reprentation.

    Parameters
    ----------
    string : str
        unit string (e.g. "km / s" or "€  / capita")

    Returns
    -------
    unit : pint unit
    """
    if ur is None:
        ur = unit_registry.ur
    import pint

    # if not isinstance(string, str):
    #     string = str(string)
    # capture if already is pint unit
    if isinstance(string, pint.Unit):
        string = str(string)
    if string is None:
        string = ""
    else:
        string = string.replace("$", "USD").replace("€", "EUR").replace("%", "percent")
    return ur(string)


def getUnitWindows(string):
    """
    Equivalent version of getUnit  but adapted for windows system.

    Parameters
    ----------
    string : str
        unit string (e.g. "km / s" or "€  / capita")

    Returns
    -------
    unit : pint unit

    """
    if string is None:
        string = ""
    else:
        string = (
            string.replace("$", "USD")
            .replace("€", "EUR")
            .replace("%", "percent")
            .replace("Â", "")
        )
    return unit_registry.ur(string)


def get_time_string():
    """
    Return formated time string.

    Returns
    -------
    time string : str

    """
    return time.strftime("%Y/%m/%d-%I:%M:%S")


def get_date_string():
    """
    Return formated date string.

    Returns
    -------
    date string : str

    """
    return time.strftime("%Y_%m_%d")


def conversionFactor(unitFrom, unitTo, context=None):
    """
    Return the conversion factor from one unit to another.

    Parameters
    ----------
    unitFrom : str
        Original unit to convert.
    unitTo : str
        Unit to which it original unit should be converted.
    context : str, optional
        For some conversions, a specifice context is needed. Currently, only
        GWPAR4 is implemented. The default is None.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """

    if context == "GWPAR4":
        import warnings

        warnings.warn(
            'The context "AR4GWP" is depricated. Pleases use "AR4GWP100" instead'
        )
        context = "AR4GWP100"
    if context is None:
        return getUnit(unitFrom).to(getUnit(unitTo)).m

    else:
        with unit_registry.ur.context(context) as urc:
            factor = getUnit(unitFrom, ur=urc).to(getUnit(unitTo, ur=urc))

        return factor.m


def _findGases(string, candidateList):
    hits = list()
    for key in candidateList:
        if key in string:
            hits.append(key)
            string = string.replace(key, "")
    return hits


def get_dimension_extend(table_iterable, dimensions):
    """
    This functions assesses the the unique extend for various dimensions
    given a set of datatables
    """
    fullIdx = dict()
    # for dim in dimensions:
    #     fullIdx[dim] = set()

    for table in table_iterable:
        #        for metaKey, metaValue in table.meta.items():
        #            if metaKey not in metaDict.keys():
        #                metaDict[metaKey] = set([metaValue])
        #            else:
        #                metaDict[metaKey].add(metaValue)

        for dim in dimensions:
            if dim not in fullIdx.keys():
                fullIdx[dim] = set()

            if dim == "region":
                fullIdx[dim] = fullIdx[dim].union(table.index)
            elif dim == "time":
                fullIdx[dim] = fullIdx[dim].union(table.columns)
            elif dim in table.meta.keys():
                fullIdx[dim].add(table.meta[dim])
            else:
                raise (BaseException("Dimension not available"))

    dimSize = [len(fullIdx[x]) for x in dimensions]
    dimList = [sorted(list(fullIdx[x])) for x in dimensions]

    return dimSize, dimList


def get_meta_collection(table_iterable, dimensions):
    """

    Parameters
    ----------
    table_iterable : list of tables
        DESCRIPTION.
    dimensions : list of dimentions
        DESCRIPTION.

    Returns
    -------
    metaCollection : TYPE
        DESCRIPTION.

    """

    metaCollection = dict()
    for table in table_iterable:
        for key in table.meta.keys():
            if key in dimensions or key == "ID":
                continue
            if key not in metaCollection.keys():
                metaCollection[key] = set()

            metaCollection[key].add(table.meta[key])

    return metaCollection


# re-defintion of getUnit function for windows users
if osIsWindows():
    getUnit = getUnitWindows

if config.DEBUG:
    print("core loaded in {:2.4f} seconds".format(time.time() - tt))
