# loader.py
import requests
import pandas as pd

def load_data():
    url = "https://data.opendatasoft.com/api/records/1.0/search/"
    params = {
        "dataset": "elections-france-presidentielles-2022-1er-tour-par-bureau-de-vote@public",
        "rows": 10000
    }

    response = requests.get(url, params=params)
    data = response.json()
    records = data["records"]
    rows = [rec["fields"] for rec in records]

    df = pd.DataFrame(rows)
    return df
