# CrossTech-Py-Tools

Commonly used python functions and interfaces for CrossTech python development. If you are a _developer_ of this library check out [this documentation](docs/dev.md).

- [📥 Install](#install)
  - [pip](#pip)
  - [poetry](#poetry)
- [🏭 Modules](#modules)
  - [☁️ Cloud Funcs](#cloud-funcs)
  - [💽 Database](#database)
  - [🗺️ Location](#location)
  - [🚂 Mileage](#mileage)
  - [👷 ELRs](#elrs)

## Install

To install the library use the commands provided below.

### pip:
```shell
pip install crosstech-py-tools
```

### poetry:
```shell
poetry add crosstech-py-tools
```

> [!WARNING]
> When trying to add this library to an existing project using poetry, be aware that it is reliant on a large number of dependencies, meaning adding it will require some labour to sort out any conflicts. Hence, it is recommended to start your project by adding this library **first**.

## Modules

### Cloud Funcs

[☁️ Cloud Funcs documentation.](docs/cloud_funcs.md) This module focuses on simplifying the process of testing cloud functions by simulated calls in-code. It provides a wrapper `make_request` around Flask call, which removes the boilerplate code needed to call the cloud function normally.

```python
from crosstech.clound_funcs import make_request
```

### Database

[💽 Database documentation.](docs/database.md) This module provides a database interface that is proven to work in cloud functions. The `BaseDB` object can be used in an inheritance relationship or be injected into a function. Either way, this will save time on setting up the boilerplate necessary to connect to the database.

```python
from crosstech.database import BaseDB
```

### Location

[🗺️ Location documentation.](docs/location.md) This module contains an array of tools useful for analysing and manipulating location data. 

The `explore` function can take in geopandas GeoDataFrames and plot them all on a single map. The `LocTools` object helps with converiting between shapely points and latitude & longitude pairs and vice versa, as well as extracting points from mileages for an ELR. Finally, `TrackGeoJSON` object serves to assist in downloading track geojsons using a single function.

```python
from crosstech.location import explore, LocTools, TrackGeoJSON
```

### Mileage

[🚂 Mileage documentation.](docs/mileage.md) This module contains an object which helps in converting mileages from _Miles.Yards_ to decimal miles, or _Miles.Chains_ to decimal miles, and vice versa.

```python
from crosstech.mileage import MilesYards
```

### ELRs

[👷 ELRs documentation](docs/elrs.md) This module contains objects that help with downloading our Network Models. For more extensive documentation about the Network Model see [this article.](https://docs.crosstech.co.uk/doc/network-model-kfGqIB0lxL)

```python
from crosstech.elrs import FullModel, SimplifiedModel
```
