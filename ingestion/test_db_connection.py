from sqlalchemy import create_engine, text
from utils import build_db_url

def main() -> None:
    # Create engine to open a database connection
    engine = create_engine(build_db_url(), future=True)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(f"Connection OK, SELECT 1 -> {result.scalar()}")

if __name__ == "__main__":
    main()
