# script where the sampling methods will be stored

import random
import geopandas as gpd

from geopandas import GeoDataFrame

from ..configs.constants import GeometryTypes


class GeoJSONSampling:

    @staticmethod
    def points_generator(n: int) -> list[tuple[float, float]]:
        """
        Generate a list of points with random coordinates.
        """

        return [(random.uniform(-180, 180), random.uniform(-90, 90)) for _ in range(n)]

    def _create_point_record(self) -> GeometryTypes.POINT:
        """
        Create a GeoDataFrame with random points.
        """

        point = self.points_generator(1)[0]

        x = point[0]
        y = point[1]

        return GeometryTypes.POINT.value(x, y)

    def _create_linestring_record(self) -> GeometryTypes.LINESTRING:
        """
        Create a GeoDataFrame with random linestrings.
        """

        return GeometryTypes.LINESTRING.value(self.points_generator(2))

    def _create_polygon_record(self) -> GeometryTypes.POLYGON:
        """
        Create a GeoDataFrame with random polygons.
        """

        return GeometryTypes.POLYGON.value(self.points_generator(5))

    def _create_multipoint_record(self) -> GeometryTypes.MULTIPOINT:
        """
        Create a GeoDataFrame with random multipoints.
        """

        return GeometryTypes.MULTIPOINT.value(self.points_generator(3))

    def _create_multilinestring_record(self) -> GeometryTypes.MULTILINESTRING:
        """
        Create a GeoDataFrame with random multilinestrings.
        """

        linestrings = [self._create_linestring_record() for _ in range(3)]

        return GeometryTypes.MULTILINESTRING.value(linestrings)

    def _create_multipolygon_record(self) -> GeometryTypes.MULTIPOLYGON:
        """
        Create a GeoDataFrame with random multipolygons.
        """

        polygons = [self._create_polygon_record() for _ in range(3)]

        return GeometryTypes.MULTIPOLYGON.value(polygons)

    def _create_geometrycollection_record(self) -> GeometryTypes.GEOMETRYCOLLECTION:
        """
        Create a GeoDataFrame with random geometry collections.
        """

        geometry_collection = [
            self._create_point_record(),
            self._create_linestring_record(),
            self._create_polygon_record(),
        ]

        return GeometryTypes.GEOMETRYCOLLECTION.value(geometry_collection)

    def generate_sample(self, crs: str = "EPSG:4326") -> GeoDataFrame:
        """
        Create a GeoDataFrame records with random data.

        The sample generated will contain all the geometry types.

        Returns:
            GeoDataFrame: A GeoDataFrame containing the records.
        """

        def selector(type: GeometryTypes):
            match type:
                case GeometryTypes.POINT:
                    return self._create_point_record()
                case GeometryTypes.LINESTRING:
                    return self._create_linestring_record()
                case GeometryTypes.POLYGON:
                    return self._create_polygon_record()
                case GeometryTypes.MULTIPOINT:
                    return self._create_multipoint_record()
                case GeometryTypes.MULTILINESTRING:
                    return self._create_multilinestring_record()
                case GeometryTypes.MULTIPOLYGON:
                    return self._create_multipolygon_record()
                case GeometryTypes.GEOMETRYCOLLECTION:
                    return self._create_geometrycollection_record()

        return GeoDataFrame(
            geometry=[selector(type) for type in list(GeometryTypes)], crs=crs
        )

    def load_file(self, file_path: str) -> GeoDataFrame:
        """
        Load a GeoJSON file.

        Returns:
            GeoDataFrame: A GeoDataFrame containing the data from the GeoJSON file.
        """

        return gpd.read_file(file_path)
