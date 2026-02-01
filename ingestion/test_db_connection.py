import os
from sqlalchemy import create_engine, text

def build_db_url() -> str:
  '''
  Build a PostgreSQL connection string from environmental variables.
  Falls back to local defaults (localhost, 5432, portfolio_db) unless specified.
  Returns SQLAlchemy-compatible connection string.
  '''
  user = os.getenv("PGUSER", os.getenv("USER", ""))
  password = os.getenv("PGPASSWORD", os.getenv("PASSWORD", ""))
  host = os.getenv("PGHOST", "localhost")
  port = os.getenv("PGPOST", 5432)
  dbname = os.getenv("PGDATABASE", "portfolio_db")

  auth = f"{user}:{password}" if password else f"{user}"
  return f"postresql+psycopg://{auth}@{host}:{port}/{dbname}"

def main() -> None:
  return

if __name__ == "__main__":
  main()