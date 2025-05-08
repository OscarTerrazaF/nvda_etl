# load.py
import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame,
                   db_path: str = "nvda.db",
                   table_name: str = "gaps_nvda"):
    """
    Crea (o reemplaza) la tabla en SQLite y vuelca el DataFrame.
    """
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
