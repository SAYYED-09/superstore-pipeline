import sqlite3
import logging
import pandas as pd
from tabulate import tabulate
from pathlib import Path
from config import DB_PATH, REPORTS_PATH, LOGS_PATH

log = logging.getLogger(__name__)

SQL_DIR = Path(__file__).parent.parent / "sql"

def run_query(conn, sql):
    return pd.read_sql_query(sql, conn)

def split_queries(sql_text):
    queries = [q.strip() for q in sql_text.split(';') if q.strip()]
    return queries

def run_all():
    log.info("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)
    REPORTS_PATH.mkdir(exist_ok=True)

    sql_files = [
        "product_analysis.sql",
        "region_analysis.sql",
        "time_analysis.sql"
    ]

    for filename in sql_files:
        sql_path = SQL_DIR / filename
        log.info(f"Running {filename}...")
        print(f"\n{'='*60}")
        print(f" {filename.upper()}")
        print(f"{'='*60}")

        sql_text = sql_path.read_text()
        queries = split_queries(sql_text)

        for i, query in enumerate(queries):
            # Strip comment lines but keep query
            clean_query = '\n'.join(
                line for line in query.splitlines()
                if not line.strip().startswith('--')
            ).strip()
            if not clean_query:
                continue

            df = run_query(conn, clean_query)
            print(f"\n--- Query {i+1} ---")
            print(tabulate(df, headers='keys', tablefmt='rounded_outline', showindex=False))

            report_name = filename.replace('.sql', f'_q{i+1}.csv')
            df.to_csv(REPORTS_PATH / report_name, index=False)
            log.info(f"Saved {report_name}")

    conn.close()
    log.info("All queries complete. Reports saved.")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
        handlers=[
            logging.FileHandler(LOGS_PATH / "pipeline.log"),
            logging.StreamHandler()
        ]
    )
    run_all()        