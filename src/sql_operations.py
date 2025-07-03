from sqlalchemy import create_engine
import pandas as pd

def save_to_sql(df, table_name, db_path="sqlite:////app/data/macadamia.db"):
    """Save Spark DF to SQLite database"""
    #convert spark dataframe to pandas dataframe for SQLAlchemy
    pandas_df = df.toPandas()
    engine = create_engine(db_path)
    pandas_df.to_sql(table_name, engine, if_exists="replace", index=False)