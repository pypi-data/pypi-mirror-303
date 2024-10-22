# script dedicated to auxiliar methods

import pandas as pd

from pandas import DataFrame


def dataframe_multiplier(df_sample: DataFrame, file_size_mb: float, target_size_mb: float) -> DataFrame:
    """
    From a small dataframe, this function will return a new dataframe with a size that is closer to the
    target size.

    This methods uses the sample method if the file size to be created is too small, and the concat method
    if the file size to be created is too large.

    Args:
        df_sample (DataFrame): a small dataframe that will be used to create the new dataframe
        file_size_mb (float): the size of the file in MB
        target_size_mb (float): the target size of the file in MB

    Returns:
        DataFrame: a new dataframe with a size that is closer to the target size
    """

    scale = target_size_mb / file_size_mb

    if scale < 1:
        return df_sample.sample(frac=scale)
    else:
        return pd.concat([df_sample] * int(scale), ignore_index=True)
