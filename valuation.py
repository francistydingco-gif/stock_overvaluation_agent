def add_risk_points(value, low_limit, high_limit, max_points):
    """Turn a metric into risk points between 0 and max_points."""
    if value is None:
        return max_points * 0.6

    if value <= low_limit:
        return 0
    if value >= high_limit:
        return max_points

    value_range = high_limit - low_limit
    value_position = value - low_limit
    return (value_position / value_range) * max_points


def score_growth_risk(revenue_growth, earnings_growth):
    """Score risk from missing, slow, or negative growth."""
    growth_values = []

    if revenue_growth is not None:
        growth_values.append(revenue_growth)
    if earnings_growth is not None:
        growth_values.append(earnings_growth)

    if not growth_values:
        return 15

    average_growth = sum(growth_values) / len(growth_values)

    if average_growth >= 0.20:
        return 0
    if average_growth >= 0.10:
        return 5
    if average_growth >= 0:
        return 10

    return 15


def score_price_position(current_price, high, low):
    """Score risk when price is close to the 52-week high."""
    if current_price is None or high is None or low is None or high == low:
        return 10

    position = (current_price - low) / (high - low)

    if position >= 0.90:
        return 15
    if position >= 0.75:
        return 10
    if position >= 0.50:
        return 5

    return 0


def calculate_overvaluation_score(stock_data):
    """Calculate an educational overvaluation risk score from 0 to 100."""
    score = 0

    score += add_risk_points(stock_data.get("trailing_pe"), 20, 80, 25)
    score += add_risk_points(stock_data.get("price_to_sales"), 3, 20, 20)
    score += score_growth_risk(
        stock_data.get("revenue_growth"),
        stock_data.get("earnings_growth"),
    )
    score += score_price_position(
        stock_data.get("current_price"),
        stock_data.get("fifty_two_week_high"),
        stock_data.get("fifty_two_week_low"),
    )
    score += add_risk_points(stock_data.get("beta"), 1.0, 2.5, 15)

    return min(round(score), 100)


def interpret_score(score):
    """Explain the score in plain English."""
    if score <= 30:
        return "Not obviously overvalued"
    if score <= 60:
        return "Fairly valued / mixed"
    if score <= 80:
        return "Looks overvalued"
    return "Very overvalued / speculative"
