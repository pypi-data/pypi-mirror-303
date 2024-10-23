# API 24SEA

**api_24sea** is a project designed to provide aid for the interaction with data from the [24SEA API](https://api.24sea.eu/).

## Installation

```shell
pip install api_24sea
```

## DataSignals Usage


The following example shows the classical usage of the datasignals module.

* The first step is to import the package and the necessary libraries.
* Then, the environment variables are loaded from a `.env` file.
* After that, the package is initialized and the user is authenticated with the API.
* Finally, the user can get data from the API.

### Importing the package
```python
# %%
# **Package Imports**
# - From the Python Standard Library
import logging
import os

# - From third party libraries
import pandas as pd
import dotenv  # <-- Not necessary to api_24sea per se, but useful for
                #     loading environment variables. Install it with
                #     `pip install python-dotenv`

# - API 24SEA
from api_24sea.version import __version__, parse_version
import api_24sea
```

### Setting up the environment variables

This step assumes that you have a file structure similar to the following one:

```shell
.
├── env/
│   └── .env
├── notebooks/
│   └── example.ipynb
└── requirements.txt
```

The `.env` file should look like this:

```shell
API_USERNAME=your_username
API_PASSWORD=your_password
```


With this in mind, the following code snippet shows how to load the environment
variables from the `.env` file:

```python
# %%
_ = dotenv.load_dotenv("../env/.env")
if _:
    print("Environment Variables Loaded Successfully")
    print(os.getenv("API_USERNAME"))
else:
    raise Exception("Environment Variables Not Loaded")
```

### Initializing an empty dataframe

Initializing an empty dataframe is necessary to use the API, as here is
where the data will be stored.

```python
# %%
# **DataFrame initialization**
# The empty DataFrame is created beforehand because it needs to authenticate
# with the API to fetch the data.
df = pd.DataFrame()

# %%
# This is a test to check if the authentication system warns the users when
# they are not authenticated.
try:
    df.datasignals.get_metrics()
except Exception as e:
    print("API not available")
    print(e)
# It will raise an exception because the user is not authenticated
```

### Authenticating with the API

The authentication step allows the user to access the API and check the
available metrics.

```python
# %%
# **Authentication**
df.datasignals.authenticate(os.getenv("API_USERNAME"), os.getenv("API_PASSWORD"))
```

### Checking the available metrics after authentication
```python
# %%
# **Metrics Overview**
# The metrics overview is a summary of the metrics available in the API and can
# be accessed from a hidden method in the DataSignals class.
df.datasignals._DataSignals__api.metrics_overview
# It will show all the available metrics with the corresponding units
# and the time window for which the user is allowed to get data
```

### Getting sample data from the API

After loading the environment variables and authenticating with the API,
the user can get data from [24SEA API endpoints](https://api.24sea.eu/redoc/v1/).

The data is retrieved and stored in the DataFrame.

When the option `as_dict` is set to False, the response from each metric is
joined on the timestamp which is then set as the index of DataFrame.
This option will necessarily drop the `location` and `site` columns from the
DataFrame, but they can still be retrieved from the metrics names.

The data retrieval is done by specifying the sites or the locations or both, the
metrics, and timestamps.

* Sites: Case insensitive, it can either match `site` or `site_id`. It is an
  optional parameter.
* Locations: Case insensitive, it can either match `location` or `location_id`.
  It is an optional parameter.
* Metrics: Case insensitive, it can be a partial match of the metric name
* Timestamps: Timezone-aware datetime, strings in ISO 8601 format, or shorthand
  strings compatible with the [shorthand_datetime package](https://pypi.org/project/shorthand-datetime/).

```python
# %%
# **Data Retrieval**

sites = ["wf"]

locations = ["a01", "a02"]

metrics = ["mean WinDSpEed", "mean pitch", "mean-Yaw", "mean_power"]

start_timestamp = "2020-03-01T00:00:00Z"
end_timestamp = "2020-06-01T00:00:00Z"

df.datasignals.get_data(sites, locations, metrics,
                        start_timestamp, end_timestamp, as_dict=False)
```


#### Checking the metrics selected and the data

```python
# %%
df.datasignals.selected_metrics
df
```

#### as_dict True

When `as_dict` is set to True, the response from each metric is stored in a
dictionary with the site and location as keys.

```python
# %%
# Data is a dictionary of dictionary of DataFrames in the shape of:
# {
#   "site1": {
#     "location1": DataFrame,
#     "location2": DataFrame,
#     ...
#   },
#   ...
# }
data = df.datasignals.get_data(sites, locations, metrics,
                    start_timestamp, end_timestamp, as_dict=True)
# %%
# Retrieve the DataFrame for the windfarm WFA01 only
data["windfarm"]["WFA02"]
```

## Core API Usage

The core API module is designed to provide a more direct interaction with the
[24SEA API](https://api.24sea.eu/redoc/v1>) as it is not implemented as a
[pandas accessor](https://pandas.pydata.org/pandas-docs/stable/development/extending.html).


The following example shows the classical usage of the core API module, which
can be integrated within other standalone classes or functions.

* The first step is to import the package and the necessary libraries.
* Then, the environment variables are loaded from a `.env` file.
* After that, the package is initialized and the user is authenticated with the API.
* Finally, the user can get data from the API.

The first two steps are the same as in the DataSignals module and will not be
repeated here.

### Authenticating with the API

The authentication step allows the user to access the API and check the
available metrics.

```python
  # %%
  # **Authentication**
  api = api_24sea.API()
  api.authenticate(
      os.getenv("API_USERNAME"), os.getenv("API_PASSWORD")
  )
```

#### Checking the available metrics after authentication

```python
  # %%
  # **Metrics Overview**
  # The metrics overview is a summary of the metrics available in the API and
  # can be accessed from a hidden method in the DataSignals class.
  api._API__api.metrics_overview
  # It will show all the available metrics with the corresponding units
  # and the time window for which the user is allowed to get Data
```

### Getting sample data from the API

After loading the environment variables and authenticating with the API,
the user can get data from [24SEA API endpoints](https://api.24sea.eu/redoc/v1/).

The retrieved data can be stored in a DataFrame or a dictionary:

- When the option `as_dict` is set to False the output is a dataframe. Besed on
  the option `outer_join_on_timestamp`, the response will be:

  * `outer_join_on_timestamp = True`: the response from each metric is joined
    on the timestamp which is then set as the index of DataFrame. This option
    will necessarily drop the `location` and `site` columns from the DataFrame,
    but they can still be retrieved from the metrics names.
  * `outer_join_on_timestamp = false`: the response from each metric is stored
    in a separate DataFrame and the `site` and `location` columns are kept.
    This means that the DataFrame will be "diagonal" with repeated timestamps
    (as many times as the number of queried (locations, sites) pairs).

- When the option `as_dict` is set to True, the dataframe is returned as
  a dictionary according to the following formula:
  `dataframe.reset_index().to_dict('records')`.

```python
  # %%
  # **Data Retrieval**
  sites = ["wf"]

  locations = ["a01", "a02"]

  metrics = ["mean WinDSpEed", "mean pitch", "mean-Yaw", "mean_power"]

  start_timestamp = "2020-03-01T00:00:00Z"
  end_timestamp = "2020-06-01T00:00:00Z"

  data = api.get_data(sites, locations, metrics,
                      start_timestamp, end_timestamp, as_dict=False,
                      outer_join_on_timestamp=True)
```

## Fatigue Extra

The extra is compatible with Python versions from 3.8 to 3.10, and installs the
[py-fatigue](https://owi-lab.github.io/py_fatigue/) and
[swifter](https://github.com/jmcarpenter2/swifter) packages.

### Installation

To install the extra, run the following command in your terminal:

```python
pip install api_24sea[fatigue]
```

### Usage

```python
# %%
# Import the pandas fatigue accessor from the api_24sea package
from api_24sea.datasignals import fatigue
```

> [!NOTE]
>
> Suppose you have already authenticated with the API, loaded the environment variables, and initialized the DataFrame.

If your *Metrics Overview* table shows metrics whose name starts with `CC_`,
then the fatigue extra will be available for use.

```python
# %%
# **Data Retrieval**
# Besides SCADA data, we will query cycle-count metrics, which are available
# by looking for "CC" (cycle-count) and ["Mtn", "Mtl"] (i.e. Normal and
# Lateral Bending moment).

sites = ["wf"]
locations = ["a01", "a02"]
metrics = ["mean WinDSpEed", "mean pitch", "mean-Yaw", "mean power",
            "cc mtn", "cc mtl"] # <-- Cycle-count metrics

start_timestamp = "2020-03-01T00:00:00Z"
end_timestamp = "2020-06-01T00:00:00Z"

df.datasignals.get_data(sites, locations, metrics,
                        start_timestamp, end_timestamp, as_dict=False)
```

#### Analyzing cycle-count metrics

Converting the cycle-count JSON objects to [`py_fatigue.CycleCount`](https://owi-lab.github.io/py_fatigue/api/cycle_count/cycle_count_.html#py_fatigue.cycle_count.cycle_count.CycleCount)
objects is the first step in the fatigue analysis. This is done by calling the
`api_24sea.datasignals.fatigue.Fatigue.cycle_counts_to_objects` method.

```python
# %%
# **Fatigue Analysis**
# The fatigue analysis is done by calling the cycle_counts_to_objects() method
# from the fatigue accessor.
try:
    df.fatigue.cycle_counts_to_objects()
except ImportError as ie:
    print(f"\033[31;1mImportError\033[22m: {ie}")
```

At this point, you can treat your [`py_fatigue.CycleCount`](https://owi-lab.github.io/py_fatigue/api/cycle_count/cycle_count_.html#py_fatigue.cycle_count.cycle_count.CycleCount) objects as
you would normally do in [py-fatigue](https://owi-lab.github.io/py_fatigue/).

For more information, check py-fatigue's [beginner's guide](https://owi-lab.github.io/py_fatigue/user/01-absolute-noob.html) and [API documentation](https://owi-lab.github.io/py_fatigue/api/01-index.html).


## Project Structure

```shell
.
├── .azure/
├── api_24sea/
│   ├── __init__.py
│   ├── datasignals/
│   │   ├── __init__.py
│   │   ├── fatigue.py
│   │   └── schemas.py
│   ├── core.py
│   ├── exceptions.py
│   ├── singleton.py
│   ├── utils.py
│   └── version.py
├── tests/
├── docs/
├── notebooks/
├── pyproject.toml
├── LICENSE
├── VERSION
└── README.md
```

## License

The package is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
