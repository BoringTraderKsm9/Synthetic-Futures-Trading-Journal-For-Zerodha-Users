# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-22

### Added
- Initial release of Synthetic Futures Trading Journal
- **Data Cleaning Module** (`Data_Cleaning_Code.ipynb`)
  - Excel parsing for broker contract notes
  - F&O section extraction from multi-segment sheets
  - Symbol normalization (CE/PE suffix removal for synthetic futures)
  - Trade consolidation by instrument and exit date
  - Duplicate detection and prevention
  - SQLite database storage

- **Trading Journal Module** (`Trading_Journal_Final.ipynb`)
  - Comprehensive performance metrics calculation (25+ metrics)
  - Indian number formatting for all monetary values
  - Configurable trading cost deduction
  - Capital tracking and lot sizing recommendations

- **Interactive Visualizations**
  - Equity curve chart
  - Drawdown percentage chart
  - P&L distribution histogram
  - Monthly P&L bar chart
  - Win/Loss pie chart
  - Cumulative P&L chart
  - Combined dashboard with all charts

- **Reports Generation**
  - Metrics summary HTML page
  - Detailed trade summary table
  - Auto-opening in browser

- **Documentation**
  - Comprehensive README with setup instructions
  - MIT License
  - Contributing guidelines
  - .gitignore for Python/Jupyter projects

### Technical Details
- Python 3.8+ compatible
- Uses Plotly for interactive charts
- Pandas for data processing
- SQLite for persistent storage
- Matrix-inspired dark theme (black/green)

---

## Future Releases (Planned)

### [1.1.0] - TBD
- [ ] Support for multiple indices (BANKNIFTY, FINNIFTY)
- [ ] Trade tagging and categorization
- [ ] Export reports to PDF

### [1.2.0] - TBD
- [ ] Risk-adjusted metrics (Sharpe, Sortino, Calmar ratios)
- [ ] Monte Carlo simulation
- [ ] Automated daily report generation

### [2.0.0] - TBD
- [ ] Web-based dashboard interface
- [ ] Direct broker API integration
- [ ] Real-time P&L tracking
