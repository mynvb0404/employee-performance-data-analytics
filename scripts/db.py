import pandas as pd
import math
from tqdm import tqdm
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def get_engine():
    connection_url = URL.create(
        "mssql+pyodbc",
        host=".",
        database="HR_Analysis",
        query={
            "driver": "ODBC Driver 17 for SQL Server",
            "trusted_connection": "yes",
        },
    )
    return create_engine(connection_url)

# save data to database
def save_to_sql(df, table_name, schema, engine, chunk_size=1000):
    total_chunks = math.ceil(len(df) / chunk_size)

    for i in tqdm(range(total_chunks), desc=table_name):
        chunk = df.iloc[i * chunk_size:(i + 1) * chunk_size]

        chunk.to_sql(
            name=table_name,
            schema=schema,
            con=engine,
            if_exists="replace" if i == 0 else "append",
            index=False,
        )
    print(table_name + ' imported ' + str(len(df)) + ' records')

# load data from database
def load_from_sql(table_name, schema, engine):
    query = 'SELECT * FROM {}.{}'.format(schema, table_name)
    return pd.read_sql(query, engine)