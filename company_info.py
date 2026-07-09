from stock_data import get_stock_data


def get_company_profile(ticker):
    """Return a clean company profile for a ticker."""
    data = get_stock_data(ticker)

    return {
        "ticker": data["ticker"],
        "company_name": data["company_name"],
        "sector": data["sector"],
        "industry": data["industry"],
        "market_cap": data["market_cap"],
        "beta": data["beta"],
    }
