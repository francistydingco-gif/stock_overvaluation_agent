# Francis AI Investing

Francis AI Investing is a beginner-friendly Python CLI app for analyzing whether stocks may look overvalued, fairly valued, or undervalued based on simple public market data.

The current app uses Yahoo Finance data through `yfinance` and focuses on educational analysis. It does not give personalized financial advice.

## What It Does

- Looks up one stock by ticker symbol
- Fetches live market and company data
- Calculates a simple overvaluation score from 0 to 100
- Gives a cautious educational recommendation
- Reads a portfolio from `data/portfolio.csv`
- Calculates position value, gain/loss, and portfolio allocation
- Reads a watchlist from `data/watchlist.csv`
- Sorts watchlist stocks from least to most overvalued

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run The App

```bash
python main.py
```

On Mac, you can also double-click:

```text
Launch Francis AI Investing.command
```

For a faster portfolio-only view, double-click:

```text
Francis Portfolio.command
```

To place a shortcut on your Desktop, double-click:

```text
Install Desktop Shortcut.command
```

Then choose from the menu:

1. Analyze One Stock
2. Analyze Portfolio
3. Watchlist
4. Exit

## Portfolio CSV Format

Edit `data/portfolio.csv` with your own holdings:

```csv
ticker,shares,cost_basis
TSLA,1,200
NVDA,1,100
```

`cost_basis` means your average cost per share.

## Watchlist CSV Format

Edit `data/watchlist.csv` with tickers you want to monitor:

```csv
ticker
TSLA
NVDA
AMD
PLTR
```

## Current Limitations

- The valuation score is a simple educational model, not a professional valuation system
- Missing Yahoo Finance data can affect the score
- It does not include news, analyst estimates, discounted cash flow models, or portfolio risk optimization yet
- It is CLI-based only
- It does not use paid APIs or private brokerage data

## Next Planned Features

- Better portfolio report formatting
- Morning investment summary
- News summaries
- ETF and crypto support
- Remote daily report generation on a Mac Studio
- More detailed valuation models by sector
