# Internal code structure

## config.py
Main configuration for datatoolbox for costomisation. It contains the required
meta data fields and how the table ID are constructed. It also includes the format
of the meta-data-aware csv data file format. Finally, the url of the shared
multi-user git prepository is set here.
 
## data_structures.py
This file contains the central data code class of the "Datatable" and ofther test
classes. Here the major functionality of Datatables is implemented.

## database.py
This file hoste the two main classes that form the database functionality. The class
Database does provide the user interface to add, remove, alter and read data from the database. 
The class "GitRepository_Manager" does contain the hidden layer for all version controling using
git and enables to create, update and share data sets (sources).

## core.py
This code part contains many central classes that are note related to data. The main important
one being the unit_registry. Can be accessed via dt.units or dt.core.unit_registry and allows 
fast and secure unit conversion for any SI units and the largest extend of emission-related units. 
It also contains a LazyLoader (taken from tensorflow) to allow full loading of modelus only if required 
by the user.
Finally it contains a new aggregator class that allows to create tree-like aggregation rules.

## indexing.py
This new container aims to bundle all index-related functionality of datatoolbox that allow to
alter, map or filter index like objects. It also presents some core functionality from 
pandas_indexing for easy access. 

## mapping.py
This more old code provide many old and current regional mappings that are used in the context
of climate science and Integrated Assessment Models.




