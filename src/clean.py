import logging
import pandas as pd
from config import LOGS_PATH

log = logging.getLogger(__name__)

def clean(df):
    log.info("Starting cleaning...")

    # Fix date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
    df['Ship Date']  = pd.to_datetime(df['Ship Date'],  format='mixed')
    log.info("Dates fixed")

    # Strip whitespace from strings
    str_cols = df.select_dtypes(include='object').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())
    log.info("Whitespace stripped")

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    log.info(f"Duplicates removed: {before - len(df)}")

    # Validate
    assert len(df) >= 9000, "Row count below 9000!"
    assert df['Order ID'].isnull().sum() == 0, "Nulls in Order ID!"
    assert df['Sales'].isnull().sum() == 0,    "Nulls in Sales!"
    assert df['Profit'].isnull().sum() == 0,   "Nulls in Profit!"
    log.info("All validations passed")

    log.info(f"Clean complete. {len(df)} rows ready.")
    return df

if __name__ == "__main__":
    from ingest import ingest
    df_raw = ingest()
    df_clean = clean(df_raw)
    print(df_clean.dtypes)