# This file contains constants for the generator.

from enum import Enum

from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
from shapely.geometry import MultiPoint
from shapely.geometry import MultiLineString
from shapely.geometry import MultiPolygon
from shapely.geometry import GeometryCollection


# TODO. we need network ontology (?)
class FileType(Enum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    AVRO = "avro"
    GEOJSON = "geojson"
    TURTLE = "turtle"


class GeometryTypes(Enum):
    POINT = Point
    LINESTRING = LineString
    POLYGON = Polygon
    MULTIPOINT = MultiPoint
    MULTILINESTRING = MultiLineString
    MULTIPOLYGON = MultiPolygon
    GEOMETRYCOLLECTION = GeometryCollection


# TODO. floats are tough to predict in terms of size - evaluate
class ValuesType(Enum):
    FLOAT = "float"
    INTEGER = "integer"
    STRING = "string"
    GEOMETRY = GeometryTypes
