import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from test_db_connection import build_db_url

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

def validate_price_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure required columns exist and coerce types as needed.
    Returns a cleaned DataFrame with only required columns
    """
    required_columns = {"date", "symbol", "close_price"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"The column(s) {missing_columns} are missing.")
    
    df = df[list(required_columns)].copy()
    # Convert the date column from strings to date objects
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

def load_prices(csv_path: str) -> int:
    """
    Read a CSV and load rows into the prices table.
    Returns the number of rows loaded.
    """


def main() -> None:
    return


if __name__ == "__main__":
    main()
