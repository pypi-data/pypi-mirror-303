from sqlalchemy import create_engine
from utsam.bases.params import SemesterParams, _CACHE_


def create_pg_engine(
    database_type: str,
    username: str,
    password: str,
    host: str,
    port: str,
    database_name: str,
    echo = False
    ):
    # Create a connection string
    connection_string = f'{database_type}://{username}:{password}@{host}:{port}/{database_name}'

    # Create a database engine
    return create_engine(connection_string, pool_size=10, max_overflow=0, echo=echo)

import os
import pandas as pd


def load_data(table_name, engine, load_cache=True):
    file_path = f"{_CACHE_}/{table_name}.csv"
    if not load_cache and os.path.isfile(file_path):
        return pd.read_csv(file_path)

    df = pd.read_sql(
        f"SELECT * FROM {table_name};",
        engine
    )
    df.to_csv(file_path, index=False)
    return df
