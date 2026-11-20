""" Checks  """

import pandas as pd

def check_code_commune_formatting(df: pd.dataframe) -> None:
    """
    Checks the city code in the entire dataset
    """
    assert (df['code_commune'].apply(len) == 5).all()
