import yfinance as yf


def safe_get(data, key, default=None):
    """Return a value from a dictionary without crashing."""
    value = data.get(key, default)
    if value == "N/A":
        return default
    return value


def get_stock_data(ticker):
    """Fetch important stock data from Yahoo Finance."""
    ticker = ticker.upper().strip()
    stock = yf.Ticker(ticker)

    try:
        info = stock.info
    except Exception:
        info = {}

    current_price = safe_get(info, "currentPrice")
    if current_price is None:
        current_price = safe_get(info, "regularMarketPrice")

    previous_close = safe_get(info, "previousClose")

    # Recent price history can fill gaps when profile data is missing.
    try:
        history = stock.history(period="5d")
    except Exception:
        history = None

    if current_price is None and history is not None and not history.empty:
        current_price = history["Close"].iloc[-1]

    if previous_close is None and history is not None and len(history) >= 2:
        previous_close = history["Close"].iloc[-2]

    return {
        "ticker": ticker,
        "company_name": safe_get(info, "longName", ticker),
        "current_price": current_price,
        "previous_close": previous_close,
        "fifty_two_week_high": safe_get(info, "fiftyTwoWeekHigh"),
        "fifty_two_week_low": safe_get(info, "fiftyTwoWeekLow"),
        "market_cap": safe_get(info, "marketCap"),
        "trailing_pe": safe_get(info, "trailingPE"),
        "forward_pe": safe_get(info, "forwardPE"),
        "price_to_sales": safe_get(info, "priceToSalesTrailing12Months"),
        "beta": safe_get(info, "beta"),
        "sector": safe_get(info, "sector"),
        "industry": safe_get(info, "industry"),
        "revenue_growth": safe_get(info, "revenueGrowth"),
        "earnings_growth": safe_get(info, "earningsGrowth"),
    }


def format_large_number(value):
    """Format big numbers like market cap in a readable way."""
    if value is None:
        return "N/A"

    if value >= 1_000_000_000_000:
        return f"${value / 1_000_000_000_000:.2f}T"
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"

    return f"${value:,.2f}"


def format_percent(value):
    """Format decimal percentages from yfinance."""
    if value is None:
        return "N/A"
    return f"{value * 100:.2f}%"


def format_money(value):
    """Format money values safely."""
    if value is None:
        return "N/A"
    return f"${value:,.2f}"
