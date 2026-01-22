# Configuration Template for Synthetic Futures Trading Journal
# Copy this file to config.py and update with your actual values

# =============================================================================
# DATA CLEANING CONFIGURATION
# =============================================================================

# Path to your broker's Excel contract note
EXCEL_FILE_PATH = r"path/to/your/contract_note.xlsx"

# Name of the sheet containing tradewise exits
# Common formats: "Tradewise Exits from YYYY-MM-DD", "FO Trades", etc.
SHEET_NAME = "Tradewise Exits from 2024-07-01"

# Path for SQLite database (will be created if doesn't exist)
DATABASE_PATH = r"path/to/your/trading_journal.db"

# Table name in SQLite database
TABLE_NAME = "fo_consolidated_data"


# =============================================================================
# TRADING JOURNAL CONFIGURATION
# =============================================================================

# Your starting/initial trading capital (in INR)
STARTING_CAPITAL = 1_400_000  # ₹14 Lakhs

# Historical lot size used for cost calculation
# NIFTY lot size history:
#   - Before Jul 2015: 50
#   - Jul 2015 - Mar 2021: 75
#   - Apr 2021 - Nov 2024: 50
#   - Dec 2024 onwards: 75 (Check NSE for latest)
HISTORICAL_LOT_SIZE = 75

# Current lot size for capital allocation metrics
CURRENT_LOT_SIZE = 75

# Total trading cost per lot (in INR)
# This includes: Brokerage, STT, Exchange fees, GST, Stamp duty, etc.
# Typical ranges:
#   - Discount broker (Zerodha, Upstox): ₹40-80 per lot roundtrip
#   - Full-service broker: ₹100-200+ per lot roundtrip
COST_PER_LOT = 50

# Output directory for generated reports
REPORTS_OUTPUT_DIRECTORY = "trading_reports"


# =============================================================================
# BROWSER CONFIGURATION (Optional)
# =============================================================================

# Path to Microsoft Edge (if you want to use Edge specifically)
# Set to None to use system default browser
EDGE_BROWSER_PATH = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"


# =============================================================================
# DISPLAY CONFIGURATION
# =============================================================================

# Color theme for reports (Matrix-style dark theme is default)
COLOR_PALETTE = {
    'background': '#000000',      # Black background
    'text': '#00FF41',            # Bright green text
    'primary': '#00FF41',         # Green for charts/titles
    'success': '#00FF41',         # Green for winning trades
    'danger': '#FF0000',          # Red for losses
    'warning': '#FFFF00',         # Yellow for highlights
    'surface': '#00FF41'          # Green for borders
}


# =============================================================================
# NOTES
# =============================================================================
#
# 1. IMPORTANT: Never commit this file with real paths/data to GitHub!
#    Use config_template.py as the template and add config.py to .gitignore
#
# 2. Synthetic Futures: This tool treats CE+PE options on the same strike
#    as a synthetic future. The data cleaning code removes CE/PE suffixes
#    to consolidate them.
#
# 3. Cost Calculation: Costs are calculated as (Lots × COST_PER_LOT)
#    Make sure to include ALL costs in COST_PER_LOT for accurate P&L
#
# 4. Database: SQLite is used for simplicity. The database file contains
#    your actual trade data, so keep it secure and backed up.
#
