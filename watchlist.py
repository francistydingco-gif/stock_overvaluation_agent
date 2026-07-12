import pandas as pd

from recommendations import get_recommendation
from stock_data import get_stock_data
from valuation import calculate_overvaluation_score, interpret_score


def read_watchlist(file_path="data/watchlist.csv"):
    """Read watchlist tickers from a CSV file."""
    return pd.read_csv(file_path)


def analyze_watchlist(file_path="data/watchlist.csv"):
    """Analyze each ticker in the watchlist."""
    watchlist = read_watchlist(file_path)
    results = []

    for _, row in watchlist.iterrows():
        ticker = str(row["ticker"]).upper().strip()
        stock_data = get_stock_data(ticker)
        score = calculate_overvaluation_score(stock_data)
        recommendation = get_recommendation(score)

        results.append(
            {
                "ticker": ticker,
                "company_name": stock_data.get("company_name"),
                "current_price": stock_data.get("current_price"),
                "trailing_pe": stock_data.get("trailing_pe"),
                "price_to_sales": stock_data.get("price_to_sales"),
                "overvaluation_score": score,
                "valuation_label": interpret_score(score),
                "action": recommendation["action"],
            }
        )

    results.sort(key=lambda item: item["overvaluation_score"])
    return results
