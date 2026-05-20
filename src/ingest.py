import logging
import pandas as pd
from config import RAW_DATA, LOGS_PATH

# Setup logging
LOGS_PATH.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler(LOGS_PATH / "pipeline.log"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

def ingest():
    log.info("Starting ingestion...")
    df = pd.read_csv(RAW_DATA, encoding='latin-1')
    log.info(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
    log.info(f"Columns: {list(df.columns)}")
    return df

if __name__ == "__main__":
    df = ingest()
    print(df.head())