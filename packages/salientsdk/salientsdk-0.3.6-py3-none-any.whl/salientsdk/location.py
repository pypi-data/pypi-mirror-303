#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Define the Location class."""

# Usage example:
# python location.py --lat 42 --lon -73

import os

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from . import constants, login_api

# location_file supports a variety of potential column names:
# fmt: off
LON_NAMES = ["lon", "Lon", "LON", "longitude", "Longitude", "LONGITUDE", "lng", "x", "X"]
LAT_NAMES = ["lat", "Lat", "LAT", "latitude", "Latitude", "LATITUDE", "y", "Y"]
NAM_NAMES = ["Location", "location", "loc", "id", "ID", "Place", "place", "Coordinates", "coordinates", "Name", "name"]
# fmt:on


class Location:
    """Define geographical parameters for an API query.

    The Salient API defines location by a single latitude/longitude,
    multiple latitude/longitude pairs in a single location_file, or a polygon
    defined in a shapefile.  This class manages these options.
    """

    def __init__(
        self,
        lat: float | None = None,
        lon: float | None = None,
        location_file: str | list[str] | None = None,
        shapefile: str | list[str] | None = None,
        region: str | list[str] | None = None,
    ):
        """Initialize a Location object.

        Only one of the following 4 options should be used at a time: lat/lon,
        location_file, shapefile, or region.

        Args:
            lat (float): Latitude in degrees, -90 to 90.
            lon (float): Longitude in degrees, -180 to 180.
            location_file (str | list[str]): Path(s) to CSV file(s) with latitude and longitude columns.
            shapefile (str | list[str]): Path(s) to a shapefile(s) with a polygon defining the location.
            region (str | list[str]): Accepts continents, countries, or U.S. states (e.g. "usa")
                Only available for `hindcast_summary()`
        """
        self.lat = lat
        self.lon = lon
        self.location_file = self._expand_user_files(location_file)
        self.shapefile = self._expand_user_files(shapefile)
        self.region = region

        self._validate()

    @staticmethod
    def _expand_user_files(files: str | list[str] | None) -> str | list[str] | None:
        """Strip directory names from location_file and shapefile.

        When referencing user files, the user may specify them with
        a directory name because that's how functions like upload_*
        create them.  But the API doesn't have a directory structure and
        only uses the file name.  So we need to strip off the directory.

        Also, handles vectorization of file names in case user passes in
        a list or a comma-separated string.

        :exclude:
        """
        files = constants._expand_comma(files)

        if files is None:
            pass
        elif isinstance(files, str):
            files = os.path.basename(files)
        elif isinstance(files, list):
            files = [os.path.basename(f) for f in files]

        return files

    def asdict(self, **kwargs) -> dict:
        """Render as a dictionary.

        Generates a dictionary representation that can be encoded into a URL.
        Will contain one and only one location_file, shapefile, or lat/lon pair.

        Args:
            **kwargs: Additional key-value pairs to include in the dictionary.
                Will validate some common arguments that are shared across API calls.
        """
        if self.location_file:
            dct = {"location_file": self.location_file, **kwargs}
        elif self.shapefile:
            dct = {"shapefile": self.shapefile, **kwargs}
        elif self.region:
            dct = {"region": self.region, **kwargs}
        else:
            dct = {"lat": self.lat, "lon": self.lon, **kwargs}

        if "apikey" in dct and dct["apikey"] is not None:
            dct["apikey"] = login_api._get_api_key(dct["apikey"])

        if "start" in dct:
            dct["start"] = constants._validate_date(dct["start"])
        if "end" in dct:
            dct["end"] = constants._validate_date(dct["end"])
        if "forecast_date" in dct:
            dct["forecast_date"] = constants._validate_date(dct["forecast_date"])

        if "version" in dct:
            dct["version"] = constants._expand_comma(
                val=dct["version"],
                valid=constants.MODEL_VERSIONS,
                name="version",
                default=constants.get_model_version(),
            )

        if "shapefile" in dct and "debias" in dct and dct["debias"]:
            raise ValueError("Cannot debias with shapefile locations")

        return dct

    def load_location_file(self, destination: str = "-default") -> gpd.GeoDataFrame:
        """Load the location file(s) into a DataFrame.

        Args:
            destination (str): The directory where the file is located.
                Defaults to the default directory via `get_file_destination`.

        Returns:
            gpd.GeoDataFrame: The location data in a DataFrame.  If multiple files are loaded,
                the DataFrames will be concatenated into a single DataFrame with an
                additional column `file_name` that documents the source file.

                location_file suports a variety of column names for latitude and longitude.
                This method standardizes them to `lat` and `lon`.
        """
        assert self.location_file is not None

        destination = constants.get_file_destination(destination)

        if isinstance(self.location_file, str):
            geo = pd.read_csv(os.path.join(destination, self.location_file))
        else:
            # location files may be a list of files.  Load all of them.
            geo = pd.concat(
                [
                    pd.read_csv(os.path.join(destination, f)).assign(file_name=f)
                    for f in self.location_file
                ]
            )

        return self._as_geoframe(geo)

    @staticmethod
    def _as_geoframe(geo: pd.DataFrame) -> gpd.GeoDataFrame:
        """Normalize column names on a DataFrame and convert to a GeoDataFrame.

        Regardless of the column names in the input DataFrame, this method
        will return a GeoDataFrame with columns `lat`,`lon`, and `name`

        :exclude:
        """
        col_names = set(geo.columns)
        lon_name = next((name for name in LON_NAMES if name in col_names), None)
        lat_name = next((name for name in LAT_NAMES if name in col_names), None)
        nam_name = next((name for name in NAM_NAMES if name in col_names), None)

        assert lon_name is not None, f"Missing longitude column in {col_names}"
        assert lat_name is not None, f"Missing latitude column in {col_names}"

        geo.rename(columns={lon_name: "lon", lat_name: "lat"}, inplace=True)

        if nam_name is not None:
            # "name" column is optional and not guaranteed to be present.
            geo.rename(columns={nam_name: "name"}, inplace=True)

        geo = gpd.GeoDataFrame(geo, geometry=gpd.points_from_xy(geo.lon, geo.lat))

        return geo

    def _validate(self):
        if self.location_file:
            assert not self.lat, "Cannot specify both lat and location_file"
            assert not self.lon, "Cannot specify both lon and location_file"
            assert not self.region, "Cannot specify both region and location_file"
            assert not self.shapefile, "Cannot specify both shape_file and location_file"
        elif self.shapefile:
            assert not self.region, "Cannot specify both region and shapefile"
            assert not self.lat, "Cannot specify both lat and shape_file"
            assert not self.lon, "Cannot specify both lon and shape_file"
        elif self.region:
            assert not self.lat, "Cannot specify both lat and region"
            assert not self.lon, "Cannot specify both lon and region"
            assert not self.location_file, "Cannot specify both location_file and region"
            assert not self.shapefile, "Cannot specify both shape_file and region"
        else:
            assert self.lat, "Must specify lat & lon, location_file, shapefile, or region"
            assert self.lon, "Must specify lat & lon, location_file, shapefile, or region"
            assert -90 <= self.lat <= 90, "Latitude must be between -90 and 90 degrees"
            assert -180 <= self.lon <= 180, "Longitude must be between -180 and 180 degrees"

    def plot_locations(self, title: str = None, weight: str = None, pad: float = 1.0):
        """Show location points on a map.

        Args:
            title (str): The title of the plot.
            weight (str): The column name in the location file to use to weight the points.
            pad (float): Adds extent to the lat/lon bounding boxon the map.
        """
        geo = self.load_location_file()

        if title is None:
            title = str(self.location_file)

        if weight is not None:
            weight = geo[weight] * 10

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": ccrs.Mercator()})
        min_lon, max_lon = geo["lon"].min() - pad, geo["lon"].max() + pad
        min_lat, max_lat = geo["lat"].min() - pad, geo["lat"].max() + pad

        ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())
        ax.add_feature(cfeature.BORDERS)
        # ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.LAND, edgecolor="black")
        ax.add_feature(cfeature.OCEAN, facecolor="aqua")
        ax.add_feature(cfeature.LAKES, facecolor="aqua")

        ax.scatter(
            geo["lon"],
            geo["lat"],
            s=weight,
            color="dodgerblue",
            alpha=0.5,
            transform=ccrs.PlateCarree(),
        )

        for lon, lat, name in zip(geo["lon"], geo["lat"], geo["name"]):
            ax.text(
                lon,
                lat,
                name,
                fontsize=8,
                ha="center",
                va="center",
                transform=ccrs.PlateCarree(),
            )

        plt.title(title)
        plt.show()

        return fig, ax

    def __str__(self):
        """Return a string representation of the Location object.

        :exclude:
        """
        if self.location_file:
            return f"location file: {self.location_file}"
        elif self.shapefile:
            return f"shape file: {self.shapefile}"
        elif self.region:
            return f"region: {self.region}"
        else:
            return f"({self.lat}, {self.lon})"

    def __eq__(self, other):
        """Check if two Location objects are equal.

        :exclude:
        """
        if self.location_file:
            return self.location_file == other.location_file
        elif self.shapefile:
            return self.shapefile == other.shape_file
        elif self.region:
            return self.region == other.region
        else:
            return self.lat == other.lat and self.lon == other.lon

    def __ne__(self, other):
        """Check if two Location objects are not equal.

        :exclude:
        """
        return not self.__eq__(other)
