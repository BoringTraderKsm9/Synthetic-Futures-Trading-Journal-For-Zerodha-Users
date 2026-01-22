# 📈 Synthetic Futures Trading Journal

A comprehensive Python-based trading journal system for tracking, analyzing, and visualizing synthetic futures trades. This tool processes broker contract notes, consolidates trade data, and generates interactive performance reports with detailed metrics and charts.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## ✨ Features

### Data Processing (`Data_Cleaning_Code.ipynb`)
- **Excel Parsing**: Automatically extracts F&O trade data from broker contract notes
- **Symbol Normalization**: Cleans and standardizes option symbols (removes CE/PE suffixes for synthetic futures)
- **Trade Consolidation**: Groups multiple leg trades by instrument and exit date
- **Duplicate Prevention**: Intelligent duplicate detection when appending new data
- **SQLite Storage**: Persistent storage with automatic table management

### Trading Journal (`Trading_Journal_Final.ipynb`)
- **Performance Metrics**: 25+ key trading metrics including win rate, drawdown, streaks, and more
- **Indian Number Formatting**: All monetary values displayed in Indian numbering system (₹)
- **Cost Accounting**: Configurable per-lot trading costs deducted from P&L
- **Capital Tracking**: Tracks current capital, peak capital, and recommended lot sizing

### Interactive Visualizations
- **Equity Curve**: Track your account growth over time
- **Drawdown Chart**: Visualize percentage drawdowns from peak equity
- **P&L Distribution**: Histogram of trade outcomes
- **Monthly P&L**: Bar chart of monthly performance
- **Win/Loss Pie Chart**: Visual breakdown of trade outcomes
- **Cumulative P&L**: Running total of profits/losses
- **Combined Dashboard**: All charts in one comprehensive view

## 📊 Sample Metrics Output

```
Metrics Calculated (Net of Costs):
  Starting Capital: ₹14,00,000.00
  Total Trades: 150
  Winning Trades: 62
  Losing Trades: 88
  Winning Rate: 41.33%
  Avg Win: ₹45,386.87
  Avg Loss: ₹-27,614.35
  Win/Loss Ratio: 1.64
  Total Net P&L: ₹3,83,923.00
  Max Drawdown: ₹-5,94,382.50
  Max Drawdown %: -27.22%
  Max Win Streak: 5
  Max Loss Streak: 10
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas numpy plotly openpyxl
```

### Step 1: Data Cleaning

1. Export your broker's contract note/tradewise exits to Excel
2. Update the file path in `Data_Cleaning_Code.ipynb`:
   ```python
   file_path = r"path/to/your/contract_note.xlsx"
   sheet_name = "Tradewise Exits from YYYY-MM-DD"
   db_path = r"path/to/your/database.db"
   ```
3. Run all cells to clean and store data in SQLite

### Step 2: Generate Reports

1. Update the database path in `Trading_Journal_Final.ipynb`:
   ```python
   db_path = r"path/to/your/database.db"
   ```
2. Configure your trading parameters:
   ```python
   COST_PER_LOT = 10              # Your trading cost per lot
   HISTORICAL_LOT_SIZE = 75       # Lot size used in historical data
   CURRENT_LOT_SIZE = 6           # Current lot size for allocation
   STARTING_CAPITAL = 1_400_000   # Your starting capital
   ```
3. Run all cells to generate interactive HTML reports

## 📁 Project Structure

```
synthetic-futures-trading-journal/
│
├── Data_Cleaning_Code.ipynb    # Excel to SQLite data pipeline
├── Trading_Journal_Final.ipynb # Journal and report generation
├── README.md                   # This file
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
├── .gitignore                  # Git ignore patterns
│
├── sample_data/                # Sample data for testing (optional)
│   └── sample_trades.xlsx
│
└── trading_reports_net_final/  # Generated reports (created on run)
    ├── metrics.html
    ├── trade_summary.html
    ├── dashboard_net.html
    ├── equity_net.html
    ├── drawdown_pct.html
    ├── pnl_dist_net.html
    ├── monthly_pnl_net.html
    ├── winloss_pie_net.html
    └── cumulative_net_pnl.html
```

## 🎨 Theme

The reports feature a sleek **Matrix-inspired** dark theme with:
- Black background (`#000000`)
- Bright green text and accents (`#00FF41`)
- Red for losses (`#FF0000`)
- Yellow highlights for neutral values (`#FFFF00`)

## 📋 Database Schema

The SQLite database uses a single table `fo_consolidated_data`:

| Column | Type | Description |
|--------|------|-------------|
| Entry Date | TEXT | Trade entry date (DD-MM-YYYY) |
| Exit Date | TEXT | Trade exit date (DD-MM-YYYY) |
| Symbol | TEXT | Cleaned instrument symbol |
| Quantity | REAL | Total quantity traded |
| Buy Value | REAL | Total buy value |
| Sell Value | REAL | Total sell value |
| Profit | REAL | Gross profit/loss |
| Turnover | REAL | Total turnover |

## 🔧 Configuration Options

### Data Cleaning
- `file_path`: Path to your Excel contract note
- `sheet_name`: Name of the sheet containing trade data
- `db_path`: SQLite database file path

### Trading Journal
- `STARTING_CAPITAL`: Your initial trading capital
- `HISTORICAL_LOT_SIZE`: Lot size for historical cost calculation
- `CURRENT_LOT_SIZE`: Current lot size for capital allocation metrics
- `COST_PER_LOT`: Trading costs (brokerage, taxes, etc.) per lot

## 🛣️ Roadmap

- [ ] Add support for multiple instruments/indices
- [ ] Implement trade tagging and categorization
- [ ] Add risk-adjusted metrics (Sharpe, Sortino ratios)
- [ ] Create automated daily/weekly report generation
- [ ] Add support for direct broker API integration
- [ ] Build a web-based dashboard interface

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is for educational and informational purposes only. It is not financial advice. Trading in futures and options involves substantial risk of loss and is not suitable for all investors. Past performance is not indicative of future results. Always consult with a qualified financial advisor before making any investment decisions.

## 🙏 Acknowledgments

- Built with [Plotly](https://plotly.com/) for interactive visualizations
- Data processing powered by [Pandas](https://pandas.pydata.org/)
- This is my first "vibe coded" project - created through iterative AI-assisted development

---

**Made with ❤️ for the trading community**
