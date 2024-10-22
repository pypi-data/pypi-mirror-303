# script responsible for the utils around avro files

from pandas import DataFrame

from fastavro import writer

from ..configs.mappers import TypeMapping


def generate_avro_file(df: DataFrame, file_name: str) -> None:
    """
    Generate a pandas DataFrame into an avro file.

    Args:
        df (DataFrame): The pandas DataFrame to convert to avro.
        file_name (str): The name of the file to write the avro data to.
    """

    def _define_schema() -> dict:
        """Define the schema from the DataFrame."""

        return {
            "type": "record",
            "name": "synthetic_data_generator",
            "fields": [
                {"name": col, "type": TypeMapping.get(str(df[col].dtype), "string")}
                for col in df.columns
            ],
        }
    
    df_str = df.astype(str)

    with open(file_name, "wb") as out:
        writer(out, _define_schema(), df_str.to_dict("records"))
