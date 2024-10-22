from shapely.ops import nearest_points
from abc import ABC, abstractmethod
from dataclasses import dataclass
from ..mileage import MilesYards
from shapely import Point
from enum import Enum
import geopandas as gpd
import pandas as pd
import numpy as np
import pickle
import os


# That's the coords when lat-long = (1, 1) in 4326 crs
ORIGIN27700 = Point(733898.3258933355, -5416388.13814126)
NULLCOORDS27700 = Point(622575.7031043093, -5527063.8148287395)
FAR_COORDS_THRESHOLD = 1000  # 1km


@dataclass
class _ExceptionInfo:
    code: str
    message: str
    ref: str = "https://docs.crosstech.co.uk/doc/violation-mileages-bAz6n1vCbB"


class _ELRExceptionEnum(Enum):
    IRISH = _ExceptionInfo(
        "IRISH",
        "The coordinates are in Ireland.",
    )
    EMPTY_COORDS = _ExceptionInfo(
        "EMPTY_COORDS",
        "This case exists for cases when the input into the match() function is a Point() with no latitude or longitude specified.",
    )
    FAR_COORDS = _ExceptionInfo(
        "FAR_COORDS",
        "If the point's coordinates put it at over 1km away from its nearest relevant (ELR present on its corresponding track) it is considered far.",
    )
    WRONG_COORDS = _ExceptionInfo(
        "WRONG_COORDS",
        "If the coordinates of the point are not consistent with CRS ESPG:4326 then it would be considered WRONG. Practically this means that when the coordinate is translated to CRS ESPG:27700 it becomes infinite.",
    )
    ORIGIN_COORDS = _ExceptionInfo(
        "ORIGIN_COORDS",
        "By convention whenever we don't know the coordinates of a point-like object we assign it coordinates of 1,1 in ESPG:4326. Points with such coordinates are considered to be at “origin”.",
    )
    NULL_COORDS = _ExceptionInfo(
        "NULL_COORDS",
        "If the coordinates of the point are null OR zero then it is considered NULL. When backend sends a point with null coordinates it is converted to 0 because we use float64 type, hence zero and null are treated equivalently.",
    )

    @property
    def code(self):
        return self.value.code

    @property
    def message(self):
        return self.value.message

    @property
    def ref(self):
        return self.value.ref


# ELRBase is an abstract class that defines the interface for all ELR classes.
#
# This interface will allow one to expand how exacly we get the ELR data.
# Perhaps in the future we will want to get the ELR data from a pd.DataFrame or a dict.
class _ELRBase(ABC):
    @abstractmethod
    def get(self) -> gpd.GeoDataFrame:
        pass


class _StringELR(_ELRBase):
    def __init__(self, **kwargs):
        self.elr: str = kwargs.get("elr")

    def get(self) -> gpd.GeoDataFrame:
        elrs_path = self._get_elrs_path()

        with open(elrs_path, "rb") as f:
            elrs: gpd.GeoDataFrame = pickle.load(f)

        elr: gpd.GeoDataFrame = (
            elrs[elrs["elr"] == self.elr].reset_index(drop=True)
            if self.elr != "all"
            else elrs
        )
        return elr
    
    def _get_elrs_path(self) -> str:
        # Get the directory of the current script
        current_dir = os.path.dirname(__file__)
        
        if self.elr.startswith("nm_"): # nm = Network Model (Simplified in this case)
            file_name = "elrs.pkl"
            self.elr = self.elr.replace("nm_", "")
        else: # manual is default
            file_name = "manual_elrs.pkl"
        
        # Construct the path to the elrs.pkl file
        return os.path.join(current_dir, "data", file_name)
        

