def get_recommendation(score):
    """Return cautious educational analysis based on the valuation score."""
    if score <= 30:
        action = "BUY / DCA"
        note = "The stock does not look obviously overvalued from these simple metrics."
    elif score <= 60:
        action = "HOLD"
        note = "The valuation picture is mixed, so patience and position sizing matter."
    elif score <= 80:
        action = "HOLD / WAIT FOR PULLBACK"
        note = "The stock shows signs of being expensive compared with its fundamentals."
    else:
        action = "TRIM / REVIEW POSITION"
        note = "The stock looks highly valued or speculative, so review risk carefully."

    return {
        "action": action,
        "note": note,
        "disclaimer": "Educational analysis only, not personalized financial advice.",
    }
