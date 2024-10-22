#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Interface to the Salient `upload_file` API.

There is no command line interface for this module.
"""

import json
import os

import pandas as pd
import requests
import xarray as xr

from .constants import _build_url, get_file_destination
from .location import Location
from .login_api import download_query, get_current_session


def upload_file(file: str, verbose: bool = True, session: requests.Session | None = None) -> None:
    """Uploads a geography file to the Salient API.

    An interface to to the Salient
    [upload_file](https://api.salientpredictions.com/v2/documentation/api/#/General/upload_file)
    API endpoint.

    Args:
        file (str): the file to upload (e.g. a shapefile or CSV).
        verbose (bool): whether to print status messages.
        session (requests.Session): the session to use for the upload.

    """
    if verbose:
        print(f"Uploading {file}")

    (url, loc_file) = _build_url("upload_file")

    if session is None:
        session = get_current_session()

    # do we need to open .zipped shapefiles in 'rb' binary mode?
    req = session.post(url, files={"file": open(file, "r")})
    req.raise_for_status()
    if verbose:
        print(req.text)

    return None


def upload_bounding_box(
    # API arguments ----------
    north: float,
    south: float,
    east: float,
    west: float,
    geoname: str,
    # Non-API arguments --------
    destination: str | None = "-default",
    force: bool = False,
    verbose: bool = False,
    session: requests.Session | None = None,
) -> str:
    """Upload a bounding box.

    Create and upload a GeoJSON shapefile with a rectangular bounding box
    for later use with the `shapefile` location argument.

    Args:
        north (float): Northern extent decimal latitude
        south (float): Southern extent decimal latitude
        east (float): Eastern extent decimal longitude
        west (float): Western extent decimal longitude
        geoname (str): Name of the GeoJSON file and object to create
        destination (str): The destination directory for the generated file
        force (bool): If the file already exists, don't upload it
        verbose (bool): Whether to print status messages
        session (requests.Session): The session object to use for the request

    Returns:
        str: File name of the GeoJSON file
    """
    assert west < east, "West must be less than East"
    assert south < north, "South must be less than North"
    coords = [
        (west, north),
        (east, north),
        (east, south),
        (west, south),
    ]  # upload_shapefile will close the polygon for us
    return upload_shapefile(coords, geoname, destination, force, verbose, session)


def upload_shapefile(
    coords: list[tuple[float, float]],
    geoname: str,
    # Non-API arguments --------
    destination: str | None = "-default",
    force: bool = False,
    verbose: bool = False,
    session: requests.Session | None = None,
):
    """Upload a custom shapefile defined by a a list of lat/lon pairs.

    This will often be used with `Location(shapefile...)`

    Args:
        coords (list[tuple]): List of (longitude, latitude) pairs defining the polygon.
        geoname (str): Name of the GeoJSON file and object to create.
        destination (str): The destination directory for the generated file.
        force (bool): If True, overwrite the existing file if it exists.
        verbose (bool): Whether to print status messages.
        session (requests.Session): The session object to use for the request.

    Returns:
        str: File name of the GeoJSON file.
    """
    geofile = geoname + ".geojson"
    destination = get_file_destination(destination)
    if destination is not None:
        geofile = os.path.join(destination, geofile)
    session = get_current_session() if session is None else session

    if not force and os.path.exists(geofile):
        if verbose:
            print(f"File {geofile} already exists")
        return geofile

    # Check to see if the polygon is closed, and close it if not:
    if coords[0] != coords[-1]:
        coords.append(coords[0])

    # Create the GeoJSON structure
    geoshape = {
        "type": "Feature",
        "properties": {"name": geoname},
        "geometry": {
            "type": "Polygon",
            "coordinates": [coords],
        },
    }

    # Write the GeoJSON to a file
    with open(geofile, "w") as f:
        json.dump(geoshape, f)

    upload_file(file=geofile, verbose=verbose, session=session)

    return geofile


def upload_location_file(
    lats: list[float] | pd.Series,
    lons: list[float] | pd.Series,
    names: list[str] | pd.Series,
    geoname: str,
    destination: str = "-default",
    force: bool = False,
    verbose: bool = False,
    session: requests.Session | None = None,
    **kwargs,
) -> str:
    """Upload a vector of locations.

    Create and upload a CSV file with a list of locations for
    later use with the `location_file` location argument.

    Args:
        lats (list[float] | pd.Series): List of decimal latitudes
        lons (list[float] | pd.Series): List of decimal longitudes
        names (list[str] | pd.Series): List of names for the locations
        geoname (str): Name of the CSV file and object to create
        destination (str): The destination directory for the generated file
        force (bool): When False, if the file already exists don't upload it
        verbose (bool): If True, print status messages
        session (requests.Session): The session object to use for the request
        **kwargs: Additional columns to include in the CSV file

    Returns:
        str: File name of the CSV file
    """
    geofile = geoname + ".csv"
    destination = get_file_destination(destination)
    if destination is not None:
        geofile = os.path.join(destination, geofile)

    if not force and os.path.exists(geofile):
        if verbose:
            print(f"File {geofile} already exists")
        return geofile

    loc_table = pd.DataFrame({"lat": lats, "lon": lons, "name": names, **kwargs})
    loc_table.to_csv(geofile, index=False)

    upload_file(file=geofile, verbose=verbose, session=session)

    return geofile


def merge_location_data(ds: xr.Dataset, loc_file: str | Location):
    """Merge additional data columns from a location_file into a dataset.

    Will add any additional columns from `loc_file` to `ds`.

    Args:
        ds (xr.Dataset): A `Dataset` with a vector `location` coordinate,
            typically resulting from requesting a `location_file`
        loc_file (str | Location): Path to a CSV file containing location data
            or a `Location` object with a `location_file` attribute.

    Returns:
        xr.Dataset: A new `Dataset` with the additional columns from `loc_file`
            along the `location` coordinate.
    """
    geo = (
        loc_file.load_location_file().drop(columns=["geometry"])  # geopandas -> pandas
        if isinstance(loc_file, Location)
        else pd.read_csv(loc_file)
    )

    geo = geo.drop(columns=["lat", "lon"])  # redundant
    geo = geo.rename(columns={"name": "location"}).set_index("location")
    geo = xr.Dataset.from_dataframe(geo)

    return xr.merge([geo, ds], combine_attrs="override")


def user_files(
    destination: str = "-default",
    session: requests.Session | None = None,
    verify: bool | None = None,
    verbose: bool = False,
) -> str:
    """List the location and shape files uploaded by the user.

    Args:
        destination (str): The destination directory for the resulting JSON file
        session (requests.Session): The session object to use for the request
        verify (bool): Whether to verify the SSL certificate.
            Defaults to use the value returned by `get_verify_ssl()`
        verbose (bool): If True, print the full contents of the file.

    Returns:
        str: the location of the JSON file containing top-level entries
             `coordinates` (for `location_file` inputs) and `shapefiles`.
    """
    format = "json"
    endpoint = "user_files"
    (url, loc_file) = _build_url(endpoint, args=None, destination=destination)
    loc_file = f"{loc_file}.{format}"

    download_query(
        query=url,
        file_name=loc_file,
        format=format,
        session=session,
        verify=verify,
        verbose=verbose,
        force=True,
    )

    if verbose:
        # parse the json file and print the results:
        with open(loc_file, "r") as f:
            data = json.load(f)
        for key, value in data.items():
            if isinstance(value, list):
                items = ", ".join(str(item) for item in value)
                print(f"{key}: {items}")
            else:
                print(f"{key}: {value}")

    return loc_file


def _mock_upload_location_file(
    destination: str = "-default",
    **kwargs,
) -> str:
    """Creates a location_file without uploading it."""
    geofile = os.path.join(get_file_destination(destination), "CA_Airports.csv")
    lats = [37.7749, 33.9416, 32.7336]
    lons = [-122.4194, -118.4085, -117.1897]
    names = ["SFO", "LAX", "SAN"]
    pd.DataFrame({"lat": lats, "lon": lons, "name": names}).to_csv(geofile, index=False)
    return geofile
