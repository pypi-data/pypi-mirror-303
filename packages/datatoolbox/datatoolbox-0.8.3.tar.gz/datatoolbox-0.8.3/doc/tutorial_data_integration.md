

# 1) Tutorial -  Basic integration of raw data

## Install additional packages
```bash
pip install panda_datareader
```
##   Downloading raw data using data reader
As first step we download an example dataset from the World Bank.

```
from pandas_datareader import wb
matches = wb.search('gdp.*capita.*const')

data_df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX', 'DE'], start=2005, end=2024)


matches2 = wb.search('emission')
emission_data = wb.download(indicator='CC.CO2.EMSE.EN', country=['US', 'CA', 'MX', 'DE'], start=2005, end=2024)
population_data = wb.download(indicator='SP.POP.TOTL', country=['US', 'CA', 'MX', 'DE'], start=2005, end=2024)

population_data = wb.download(indicator=['SP.POP.TOTL','CC.CO2.EMSE.EN'], country=['US', 'CA', 'MX', 'DE'], start=2005, end=2024)


```

## Data transformation

In order to integrate the raw data into datatoolbox, the raw structure must be adapted to the following requirements:
- ISO3  code for country as index
- years or  timestampe as  columns
- additional meta data describing the variable, scenario and source of the data

dt.Datatable takes as arguments a pandas dataframe and meta the meta data

```
dt.Datatable(data=pandas_df, meta  = meta_dict)
````



Exercise: convert the  data to required format
```

















--- scroll below for solution  --- 


```


### Solution 

```
import datatoolbox as dt
from pandas_datareader import wb
matches = wb.search('gdp.*capita.*const')

data_df = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX', 'DE'], start=2005, end=2024)



#assuming the correct meta data
meta = {'variable' : 'GDP_per_capita',
        'scenario' : 'Historic',
        'source' : 'WORLDBANK_2024',
        'unit' : 'USD/count'}
wide_df = data_df.reset_index().pivot(index='country', columns='year', values='NY.GDP.PCAP.KD')
  
        
        
gdp_table = dt.Datatable(data=wide_df,
                     meta=meta)
gdp_table.index = dt.idx.convert_idx_string_to_iso(gdp_table.index)

final_table = gdp_table                     

```    


## Commit data as datatoolbox source


Excercise - Create and commit data as new sources
1) create the meta data dictionary for the new source
2) use the function add_table or dt.add_tables to database
3) verfiy that table is in database

```
# switch to testing database
dt.admin.switch_database_to_testing(force_new_DB=True)

# meta data for new source
source_dict =  {
    'SOURCE_ID': '',
    'collected_by': '',
    'date': dt.core.get_date_string(),
    'source_url': '',
    'licence': '',
}

# add your code here






```

### Solution 


```
dt.admin.switch_database_to_testing(force_new_DB=True)

# meta data for new source
source_dict =  {
    'SOURCE_ID': 'WORLDBANK_2024',
    'collected_by': 'MM',
    'date': dt.core.get_date_string(),
    'source_url': 'https://datatopics.worldbank.org/world-development-indicators/',
    'licence': 'open_source',
}
dt.commitTable(final_table, message = 'adding first table', sourceMetaDict = source_dict)


#verify that table is in inventory
dt.findp(source='WORLDBANK*')
```

### What happend  in the back ground
From the meta data, datatoolbox create  a table ID that conains  the variable,  scenario and source.  
This  ID should be unique within your database and is used to directly access the data, e.g. via 
dt.getTable
```
print(final_table.meta['ID'])

table_reloaded =  dt.getTable('GDP_per_capita__Historic__WORLDBANK_2024')
```