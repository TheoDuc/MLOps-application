"""Checks if the entire project works well"""

import pandas as pd


def check_code_commune_formatting(df: pd.DataFrame) -> None:
    """
    Checks the city code in the entire dataset
    """
    assert (df["code_commune"].apply(len) == 5).all()


def check_missing_values_col(df: pd.DataFrame, col: str) -> None:
    pass


def check_unseen_categories(df: pd.DataFrame, test: pd.DataFrame) -> None:
    pass


def check_missing_values(df: pd.DataFrame) -> None:
    pass
