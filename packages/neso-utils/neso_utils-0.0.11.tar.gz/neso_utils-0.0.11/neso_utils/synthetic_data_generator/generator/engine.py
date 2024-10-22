# code to generate synthetic data

import os
import logging
import pandas as pd
import numpy as np

from typing import Union

from logging import Logger

from pandas import DataFrame

from rdflib import Graph

from ..configs.constants import FileType
from ..configs.constants import ValuesType
from ..utils.pandas import dataframe_multiplier
from ..sampling.geojson import GeoJSONSampling
from ..sampling.ttl import TTLSampling
from ..utils.avro import generate_avro_file


class SyntheticDataGenerator:
    """
    This class is used to generate synthetic dataframes of a specified size and save them in
    various file formats.

    This class firstly generates a sample dataframe according to the parameters specified. After that,
    and depending on the size of the sample dataframe, the dataframe is scaled up or down to the
    target size.

    Args:
        target_size_mb (float): The target size of the file in MB.
        num_columns (int, optional): The number of columns that the generated dataframe will have.
        sample_rows_num (int, optional): The number of rows in the sample dataframe.
        log_level (int, optional): The level of logging to use.

    Returns:
        DataFrame: A pandas DataFrame stored in a specific file format with the specified
        number of columns and rows.
    """

    def __init__(
        self,
        target_size_mb: float,
        num_columns: int = 10,
        sample_rows_num: int = 1000,
        log_level: int = logging.INFO,
    ):

        self.target_size_mb = target_size_mb
        self.num_columns = num_columns
        self.sample_rows_num = sample_rows_num
        self.log_level = log_level

        self.ttl_sampling = TTLSampling()

        self.logger = self._setup_logger()

    def _setup_logger(self) -> Logger:
        """
        Setup the logger for the SyntheticDataGenerator class.
        """

        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    @property
    def target_size_mb(self):
        """
        Get the target size of the file in MB.

        Returns:
            float: The target size of the file in MB.
        """

        return self._target_size_mb

    @property
    def num_columns(self):
        """
        Get the number of columns in the dataframe.

        Returns:
            int: The number of columns in the dataframe.
        """

        return self._num_columns

    @property
    def sample_rows_num(self):
        """
        Get the number of rows in the sample dataframe.

        Returns:
            int: The number of rows in the sample dataframe.
        """

        return self._sample_rows_num

    @target_size_mb.setter
    def target_size_mb(self, value):
        """
        Set the target size of the file in MB.

        Args:
            value (float): The target size of the file in MB.

        Raises:
            ValueError: If the target size is less than or equal to 0 MB.
        """

        if value <= 0:
            raise ValueError("Target size must be greater than 0 MB")

        self._target_size_mb = value

    @num_columns.setter
    def num_columns(self, value):
        """
        Set the number of columns in the dataframe.

        Args:
            value (int): The number of columns in the dataframe.
        """

        if value <= 0:
            raise ValueError("Number of columns must be greater than 0")

        self._num_columns = value

    @sample_rows_num.setter
    def sample_rows_num(self, value):
        """
        Set the number of rows in the sample dataframe.

        Args:
            value (int): The number of rows in the sample dataframe.
        """

        if value < 1:
            raise ValueError("Number of rows must be greater than 1")

        self._sample_rows_num = value

    def _prepare_file_path(self, file_name: str, file_type: FileType, landing_path: str) -> str:
        """
        Prepare the file path for the generated file.

        This envolves creating a directory where the file will be saved, if that directory does not exist.
        It also envolves creating a file name with the specified file type.

        Args:
            file_name (str): The name of the file to generate.
            file_type (FileType): The type of the file to generate.
            landing_path (str): The path where the generated file should be saved.

        Returns:
            str: The full file path.
        """

        os.makedirs(landing_path, exist_ok=True)
        return os.path.join(landing_path, f"{file_name}.{file_type.value}")

    def _save_and_scale_data(self, df_sample: DataFrame, full_file_name: str, file_type: FileType):
        """
        Save the dataframe to the specified file type and scale it to the target size.

        Args:
            df_sample (DataFrame): The dataframe to save.
            full_file_name (str): The full file path.
            file_type (FileType): The type of the file to generate.
        """

        def scale_data(df_sample: DataFrame, initial_size: float, file_type: FileType) -> DataFrame:
            """
            Scale the dataframe to the target size.

            Args:
                df_sample (DataFrame): The dataframe to scale.
                initial_size (float): The initial size of the dataframe in MB.
                file_type (FileType): The type of the file to generate.

            Returns:
                DataFrame: A pandas DataFrame scaled to the target size.
            """

            return (
                dataframe_multiplier(df_sample, initial_size, self.target_size_mb)
                if file_type != FileType.TURTLE
                else self.ttl_sampling.scale_ttl_file(df_sample, initial_size, self.target_size_mb)
            )

        self.save_dataframe(df_sample, full_file_name, file_type)
        initial_size = self.get_file_size_in_mb(full_file_name)

        df_scaled = scale_data(df_sample, initial_size, file_type)
        self.save_dataframe(df_scaled, full_file_name, file_type)

    @staticmethod
    def get_file_size_in_mb(file_path: str) -> float:
        """
        Get the file size in MB.

        Args:
            file_path (str): The path to the file.

        Returns:
            float: The file size in MB.
        """

        return os.path.getsize(file_path) / (1024 * 1024)

    @staticmethod
    def save_dataframe(df: Union[DataFrame, Graph], file_name: str, file_type: FileType):
        """
        Save the dataframe to the specified file type.

        Args:
            df (DataFrame): The dataframe to save.
            file_name (str): The name of the file to save.
            file_type (str): The type of the file to save.
        """

        match file_type:
            case FileType.CSV:
                df.to_csv(file_name, index=False)
            case FileType.JSON:
                df.to_json(file_name, orient="records")
            case FileType.PARQUET:
                df.to_parquet(file_name, index=False, engine="fastparquet")
            case FileType.GEOJSON:
                df.to_file(file_name, driver="GeoJSON")
            case FileType.TURTLE:
                df.serialize(destination=file_name, format="turtle")
            case FileType.AVRO:
                generate_avro_file(df, file_name)

    def generate_dataframe(self, values_type: ValuesType) -> DataFrame:
        """
        Generate a dataframe with the specified number of columns and rows.

        Args:
            values_type (ValuesType): The type of values the dataframe will contain.

        Returns:
            DataFrame: A pandas DataFrame with the specified number of columns and rows.
        """

        match values_type:
            case ValuesType.FLOAT:
                data = np.random.rand(self.sample_rows_num, self.num_columns).astype(np.float32)
            case ValuesType.INTEGER:
                data = np.random.randint(
                    0, 100, (self.sample_rows_num, self.num_columns), dtype=np.int32
                )
            case ValuesType.STRING:
                data = np.random.choice(["a", "b", "c"], (self.sample_rows_num, self.num_columns))

        return pd.DataFrame(data, columns=[f"col_{i}" for i in range(self.num_columns)])

    def generate_file(self, values_type: ValuesType, file_name: str, file_type: FileType, landing_path: str = "./"):
        """
        Generate a file with the specified file type and target size.

        This method generates a sample dataframe, scales it to the target size,
        and saves it to the specified file.

        Args:
            values_type (ValuesType): The type of values the dataframe will contain.
            file_name (str): The name of the file to generate.
            file_type (FileType): The type of the file to generate.
            landing_path (str, optional): The path where the generated files should be saved. Defaults to "./".
        """

        self.logger.info(f"Generating a {file_type.value} file {file_name} with size {self.target_size_mb} MB")

        match file_type:
            case FileType.GEOJSON:
                geojson_sampling = GeoJSONSampling()
                df_sample = geojson_sampling.generate_sample()
            case FileType.TURTLE:
                df_sample = self.ttl_sampling.sample_ttl_file(self.sample_rows_num)
            case _:
                df_sample = self.generate_dataframe(values_type)

        full_file_name = self._prepare_file_path(file_name, file_type, landing_path)
        self._save_and_scale_data(df_sample, full_file_name, file_type)

        self.logger.info("File generated successfully!")

    def generate_all_file_types(self, base_file_name: str, landing_path: str = "./"):
        """
        Generate a file for all file types.

        By default, the values type is set to ValuesType.STRING except for the GEOJSON file type.

        Args:
            base_file_name (str): The name of the file to generate.
            landing_path (str, optional): The path where the generated files should be saved. Defaults to "./".
        """

        self.logger.info("Generating files for all file types.")

        for file_type in FileType:

            values_type = ValuesType.STRING if file_type != FileType.GEOJSON else ValuesType.GEOMETRY
            self.generate_file(values_type, base_file_name, file_type, landing_path)

