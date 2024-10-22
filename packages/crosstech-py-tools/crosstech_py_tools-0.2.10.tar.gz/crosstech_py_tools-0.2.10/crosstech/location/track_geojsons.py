import os
import pickle
import logging
import requests
import pandas as pd
import geopandas as gpd
from tqdm import tqdm


logging.basicConfig(level=logging.INFO)


class TrackGeoJSON:
    """
    A utility class for downloading and managing GeoJSON data of tracks.
    """

    @classmethod
    def download(cls, url: str) -> gpd.GeoDataFrame:
        """
        Downloads GeoJSON data from a URL and converts it into a GeoDataFrame.

        Parameters
        ----------
        url : str
            The URL from which to download GeoJSON data.

        Returns
        -------
        gpd.GeoDataFrame
            A GeoDataFrame created from the downloaded GeoJSON data.
        """
        response = requests.get(url).json()
        return gpd.GeoDataFrame.from_features(response["features"], crs="EPSG:4326")

    @classmethod
    def download_multiple(
        cls,
        tracks: pd.DataFrame = None,
        **kwargs,
    ) -> gpd.GeoDataFrame:
        """
        Downloads GeoJSON data for multiple tracks and combines them into a single GeoDataFrame.

        Parameters
        ----------
        tracks : pd.DataFrame, optional
            A DataFrame containing 'track_id' and 'geojson' columns.
        **kwargs : dict, optional
            Optional keyword arguments:
        - use_cache : bool, default False
            - If True, tries to load data from a cached file. Useful when you want to avoid downloading data again, and save time.
        - show_progress : bool, default True
            - If True, displays a progress bar.
        - save : bool, default False
            - If True, saves the combined GeoDataFrame to a cache file.

        Returns
        -------
        gpd.GeoDataFrame
            A combined GeoDataFrame containing GeoJSON data from all tracks.

        Raises
        ------
        ValueError
            If tracks DataFrame is not provided or does not contain necessary columns ('track_id' and 'geojson').
        """
        use_cache = kwargs.get("use_cache", False)
        show_progress = kwargs.get("show_progress", True)
        save = kwargs.get("save", False)

        if use_cache:
            with open("tracks.pkl", "rb") as f:
                gdf = pickle.load(f)
                logging.warning("Using cache! Data may be incomplete / or outdated.")
                return gpd.GeoDataFrame(gdf)

        if tracks is None:
            raise ValueError(
                "Please provide a DataFrame with 'track_id' and 'geojson' columns."
            )
        if tracks.empty:
            raise ValueError(
                "Please provide a DataFrame with 'track_id' and 'geojson' columns."
            )
        if "track_id" not in tracks.columns:
            raise ValueError("Please provide a 'track_id' column in the DataFrame.")
        if "geojson" not in tracks.columns:
            raise ValueError("Please provide a 'geojson' column in the DataFrame.")

        gdf = gpd.GeoDataFrame()

        for _, row in tqdm(
            tracks.iterrows(),
            total=len(tracks),
            desc="Downloading tracks' geojsons...",
            unit="track",
            disable=not show_progress,
        ):
            track_id = row["track_id"]
            url = row["geojson"]
            new_gdf = cls.download(url)
            new_gdf["track_id"] = track_id
            gdf = pd.concat([gdf, new_gdf])

        if save:
            logging.info("Saving tracks.pkl...")
            with open("tracks.pkl", "wb") as f:
                pickle.dump(gdf, f)

        return gdf.reset_index(drop=True)

    @classmethod
    def delete_cache(cls) -> bool:
        """
        Deletes the cache file used by download_multiple method.

        Returns
        -------
        bool
            True if cache file was successfully deleted, False if no cache file was found.

        Notes
        -----
        This method deletes the cache file 'tracks.pkl' if it exists.
        """
        try:
            os.remove("tracks.pkl")
        except FileNotFoundError:
            logging.warning("No cache found.")
            return False

        logging.info("Cache deleted!")
        return True
