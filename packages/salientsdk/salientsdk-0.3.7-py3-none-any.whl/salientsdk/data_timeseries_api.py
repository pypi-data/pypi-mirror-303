#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Historical data timeseries.

This module is an interface to the Salient `data_timeseries` API, which returns historical
observed data.  It also includes utility functions for operating on the returned data.

Command line usage example:

```
cd ~/salientsdk
# this will get a single variable in a single file:
python -m salientsdk data_timeseries -lat 42 -lon -73 -fld all --start 2020-01-01 --end 2020-12-31 --force  -u username -p password
# this will get multiple variables in separate files:
python -m salientsdk data_timeseries -lat 42 -lon -73 -fld all -var temp,precip -u username -p password
# test with an apikey
python -m salientsdk data_timeseries -lat 42 -lon -73 -fld anom --start 2020-01-01 --end 2020-12-31 --force --apikey testkey
```

"""

import numpy as np
import pandas as pd
import requests
import xarray as xr

from .constants import _build_urls, _expand_comma
from .location import Location
from .login_api import download_queries

HOURLY_VARIABLES = [
    "cc",
    "precip",
    "sm",
    "snow",
    "st",
    "temp",
    "tsi",
    "dhi",
    "dni",
    "wdir",
    "wdir100",
    "wgst",
    "wspd",
    "wspd100",
]


def data_timeseries(
    # API inputs -------
    loc: Location,
    variable: str | list[str] = "temp",
    field: str = "anom",
    debias: bool = False,
    start: str = "1950-01-01",
    end: str = "-today",
    format: str = "nc",
    frequency: str = "daily",
    # non-API arguments ---
    destination: str = "-default",
    force: bool = False,
    session: requests.Session | None = None,
    apikey: str | None = None,
    verify: bool | None = None,
    verbose: bool = False,
    **kwargs,
) -> str | pd.DataFrame:
    """Get a historical time series of ERA5 data.

    This function is a convenience wrapper to the Salient
    [API](https://api.salientpredictions.com/v2/documentation/api/#/Historical/get_data_timeseries).

    Args:
        loc (Location): The location to query.
            If using a `shapefile` or `location_file`, may input a vector of file names which
            will trigger multiple calls to `data_timeseries`.
        variable (str | list[str]): The variable to query, defaults to `temp`
            To request multiple variables, separate them with a comma `temp,precip`
            This will download one file per variable
            See the
            [Data Fields](https://salientpredictions.notion.site/Variables-d88463032846402e80c9c0972412fe60)
            documentation for a full list of available historical variables.
        field (str): The field to query, defaults to "anom"
        debias (bool): If True, debias the data to local observations.
            Disabled for `shapefile` locations.
            [detail](https://salientpredictions.notion.site/Debiasing-2888d5759eef4fe89a5ba3e40cd72c8f)
        start (str): The start date of the time series
        end (str): The end date of the time series
        format (str): The format of the response
        frequency (str): The frequency of the time series
        destination (str): The directory to download the data to
        force (bool): If False (default), don't download the data if it already exists
        session (requests.Session): The session object to use for the request.
            If `None` (default) uses `get_current_session()`.
        apikey (str | None): The API key to use for the request.
            In most cases, this is not needed if a `session` is provided.
        verify (bool): If True (default), verify the SSL certificate
        verbose (bool): If True (default False) print status messages
        **kwargs: Additional arguments to pass to the API

    Keyword Arguments:
        units (str): `SI` or `US`

    Returns:
        str | pd.DataFrame:
            the file name of the downloaded data.  File names are a hash of the query parameters.
            When `force=False` and the file already exists, the function will return the file name
            almost instantaneously without querying the API.
            If multiple variables are requested, returns a `pd.DataFrame` with columns `file_name`
            and additional columns documenting the vectorized input arguments such as `location_file`
            or `variable`
    """
    assert field in [
        "anom",
        "anom_d",
        "anom_ds",
        "anom_qnt",
        "anom_s",
        "clim",
        "stdv",
        "trend",
        "vals",
        "all",
    ], f"Invalid field {field}"
    assert format in ["nc", "csv"], f"Invalid format {format}"
    assert frequency in [
        "hourly",
        "daily",
        "weekly",
        "monthly",
        "3-monthly",
    ], f"Invalid frequency {frequency}"

    if field != "vals" and frequency == "hourly":
        raise ValueError("Only field `vals` is available for hourly frequency")

    variable = _expand_comma(
        variable, HOURLY_VARIABLES if frequency == "hourly" else None, "variable"
    )

    endpoint = "data_timeseries"
    args = loc.asdict(
        start=start,
        end=end,
        debias=debias,
        field=field,
        format=format,
        frequency=frequency,
        variable=variable,
        apikey=apikey,
        **kwargs,
    )

    queries = _build_urls(endpoint, args, destination)

    download_queries(
        query=queries["query"].values,
        file_name=queries["file_name"].values,
        force=force,
        session=session,
        verify=verify,
        verbose=verbose,
        format=format,
    )

    if len(queries) == 1:
        return queries["file_name"].values[0]
    else:
        # Now that we've executed the queries, we don't need it anymore:
        queries = queries.drop(columns="query")

        # we vectorized on something other than variable, but we still need it
        # in load_multihistory to rename the fields since we don't have short_name
        if not "variable" in queries:
            queries["variable"] = variable

        return queries


def _load_history_row(row: pd.DataFrame, fields: list[str] = ["vals"]) -> xr.Dataset:
    """Load a single history file and prepare for merging with others."""
    variable = row["variable"] if "variable" in row else "variable"

    hst = xr.load_dataset(row["file_name"])
    hst = hst[fields]
    fields_new = [variable if field == "vals" else variable + "_" + field for field in fields]
    hst = hst.rename({field: field_new for field, field_new in zip(fields, fields_new)})
    for fld in fields_new:
        hst[fld].attrs = hst.attrs
    hst.attrs = {}

    if "location_file" in row:
        # Preserve the provenance of the source location_file
        location_files = np.repeat(row["location_file"], len(hst.location))
        hst = hst.assign_coords(location_file=("location", location_files))

    hst.close()

    return hst


def load_multihistory(files: pd.DataFrame, fields: list[str] = ["vals"]) -> xr.Dataset:
    """Load multiple .nc history files and merge them into a single dataset.

    Args:
        files (pd.DataFramme): Table of the type returned by
            `data_timeseries` when multiple `variable`s, `location_file`s
            or `shapefile`s are requested
            e.g. `data_timeseries(..., variable = "temp,precip")`

        fields (list[str]): List of fields to extract from the history files.
            Useful if when calling `data_timeseries(..., field = "all")`

    Returns:
        xr.Dataset: The merged dataset, where each field and variable is renamed
            to `<variable>_<field>` or simply `variable` if field = "vals".
            This will cause the format of a multi-variable file to match the data
            variable names of `downscale`, which natively supports multi-variable queries.
    """
    hst = [_load_history_row(row, fields) for _, row in files.iterrows()]
    hst = xr.merge(hst)
    return hst