class _GeoDataFrameELR(_ELRBase):
    def __init__(self, **kwargs):
        self.elr: gpd.GeoDataFrame = kwargs.get("elr")
        self._validate_columns()

    def get(self) -> gpd.GeoDataFrame:
        if self.elr.crs != 27700:
            self.elr = self.elr.to_crs(27700)
        if "L_M_FROM" in self.elr.columns:
            self.elr.rename(columns={"L_M_FROM": "start_mileage"}, inplace=True)
        if "L_M_TO" in self.elr.columns:
            self.elr.rename(columns={"L_M_TO": "end_mileage"}, inplace=True)
        return self.elr

    def _validate_columns(self) -> None:
        if "geometry" not in self.elr.columns:
            raise ValueError("Please provide a GeoDataFrame with a 'geometry' column.")
        if "elr" not in self.elr.columns:
            raise ValueError("Please provide a GeoDataFrame with an 'elr' column.")
        if (
            "start_mileage" not in self.elr.columns
            and "L_M_FROM" not in self.elr.columns
        ):
            raise ValueError(
                "Please provide a GeoDataFrame with a 'start_mileage' OR 'L_M_FROM' column."
            )
        if "end_mileage" not in self.elr.columns and "L_M_TO" not in self.elr.columns:
            raise ValueError(
                "Please provide a GeoDataFrame with an 'end_mileage' OR 'L_M_TO' column."
            )


class _ELRFactory:
    @staticmethod
    def create_elr(**kwargs) -> type[_ELRBase]:
        elr = kwargs.get("elr")
        if elr is None:
            raise ValueError("Please provide an ELR.")
        elif isinstance(elr, str):
            return _StringELR(**kwargs)
        elif isinstance(elr, gpd.GeoDataFrame):
            return _GeoDataFrameELR(**kwargs)
        else:
            raise ValueError("Please provide a valid ELR.")


def _adjust_mileage(gdf: gpd.GeoDataFrame) -> pd.Series:
    """
    Adjust mileage based on the geometry projection.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing geometries to be adjusted.

    Returns
    -------
    Series[float]
        Adjusted mileage values as a pandas Series.
    """
    return gdf["saved_geom"].project(
        gdf.geometry,
        normalized=True,
    )


def _find_absolute_mileage(*, start: float, end: float, dr: float) -> float:
    """
    Finds absolute mileage of points using dr and network model.

    Parameters
    ----------
    start : float
        Starting mileage point.
    end : float
        Ending mileage point.
    dr : float
        Distance ratio for the network model.

    Returns
    -------
    float
        Absolute mileage value.
    """
    sign = 1 if start < end else -1
    return start + sign * abs(start - end) * dr


