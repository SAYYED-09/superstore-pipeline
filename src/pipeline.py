import logging
from config import LOGS_PATH
from ingest import ingest
from clean import clean
from transform import transform

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

if __name__ == "__main__":
    log.info("=" * 50)
    log.info("PIPELINE STARTED")
    log.info("=" * 50)

    df = ingest()
    df = clean(df)
    df = transform(df)

    log.info("=" * 50)
    log.info(f"PIPELINE COMPLETE — {len(df)} rows processed")
    log.info("=" * 50)