import logging
import pandas as pd
from config import PROCESSED_DATA, LOGS_PATH

log = logging.getLogger(__name__)

def transform(df):
    log.info("Starting transformation...")

    # Derive time columns
    df['Year']    = df['Order Date'].dt.year
    df['Month']   = df['Order Date'].dt.month
    df['Quarter'] = df['Order Date'].dt.quarter
    log.info("Year, Month, Quarter derived")

    # Derive financial columns
    df['Profit_Margin_Pct'] = (df['Profit'] / df['Sales']) * 100
    df['Discount_Impact']   = df['Sales'] * df['Discount']
    log.info("Profit_Margin_Pct and Discount_Impact derived")

    # Save clean file
    PROCESSED_DATA.parent.mkdir(exist_ok=True)
    df.to_csv(PROCESSED_DATA, index=False)
    log.info(f"Saved to {PROCESSED_DATA}")

    log.info(f"Transform complete. {len(df)} rows saved.")
    return df

if __name__ == "__main__":
    from ingest import ingest
    from clean import clean
    df = transform(clean(ingest()))
    print(df[['Order Date','Year','Month','Quarter','Profit_Margin_Pct','Discount_Impact']].head())