# Custom imports
import sys  
sys.path.insert(1, '..')
from sensitive_info import *

# SQL imports
import pandas as pd
from sqlalchemy import create_engine, URL
from sqlalchemy.sql import text

def load_postgresql_data():
    # create SQLAlchemy engine
    url_object = URL.create(
        drivername="postgresql+psycopg2",
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
        port=PORT
    )
    engine = create_engine(url=url_object)

    # connect to database and extract data to dataframe
    train_df = None
    test_df = None
    with engine.connect() as db_conn:
        sql_query = "SELECT * FROM watson.train"
        train_df = pd.read_sql_query(sql=text(sql_query), con=db_conn)

        sql_query = "SELECT * FROM watson.test"
        test_df = pd.read_sql_query(sql=text(sql_query), con=db_conn)

    return train_df, test_df