def _filter_irish_assets(
    gdf: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    """
    Filter and label Irish assets in the GeoDataFrame.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing asset data.

    Returns
    -------
    gpd.GeoDataFrame
        GeoDataFrame with Irish assets labeled.
    """
    gdf.loc[
        (
            (gdf.geometry.x > -203722.42)  # Irish Coords in crs = 27700
            & (gdf.geometry.x < 273547.999)
            & (gdf.geometry.y > 199423.488)
            & (gdf.geometry.y < 617276.107)
        ),
        ["elr", "mileage"],
    ] = ["IRISH", 1]

    return gdf


def _get_infinite_coords_ids(
    gdf: gpd.GeoDataFrame,
) -> list[int]:
    """
    Get IDs of points with infinite coordinates.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing point geometries.

    Returns
    -------
    list[int]
        List of IDs for points with infinite coordinates.
    """
    return gdf[gdf["geometry"] == Point(np.inf, np.inf)]["id"].tolist()


def _get_empty_coords_ids(
    gdf: gpd.GeoDataFrame,
) -> list[int]:
    """
    Get IDs of points with nno coordinates.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing point geometries.

    Returns
    -------
    list[int]
        List of IDs for points with no coordinates.
    """
    return gdf[gdf["geometry"] == Point()]["id"].tolist()


def _get_origin_coords_ids(
    gdf: gpd.GeoDataFrame,
) -> list[int]:
    """
    Get IDs of points at the origin coordinates.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing point geometries.

    Returns
    -------
    list[int]
        List of IDs for points at the origin coordinates.
    """
    return gdf[gdf["geometry"] == ORIGIN27700]["id"].tolist()


def _get_null_coords_ids(
    gdf: gpd.GeoDataFrame,
) -> list[int]:
    """
    Get IDs of points with null coordinates. Because golang
    converts null to 0 when we use type float64, when we get
    lat long = 0 it means that in the database it was null.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing point geometries.

    Returns
    -------
    list[int]
        List of IDs for points with null coordinates.
    """
    return gdf[gdf["geometry"] == NULLCOORDS27700]["id"].tolist()


def _filter_far_points(
    gdf: gpd.GeoDataFrame,
) -> list[int]:
    """
    Filter and label points that exceed the far coordinates threshold.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame containing merged geometries.

    Returns
    -------
    list[int]
        List of IDs for points exceeding the far coordinates threshold.
    """
    gdf.loc[
        (gdf["distance"] > FAR_COORDS_THRESHOLD),
        ["elr", "mileage"],
    ] = ["FAR_COORDS", 1]

    return gdf


class LocTools:
    """
    A class providing tools for location-based operations.

    Methods
    -------
    to_point(lat: float, lon: float, **kwargs) -> Point
        Converts latitude and longitude to a Point object, optionally transforming CRS.
    to_coords(point: Point, **kwargs) -> tuple[float, float] | float
        Extracts latitude or longitude or both from a Point object based on provided keyword arguments.
    point_from_mileage(mileage: float, **kwargs) -> Point
        Interpolates a Point on a GeoDataFrame geometry based on a given mileage.
    """

    @classmethod
    def to_point(cls, lat: float, lon: float, **kwargs) -> Point:
        """
        Converts latitude and longitude to a Point object, optionally transforming CRS.

        Parameters
        ----------
        lat : float
            Latitude of the point.
        lon : float
            Longitude of the point.
        **kwargs : dict
            Optional keyword arguments:
        - crs : str or int
            - The current coordinate reference system of the point.
        - to_crs : str or int
            - The target coordinate reference system to transform the point.

        NOTE: 'crs' and 'to_crs' must be provided together.

        Returns
        -------
        Point
            A shapely.geometry.Point object representing the location.

        Raises
        ------
        Exception
            If only one of 'crs' or 'to_crs' is provided.
        """
        crs = kwargs.get("crs")
        to_crs = kwargs.get("to_crs")

        if crs and to_crs:
            return (
                gpd.GeoDataFrame({"geometry": [Point(lon, lat)]}, crs=crs)
                .to_crs(to_crs)
                .iloc[0]["geometry"]
            )
        elif (crs and not to_crs) or (to_crs and not crs):
            raise Exception(
                "Please provide both 'crs' and 'to_crs' as keyword arguments."
            )

        return Point(lon, lat)

    @classmethod
    def to_coords(cls, point: Point, **kwargs) -> tuple[float, float] | float:
        """
        Extracts latitude or longitude or both from a Point object based on provided keyword arguments.
        Optionally transforming CRS, by default CRS agnostic.

        Parameters
        ----------
        point : Point
            A shapely.geometry.Point object.
        **kwargs : dict
            Optional keyword arguments:
        - lat : bool
            - If True, returns the latitude of the point.
        - lon : bool
            - If True, returns the longitude of the point.
        - crs : str or int
            - The current coordinate reference system of the point.
        - to_crs : str or int
            - The target coordinate reference system to transform the point.

        NOTE: 'crs' and 'to_crs' must be provided together.
        NOTE: 'lat' and 'lon' cannot be provided together.

        Returns
        -------
        tuple[float, float] or float
            - A tuple of (latitude, longitude) if neither 'lat' nor 'lon' is specified.
            - A single float representing latitude if 'lat' is True.
            - A single float representing longitude if 'lon' is True.

        Raises
        ------
        Exception
            If both 'lat' and 'lon' are provided.
        Exception
            If only one of 'crs' or 'to_crs' is provided.
        """
        lat, lon = kwargs.get("lat"), kwargs.get("lon")
        crs, to_crs = kwargs.get("crs"), kwargs.get("to_crs")

        if crs and to_crs:
            point = (
                gpd.GeoDataFrame({"geometry": [point]}, crs=crs)
                .to_crs(to_crs)
                .iloc[0]["geometry"]
            )
        elif (crs and not to_crs) or (to_crs and not crs):
            raise Exception(
                "Please provide both 'crs' and 'to_crs' as keyword arguments."
            )

        if lat and lon:
            raise Exception(
                "Please provide either 'lat' or 'lon' as a keyword argument."
            )
        elif lat:
            return point.coords.xy[1][0]
        elif lon:
            return point.coords.xy[0][0]

        return point.coords.xy[1][0], point.coords.xy[0][0]

    @classmethod
    def point_from_mileage(
        cls,
        mileage: float,
        **kwargs,
    ) -> Point:
        """
        Interpolates a Point on a GeoDataFrame geometry based on a given mileage.
        Naturally input mileage is in miles. Return point is in meters of crs 27700.

        Parameters
        ----------
        mileage : float
            The mileage to interpolate the point.
        **kwargs : dict
            Additional keyword arguments to pass to the ELRFactory.create_elr method.
        - elr : str or GeoDataFrame
            - The ELR (Engineer's Line Reference) code or a single-row GeoDataFrame with ELR data.

        Returns
        -------
        Point
            A shapely.geometry.Point object representing the interpolated location.

        Notes
        -----
        The ELRFactory handles the creation and retrieval of ELR data. It supports two types of inputs:
        - A string representing the ELR code, which retrieves the corresponding GeoDataFrame from a predefined file.
        - A GeoDataFrame containing ELR data, which must include columns for 'geometry' and either 'start_mileage' or 'L_M_FROM'.

        The ELR data is assumed to be in EPSG:27700 CRS. If not, it is transformed accordingly.
        """
        if type(kwargs.get("elr")) == str and kwargs.get("elr") == "all":
            raise ValueError("Please provide a single ELR.")

        elr_handler = _ELRFactory.create_elr(**kwargs)
        elr: gpd.GeoDataFrame = elr_handler.get()

        meterage = float((mileage - elr.start_mileage.values[0]) * 1609.34)
        return elr.geometry.values[0].interpolate(meterage)

    @classmethod
    def mileage_from_points(
        self,
        *args,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Match points to their nearest ELR (Engineer's Line Reference) and calculate mileage.

        This function performs a spatial join between points and ELRs, handles special cases
        such as infinite coordinates and origin coordinates, and calculates the mileage for
        each point along its matched ELR.

        Parameters
        ----------
        *args : Point
            A variable number of Point objects to match to ELRs.
        **kwargs : dict
            Additional keyword arguments to pass to the ELRFactory.create_elr method.
        - elr : str or GeoDataFrame
            - The ELR (Engineer's Line Reference) code or a GeoDataFrame with ELR data.
        - in_miles_yards : bool
            - If True, ELR mileages are in miles.yards format and will be converted to decimal miles.

        Returns
        -------
        pd.DataFrame or None
            A DataFrame containing the matched ELR and mileage for each point,
            or None if no matches are found.

        Notes:
        ------
        See also the mother function: https://github.com/HackPartners/FindMileageFromLatLong
        """
        points = gpd.GeoDataFrame()

        # Disallow non-Point objects
        if not all(isinstance(arg, Point) for arg in args):
            raise TypeError("All positional arguments must be of type 'Point'")

        # No points
        if len(args) == 0:
            raise ValueError("Please provide at least one Point.")

        # Single point passed in
        if all(isinstance(arg, Point) for arg in args) and len(args) == 0:
            points = points.set_geometry([args[0]])
            points["id"] = 1

        # Multiple points passed in
        elif all(isinstance(arg, Point) for arg in args) and len(args) > 0:
            points = points.set_geometry([arg for arg in args])
            points["id"] = range(1, len(args) + 1)

        # Set CRS 27700
        points.crs = "EPSG:27700"

        # Get ELR data
        if "elr" not in kwargs:
            kwargs["elr"] = "all"
            kwargs["in_miles_yards"] = False
        elif isinstance(kwargs["elr"], str) and not kwargs["elr"].startswith("nm_"):
            kwargs["in_miles_yards"] = False
            
        elr_handler = _ELRFactory.create_elr(**kwargs)
        elrs: gpd.GeoDataFrame = elr_handler.get()
        elrs["saved_geom"] = elrs["geometry"]

        # Account for if ELR mileages are not in miles.yards
        in_miles_yards = kwargs.get("in_miles_yards", True)
        if not isinstance(in_miles_yards, bool):
            raise ValueError("Please provide a boolean value for 'in_miles_yards'.")

        # Find null coordinates
        null_coord_ids = _get_null_coords_ids(points)

        # Account for infinite (incorrectly input) coordinates
        wrong_coord_ids = _get_infinite_coords_ids(points)
        points.loc[
            points["geometry"]
            == Point(
                np.inf, np.inf
            ),  # Points with incorrectly formatted coordinates will become Point(inf, inf)
            ["geometry"],  # when converted to 27700 crs.
        ] = Point(
            0,  # NOT origin coordinates, but a point that is not on the network,
            0,  # therefore will not be affected by the next filter
        )  # This ensures that these points go through the spatial join - order of data not changed

        # Account for empty (POINT EMPTY) coordinates
        empty_coord_ids = _get_empty_coords_ids(points)
        points.loc[
            points["geometry"] == Point(),
            ["geometry"],
        ] = Point(
            0,  # NOT origin coordinates, but a point that is not on the network,
            0,  # therefore will not be affected by the next filter
        )  # This ensures that these points go through the spatial join - order of data not changed

        # Account for origin coordinates
        origin_coord_ids = _get_origin_coords_ids(points)

        # Perform spatial join (nearest) between points and elrs
        gdf = points.sjoin_nearest(
            elrs,
            distance_col="distance",
        )
        if len(gdf) == 0:
            return None

        # Adjust mileage to relative mileage
        gdf["relative_mileage"] = _adjust_mileage(gdf)

        if in_miles_yards:  # Convert miles.yards to decimal miles
            gdf["start_mileage"] = gdf["start_mileage"].apply(
                lambda x: MilesYards(x).miles_decimal
            )
            gdf["end_mileage"] = gdf["end_mileage"].apply(
                lambda x: MilesYards(x).miles_decimal
            )

        gdf["mileage"] = gdf.apply(
            lambda x: _find_absolute_mileage(
                start=x["start_mileage"],
                end=x["end_mileage"],
                dr=x["relative_mileage"],
            ),
            axis=1,
        )

        # Recalculate distances
        gdf["distance"] = gdf.apply(
            lambda x: nearest_points(x["saved_geom"], x["geometry"])[0].distance(
                x["geometry"]
            ),
            axis=1,
        )

        # Remove double matches for the same point
        gdf = gdf.drop_duplicates(subset=["id"], keep="first")

        # Filter out far violations - mark them as FAR_COORDS
        gdf = _filter_far_points(gdf)

        # Filter out Irish assets - mark them as IRISH
        gdf = _filter_irish_assets(gdf)

        # Mark points with infinite coordinates as WRONG_COORDS
        gdf.loc[
            gdf["id"].isin(wrong_coord_ids),
            ["elr", "mileage"],
        ] = ["WRONG_COORDS", 1]

        # Mark points with origin coordinates as ORIGIN_COORDS
        gdf.loc[
            gdf["id"].isin(origin_coord_ids),
            ["elr", "mileage"],
        ] = ["ORIGIN_COORDS", 1]

        # Mark points with empty coordinates as EMPTY_COORDS
        gdf.loc[
            gdf["id"].isin(empty_coord_ids),
            ["elr", "mileage"],
        ] = ["EMPTY_COORDS", 1]

        # Mark points with null coordinates as NULL_COORDS
        gdf.loc[
            gdf["id"].isin(null_coord_ids),
            ["elr", "mileage"],
        ] = ["NULL_COORDS", 1]

        # Adjust column names & return
        gdf["elr_exception"] = gdf["elr"].apply(
            lambda x: x if x in [e.name for e in _ELRExceptionEnum] else np.nan
        )
        gdf["elr"] = gdf["elr"].apply(
            lambda x: x if x not in [e.name for e in _ELRExceptionEnum] else np.nan
        )
        gdf["mileage"] = gdf["mileage"].apply(lambda x: x if x != 1 else np.nan)
        gdf["message"] = gdf["elr_exception"].apply(
            lambda x: (
                f"{_ELRExceptionEnum[x].message} Docs Reference: {_ELRExceptionEnum[x].ref}"
                if not pd.isna(x)
                else np.nan
            )
        )
        gdf["error"] = gdf["elr_exception"].apply(
            lambda x: True if not pd.isna(x) else False
        )

        return gdf[
            ["id", "elr", "mileage", "distance", "elr_exception", "message", "error"]
        ]
