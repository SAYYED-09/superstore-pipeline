import sqlite3
import logging
import pandas as pd
from config import PROCESSED_DATA, DB_PATH, LOGS_PATH

log = logging.getLogger(__name__)

def load_db():
    log.info("Loading data into SQLite...")

    df = pd.read_csv(PROCESSED_DATA)
    log.info(f"Read {len(df)} rows from processed CSV")

    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    log.info("Table 'sales_data' created")

    count = conn.execute("SELECT COUNT(*) FROM sales_data").fetchone()[0]
    log.info(f"Verified: {count} rows in database")

    conn.close()
    log.info(f"Database saved to {DB_PATH}")
    return count

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
        handlers=[
            logging.FileHandler(LOGS_PATH / "pipeline.log"),
            logging.StreamHandler()
        ]
    )
    load_db()