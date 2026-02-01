import os
from sqlalchemy import create_engine, text

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

def main() -> None:
  # Create engine to open a database connection
  engine = create_engine(build_db_url(), future=True)
  with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(f"Connection OK, SELECT 1 -> {result.scalar()}")

if __name__ == "__main__":
  main()
