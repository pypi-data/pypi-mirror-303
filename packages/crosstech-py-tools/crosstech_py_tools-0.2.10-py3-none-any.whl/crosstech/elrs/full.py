import json
import geopandas as gpd
from google.cloud import storage


class FullModel:
    @staticmethod
    def download() -> gpd.GeoDataFrame:
        """
        Downloads the Full Network Model from the Google Cloud Storage bucket.

        Source:
        - Google Cloud Storage Bucket: hubble-elr-geojsons
        - Blob: Data/2024-March/NetworkLinks.geojson

        Returns:
        --------
        elr_gdf : gpd.GeoDataFrame
            GeoDataFrame of the Full Network Model.
        """
        client = storage.Client()
        bucket = client.get_bucket("hubble-elr-geojsons")
        blob = bucket.blob("Data/2024-March/NetworkLinks.geojson")

        elr_string = json.loads(blob.download_as_string())
        elr_gdf = gpd.GeoDataFrame.from_features(elr_string["features"])
        elr_gdf.crs = "EPSG:27700"

        return elr_gdf
