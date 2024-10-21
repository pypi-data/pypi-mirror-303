#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:58:27 2019

@author: Andreas Geiges
"""
import re
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
#import deprecated as dp
#import numpy as np

#from . import config

#from . import core
#from . import util
#from . import mapping as mapp
#from .tools.pandas import yearsColumnsOnly



from .data_structures import Datatable, TableSet
from openpyxl import load_workbook

REQUIRED_SETUP_FIELDS = [
    'filePath',
    'fileName',
    'sheetName',
    'timeIdxList',
    'spaceIdxList',
]

SP_ARG = 3
TI_ARG = 2
DT_ARG = 4

#from datatoolbox.tools.excel import Excel_Reader

#%% Functions

def yearsColumnsOnly(index):
    """
    Extracts from any given index only the index list that can resemble
    as year

    e.g. 2001
    """

    import re

    REG_YEAR = re.compile('^[0-9]{4}$')

    newColumns = []
    for col in index:
        if REG_YEAR.search(str(col)) is not None:
            newColumns.append(col)
        else:
            try:
                if ~np.isnan(col) and REG_YEAR.search(str(int(col))) is not None:
                    #   test float string
                    newColumns.append(col)
            except:
                pass
    return newColumns
#from .tools import excel as _xls

# excel_to_pandas_idx = _xls.excel_to_pandas_idx
# getAllSheetNames = _xls.getAllSheetNames


def read_MAGICC6_MATLAB_bulkout(pathName):

    temp_offset = 0.61
    df = pd.read_table(
        pathName, skiprows=23, header=0, delim_whitespace=True, index_col=0
    )
    df = df + temp_offset
    df.index = df.index.astype(int)
    return df
    # df.values[df.values<0] = np.nan


#
#    meta = dict()
#    meta['entity'] = 'global_temp'
#    meta['unit']   = '°C'
#    return Datatable(df, meta=meta)


def read_MAGICC6_BINOUT(filePath):
    import pymagicc as pym

    reader = pym.io._BinaryOutReader(filePath)

    metaData, df = reader.read()

    data = df.pivot(index='region', columns='time', values='value')

    metaDict = dict()
    metaDict['entity'] = df.variable[0]
    metaDict['source'] = 'MAGICC6_calculation'
    metaDict['unit'] = None

    return Datatable(data, meta=metaDict)


def read_PRIMAP_csv(fileName):

    metaMapping = {
        'entity': 'SHEET_ENTITY',
        'unit': 'SHEET_UNIT',
        'category': 'SHEET_NAME_CATEGORY',
        'scenario': 'SHEET_SCENARIO',
        'model': 'SHEET_SOURCE',
    }

    allDf = pd.read_csv(fileName, usecols=[0, 1], index_col=0)
    # print(os.path.basename(fileName))

    firstDataRow = allDf.loc['SHEET_FIRSTDATAROW', 'Unnamed: 1']

    # bugfix of old wrong formated PRIMAP files
    try:
        int(firstDataRow)
    except:
        firstDataRow = np.where(allDf.index == "Countries\Years")[0][0] + 3

    firstMetaRow = np.where(allDf.index == "&SHEET_SPECIFICATIONS")[0][0] + 1

    metaPrimap = dict()
    for row in range(firstMetaRow, firstDataRow):
        key = allDf.index[row]
        value = allDf.iloc[row, 0]
        if key == '/':
            break
        metaPrimap[key] = value

    data = pd.read_csv(fileName, header=firstDataRow - 2, index_col=0)

    meta = dict()
    for metaKey in metaMapping:

        if isinstance(metaMapping[metaKey], list):
            value = '_'.join(metaPrimap[x] for x in metaMapping[metaKey])
        else:
            value = metaPrimap[metaMapping[metaKey]]
        meta[metaKey] = value

    table = Datatable(data, meta=meta)
    table = table.loc[:, yearsColumnsOnly(table)]
    table.columns = table.columns.astype(int)
    return table  # , data


def read_PRIMAP_Excel(fileName, sheet_names=None, sheet_name=None, xlsFile=None):

    # single sheet reading
    if (sheet_names is None) and (sheet_name is not None):
        return _read_PRIMAP_Excel_single(fileName, sheet_name, xlsFile)

    # single sheet reading
    if isinstance(sheet_names, str):
        return _read_PRIMAP_Excel_single(fileName, sheet_names, xlsFile)

    if sheet_names is None:
        sheet_names = getAllSheetNames(fileName)

    out = TableSet()
    if xlsFile is None:
        xlsFile = pd.ExcelFile(fileName)
    for sheet_name in tqdm(sheet_names):
        table = _read_PRIMAP_Excel_single(fileName, sheet_name, xlsFile=xlsFile)
        out[sheet_name] = table

    return out


def _read_PRIMAP_Excel_single(fileName, sheet_name=0, xlsFile=None):
    if xlsFile is None:
        xlsFile = pd.ExcelFile(fileName)
    allDf = pd.read_excel(xlsFile, sheet_name=sheet_name, usecols=[0, 1], index_col=0)
    # print(os.path.basename(fileName))

    firstDataRow = allDf.loc['SHEET_FIRSTDATAROW', 'Unnamed: 1']

    # bugfix of old wrong formated PRIMAP files
    try:
        int(firstDataRow)
    except:
        firstDataRow = np.where(allDf.index == "Countries\Years")[0][0] + 3

    # print(firstDataRow)
    setup = dict()
    setup['filePath'] = os.path.dirname(fileName) + '/'
    setup['fileName'] = os.path.basename(fileName)
    setup['sheetName'] = sheet_name
    setup['timeIdxList'] = ('B' + str(firstDataRow - 1), 'XX' + str(firstDataRow - 1))
    setup['spaceIdxList'] = ('A' + str(firstDataRow), 'A1000')
    # print(setup)
    ex = ExcelReader(setup, xlsFile=xlsFile)
    data = ex.gatherData().astype(float)
    # return data
    meta = {
        'source': '',
        'entity': allDf.loc['SHEET_ENTITY', 'Unnamed: 1'],
        'unit': allDf.loc['SHEET_UNIT', 'Unnamed: 1'],
        'category': allDf.loc['SHEET_NAME_CATEGORY', 'Unnamed: 1'],
        'scenario': allDf.loc['SHEET_SCENARIO', 'Unnamed: 1']
        + '|'
        + allDf.loc['SHEET_SOURCE', 'Unnamed: 1'],
    }
    REG_ton = re.compile('^[GM]t')
    xx = REG_ton.search(meta['unit'])

    if xx:
        meta['unit'] = meta['unit'].replace(xx.group(0), xx.group(0) + ' ')

    table = Datatable(data, meta=meta)
    try:
        table = table.loc[:, yearsColumnsOnly(table)]
        table.columns = table.columns.astype(int)
    #        table = table.loc[:,yearsColumnsOnly(table)]
    except:
        print('warning: Columns could not be converted to int')
    return table


def read_MAGICC6_ScenFile(fileName, **kwargs):
    
    from . import greenhouse_gas_database as gh

    GHG_data = gh.GreenhouseGasTable()
    VALID_MASS_UNITS = {
        'Pt': 1e18,
        'Gt': 1e15,
        'Mt': 1e12,
        'kt': 1e9,
        't': 1e6,
        'Pg': 1e15,
        'Tg': 1e12,
        'Gg': 1e9,
        'Mg': 1e6,
        'kg': 1e3,
        'g': 1,
    }
    fid = open(fileName, 'r')
    nDataRows = int(fid.readline().replace('/n', ''))

    while True:
        # for i, line in enumerate(fid.readlines()):
        line = fid.readline()
        if line[:11] == '{0: >11}'.format('YEARS'):
            break
    # get first header line
    entities = line.split()[1:]

    # reading units
    unitLine = fid.readline().split()[1:]
    # print(unitLine)

    # find correct component
    components = [GHG_data.findEntryIdx(entity) for entity in entities]

    units = [unit for unit in unitLine if unit[:2] in VALID_MASS_UNITS]

    replacementDict = {'MtN2O-N': 'Mt N'}

    units = [replacementDict.get(unit, unit) for unit in units]

    columns = [(x, y, z) for x, y, z in zip(entities, components, units)]
    entityFrame = pd.DataFrame(columns=entities)
    entityFrame.columns = pd.MultiIndex.from_tuples(columns)

    entityFrame.columns.names = ['NAME', 'COMP', 'UNIT']

    for i, line in enumerate(fid.readlines()):

        if i == nDataRows:
            break
        data = line.split()
        entityFrame.loc[int(data[0])] = np.asarray(data[1:])

    # TODO: CHange to a results list of datatables
    return entityFrame


def insertDataIntoExcelFile(
    fileName, overwrite=False, setupSheet='INPUT', interpolate=False
):
    ins = _xls.ExcelWriter(
        fileName=fileName,
        overwrite=overwrite,
        setupSheet=setupSheet,
        interpolate=interpolate,
    )
    ins.insert_data()
    ins.close()
    return ins

def getAllSheetNames(filePath):
    """
    Retrive all sheetnames of the given excel file path.


    Parameters
    ----------
    filePath : str
        Path of excel file to get sheet names.

    Returns
    -------
    sheetNameList : list of str


    """
    xlFile = pd.ExcelFile(filePath)
    sheetNameList = xlFile.sheet_names
    xlFile.close()
    return sheetNameList


#%%
#%%


def PandasExcelWriter(fileName):
    return pd.ExcelWriter(
        fileName,
        engine='xlsxwriter',
        datetime_format='mmm d yyyy hh:mm:ss',
        date_format='mmmm dd yyyy',
    )


#%%


