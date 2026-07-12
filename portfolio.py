import pandas as pd

from stock_data import get_stock_data
from valuation import calculate_overvaluation_score, interpret_score


def read_portfolio(file_path="data/portfolio.csv"):
    """Read portfolio holdings from a CSV file."""
    return pd.read_csv(file_path)


def analyze_portfolio(file_path="data/portfolio.csv"):
    """Calculate portfolio values, gains, losses, and allocation."""
    portfolio = read_portfolio(file_path)
    holdings = []
    total_value = 0
    total_cost_basis = 0

    for _, row in portfolio.iterrows():
        ticker = str(row["ticker"]).upper().strip()
        shares = float(row["shares"])
        cost_basis = float(row["cost_basis"])

        stock_data = get_stock_data(ticker)
        current_price = stock_data.get("current_price")

        if current_price is None:
            position_value = 0
        else:
            position_value = shares * current_price

        cost_basis_total = shares * cost_basis
        gain_loss_dollars = position_value - cost_basis_total

        if cost_basis_total == 0:
            gain_loss_percent = 0
        else:
            gain_loss_percent = gain_loss_dollars / cost_basis_total

        score = calculate_overvaluation_score(stock_data)
        total_cost_basis += cost_basis_total

        holdings.append(
            {
                "ticker": ticker,
                "shares": shares,
                "cost_basis": cost_basis,
                "current_price": current_price,
                "position_value": position_value,
                "cost_basis_total": cost_basis_total,
                "gain_loss_dollars": gain_loss_dollars,
                "gain_loss_percent": gain_loss_percent,
                "overvaluation_score": score,
                "valuation_label": interpret_score(score),
                "allocation_percent": 0,
            }
        )

        total_value += position_value

    for holding in holdings:
        if total_value == 0:
            holding["allocation_percent"] = 0
        else:
            holding["allocation_percent"] = holding["position_value"] / total_value

    total_gain_loss = total_value - total_cost_basis

    if total_cost_basis == 0:
        total_gain_loss_percent = 0
    else:
        total_gain_loss_percent = total_gain_loss / total_cost_basis

    biggest_positions = sorted(
        holdings,
        key=lambda holding: holding["position_value"],
        reverse=True,
    )[:5]

    most_overvalued = sorted(
        holdings,
        key=lambda holding: holding["overvaluation_score"],
        reverse=True,
    )[:5]

    return {
        "holdings": holdings,
        "total_value": total_value,
        "total_cost_basis": total_cost_basis,
        "total_gain_loss": total_gain_loss,
        "total_gain_loss_percent": total_gain_loss_percent,
        "biggest_positions": biggest_positions,
        "most_overvalued": most_overvalued,
    }
