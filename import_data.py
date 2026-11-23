""" Module that imports the data """

import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

JETON_API = os.environ["JETON_API"]


def download_sources(url_fichier, cible):
    """Download url_fichier and write it to cible"""
    r = requests.get(url_fichier, timeout=120)
    r.raise_for_status()
    with open(cible, "wb") as f:
        f.write(r.content)


def get_melodi_indicator(
    code: str,
    value_name: str,
    API: str = JETON_API,
    dataset: str = "DS_FILOSOFI_CC",
    dimension: str = "FILOSOFI_MEASURE",
    time_period: int = 2023,
    geo_level: list = None,
) -> pd.DataFrame:
    if geo_level == None:
        geo_level = ["COM", "ARM"]

    url = f"https://api.insee.fr/melodi/data/{dataset}"

    params = {
        "GEO": geo_level,
        dimension: code,
        "TIME_PERIOD": time_period,
        "maxResult": 40000,
    }

    headers = {"Authorization": f"Bearer {JETON_API}"}

    response = requests.get(url, params=params, headers=headers, timeout=60)
    response.raise_for_status()
    observations = response.json()["observations"]

    df = pd.DataFrame(
        {
            "CODGEO": obs["dimensions"]["GEO"].split("-")[-1],
            value_name: obs["measures"]["OBS_VALUE_NIVEAU"].get("value"),
        }
        for obs in observations
    )

    return df
