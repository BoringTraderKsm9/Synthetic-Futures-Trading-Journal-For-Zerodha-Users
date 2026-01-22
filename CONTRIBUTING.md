# Contributing to Synthetic Futures Trading Journal

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (sample data if possible, with sensitive info removed)
- **Describe the behavior you observed and what you expected**
- **Include your Python version and package versions**

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the proposed feature**
- **Explain why this enhancement would be useful**
- **Include mockups or examples if applicable**

### 🔧 Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding style below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

## 📝 Coding Style

### Python Guidelines

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Use type hints where appropriate

### Example:

```python
def calculate_drawdown(equity_series: pd.Series) -> pd.Series:
    """
    Calculate the drawdown percentage from peak equity.
    
    Args:
        equity_series: A pandas Series of equity values over time.
        
    Returns:
        A pandas Series of drawdown percentages.
    """
    peak = equity_series.cummax()
    drawdown = (equity_series - peak) / peak * 100
    return drawdown
```

### Jupyter Notebook Guidelines

- Clear all outputs before committing (or use `nbstripout`)
- Use markdown cells to document your code sections
- Keep cells focused on single tasks
- Include comments for complex logic

## 🧪 Testing

Before submitting:

1. Test with sample data to ensure basic functionality works
2. Test edge cases (empty data, missing columns, etc.)
3. Verify reports generate correctly
4. Check that no personal/sensitive data is included

## 📚 Documentation

- Update README.md if you add new features
- Add docstrings to new functions
- Include usage examples for new functionality

## 🏷️ Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Reference issue numbers when applicable

**Good examples:**
```
Add monthly returns calculation to metrics
Fix duplicate detection in data cleaning
Update README with new configuration options
```

## 📋 Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature request
- `documentation` - Documentation improvements
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed

## 🤔 Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

---

Thank you for helping make this project better! 🙌
