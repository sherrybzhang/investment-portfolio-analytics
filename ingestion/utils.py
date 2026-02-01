import os
import pandas as pd

def build_db_url() -> str:
    """
    Build a PostgreSQL connection string from environment variables.
    Falls back to local defaults (localhost, 5432, portfolio_db) unless specified.
    Returns a SQLAlchemy-compatible connection string.
    """
    user = os.getenv("PGUSER", os.getenv("USER", ""))
    password = os.getenv("PGPASSWORD", "")
    host = os.getenv("PGHOST", "localhost")
    port = os.getenv("PGPORT", "5432")
    dbname = os.getenv("PGDATABASE", "portfolio_db")

    auth = f"{user}:{password}" if password else f"{user}"
    return f"postgresql+psycopg://{auth}@{host}:{port}/{dbname}"

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize column names (e.g., lowercase, underscores).
    """
    new_cols = []
    for col in df.columns:
        cleaned = col.strip().lower().replace(" ", "_")
        new_cols.append(cleaned)

    df.columns = new_cols
    return df
