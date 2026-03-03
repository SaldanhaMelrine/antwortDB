import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///database/olist.db",
    connect_args={"check_same_thread": False}
)


def run_query(sql):

    df = pd.read_sql(sql, engine)

    return df.to_dict(orient="records")
