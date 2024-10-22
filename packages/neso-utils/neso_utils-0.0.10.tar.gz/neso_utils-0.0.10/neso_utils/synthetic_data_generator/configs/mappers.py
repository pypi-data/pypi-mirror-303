# script responsible for mapping processes

from dataclasses import dataclass
from dataclasses import field

@dataclass
class TypeMapping:
    """
    Class that maps the pandas dtypes to the rdflib types.
    """

    int64: str = "int"
    float64: str = "float"
    bool: str = "boolean"
    object: str = "string"
    datetime64_ns: str = field(default="string", metadata={"pandas_dtype": "datetime64[ns]"})

    def get(self, key: str, default: str = "string") -> str:
        return getattr(self, key.replace("[", "_").replace("]", ""), default)
