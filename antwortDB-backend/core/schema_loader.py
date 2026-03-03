from sqlalchemy import create_engine, inspect

DB_PATH = "sqlite:///database/olist.db"


def load_schema():

    engine = create_engine(DB_PATH)
    inspector = inspect(engine)

    schema = {}

    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        schema[table] = [c["name"] for c in columns]

    return schema