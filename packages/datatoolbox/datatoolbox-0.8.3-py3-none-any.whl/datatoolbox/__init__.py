#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------- DATATOOLBOX -------------
This is a python tool box project for handling global datasets.
It contains the following features:

    Augumented pandas DataFrames adding meta data,
    Automatic unit conversion and table based computations
    ID based data structure
    Code templates (see templates.py)
    Package specific helper functions (see: tools/)

Authors: Andreas Geiges
         Jonas Hörsch
         Gaurav Ganti
         Matthew Giddens

"""

from . import version

__version__ = version.__version__
import time

all_tt = time.time()

import os

tt = time.time()
from . import config

print("Config initialised in {:2.4f} seconds".format(time.time() - tt))
tt = time.time()
from . import core

if config.DEBUG:
    print("Init of core in {:2.4f} seconds".format(time.time() - all_tt))


try:
    tt = time.time()
    from . import database

    if config.DEBUG:
        print("Database import in {:2.4f} seconds".format(time.time() - tt))

    core.DB = database.Database()
    db_connected = True
except Exception:
    import traceback

    print("Database connection broken. Running without database connection.")
    traceback.print_exc()
    db_connected = False


tt = time.time()
interfaces = core.LazyLoader("interfaces", globals(), "datatoolbox.interfaces")
# from . import interfaces

if config.DEBUG:
    print("Interfaces loaded in {:2.4f} seconds".format(time.time() - tt))

tt = time.time()
from . import util as util

if config.DEBUG:
    print("Utils loaded in {:2.4f} seconds".format(time.time() - tt))

from . import admin as admin

tt = time.time()
import pint

print("Utils loaded in {:2.4f} seconds".format(time.time() - tt))


# %% DATA STRUCTURES
tt3 = time.time()
from .data_structures import Datatable, TableSet, DataSet, read_csv

if config.DEBUG:
    print("Data structures loaded in {:2.4f} seconds".format(time.time() - tt3))

# %% IO

if config.DEBUG:
    print("IO loaded in {:2.4f} seconds".format(time.time() - tt))

# %% SETS
# Predefined sets for regions and scenrarios

from .sets import SCENARIOS, REGIONS, PATHWAYS

# %% indexing

from . import indexing as idx

# %% UNITS

units = core.unit_registry

# %% DATABASE
if db_connected:
    db = core.DB
    commitTable = core.DB.commitTable
    commitTables = core.DB.commitTables

    updateTable = core.DB.updateTable
    updateTables = core.DB.updateTables
    updateTablesAvailable = core.DB.updateTablesAvailable

    removeTable = core.DB.removeTable
    removeTables = core.DB.removeTables

    findc = core.DB.findc
    findp = core.DB.findp
    finde = core.DB.finde
    getTable = core.DB.getTable
    getTables = core.DB.getTables
    getTablesAvailable = core.DB.getTablesAvailable

    isAvailable = core.DB._tableExists

    updateExcelInput = core.DB.updateExcelInput

    sourceInfo = core.DB.sourceInfo
    inventory = core.DB.returnInventory

    validate_ID = core.DB.validate_ID
    # writeMAGICC6ScenFile = tools.wr

    # Source management
    import_new_source_from_remote = core.DB.importSourceFromRemote
    export_new_source_to_remote = core.DB.exportSourceToRemote
    remove_source = core.DB.removeSource
    push_source_to_remote = core.DB.push_source_to_remote
    pull_source_from_remote = core.DB.pull_update_from_remote

    # show available remote data sources
    remote_sourceInfo = core.DB.remote_sourceInfo
    available_remote_data_updates = core.DB.available_remote_data_updates
    test_ssh_remote_connection = core.DB.test_ssh_remote_connection
# %% TOOLS
# Tools related to packages
if config.DEBUG:
    tt = time.time()

tools = core.LazyLoader("tools", globals(), "datatoolbox.tools")


# insertDataIntoExcelFile = io.insertDataIntoExcelFile


# %% UNITS

conversionFactor = units.conversionFactor

# get country ISO code
getCountryISO = util.getCountryISO


# convenience functions
get_time_string = core.get_time_string
get_date_string = core.get_date_string


if db_connected:
    if config.PATH_TO_DATASHELF == os.path.join(
        config.MODULE_PATH, "data/SANDBOX_datashelf"
    ):
        print(
            """
              ################################################################
              You are using datatoolbox with a testing database as a SANDBOX.
              This allows for testing and initial tutorial use.
              
    
              For creating an empty dataase please use:
                  "datatoolbox.admin.create_empty_datashelf(pathToDatabase)"
    
              For switching to a existing database use: 
                  "datatoolbox.admin.change_personal_config()"
                  
                  
              ################################################################
              """
        )
else:
    print(
        """
          ################################################################
          
          You are using datatoolbox with no database connected
          
          Access functions and methods to database are not available.
              
          ################################################################
          """
    )


if config.DEBUG:
    print("Full datatoolbox init took {:2.4f} seconds".format(time.time() - all_tt))
