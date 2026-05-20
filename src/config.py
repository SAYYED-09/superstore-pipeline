from pathlib import Path    

# Root of project
ROOT = Path(__file__).parent.parent

# Data paths
RAW_DATA      = ROOT / "data" / "raw" / "superstore.csv"
PROCESSED_DATA = ROOT / "data" / "processed" / "superstore_clean.csv"

# Database
DB_PATH       = ROOT / "data" / "superstore.db"

# Output
REPORTS_PATH  = ROOT / "reports"
LOGS_PATH     = ROOT / "logs"