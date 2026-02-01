import sys
import pandas as pd
from sqlalchemy import create_engine
from utils import build_db_url, normalize_columns

def validate_holdings_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure required columns exist and coerce types as needed.
    Returns a cleaned DataFrame with only required columns.
    """
    required_columns = {"date", "symbol", "quantity"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"The column(s) {missing_columns} are missing.")
    df = df[list(required_columns)].copy()
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

def load_holdings(csv_path: str) -> int:
    """
    Read a CSV and load rows into the holdings table.
    Returns the number of rows loaded.
    """
    df = pd.read_csv(csv_path)
    df = normalize_columns(df)
    df = validate_holdings_columns(df)
    
    engine = create_engine(build_db_url(), future=True)
    df.to_sql(
        "holdings",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000,
    )
    return len(df)

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python ingestion/load_holdings.py data/holdings.csv")
        return
    csv_path = sys.argv[1]
    rows = load_holdings(csv_path)
    print(f"Loaded {rows} rows into holdings")
    
if __name__ == "__main__":
    main()
