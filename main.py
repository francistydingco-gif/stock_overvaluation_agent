from recommendations import get_recommendation
from stock_data import format_large_number, format_money, format_percent, get_stock_data
from valuation import calculate_overvaluation_score, interpret_score
from portfolio import analyze_portfolio
from watchlist import analyze_watchlist


def print_stock_report(ticker):
    """Print a clean single-stock report."""
    stock = get_stock_data(ticker)
    score = calculate_overvaluation_score(stock)
    score_label = interpret_score(score)
    recommendation = get_recommendation(score)

    print("\n==============================")
    print("Stock Valuation Report")
    print("==============================")
    print(f"Ticker: {stock['ticker']}")
    print(f"Company: {stock['company_name']}")
    print(f"Sector: {stock['sector'] or 'N/A'}")
    print(f"Industry: {stock['industry'] or 'N/A'}")
    print()
    print(f"Current Price: {format_money(stock['current_price'])}")
    print(f"Previous Close: {format_money(stock['previous_close'])}")
    print(f"52-Week High: {format_money(stock['fifty_two_week_high'])}")
    print(f"52-Week Low: {format_money(stock['fifty_two_week_low'])}")
    print(f"Market Cap: {format_large_number(stock['market_cap'])}")
    print()
    print(f"Trailing P/E: {stock['trailing_pe'] or 'N/A'}")
    print(f"Forward P/E: {stock['forward_pe'] or 'N/A'}")
    print(f"Price/Sales: {stock['price_to_sales'] or 'N/A'}")
    print(f"Beta: {stock['beta'] or 'N/A'}")
    print(f"Revenue Growth: {format_percent(stock['revenue_growth'])}")
    print(f"Earnings Growth: {format_percent(stock['earnings_growth'])}")
    print()
    print(f"Overvaluation Score: {score}/100")
    print(f"Score Meaning: {score_label}")
    print(f"Educational Action: {recommendation['action']}")
    print(f"Note: {recommendation['note']}")
    print(f"Disclaimer: {recommendation['disclaimer']}")
    print()


def print_portfolio_report():
    """Print a simple portfolio summary."""
    try:
        portfolio = analyze_portfolio()
    except FileNotFoundError:
        print("\nCould not find data/portfolio.csv.")
        return

    print("\n==============================")
    print("Portfolio Summary")
    print("==============================")
    print(f"Total Portfolio Value: {format_money(portfolio['total_value'])}")
    print(f"Total Cost Basis: {format_money(portfolio['total_cost_basis'])}")
    print(f"Total Gain/Loss: {format_money(portfolio['total_gain_loss'])}")
    print(f"Total Gain/Loss %: {format_percent(portfolio['total_gain_loss_percent'])}")
    print()

    print("Biggest Positions")
    print("------------------------------")
    for holding in portfolio["biggest_positions"]:
        print(
            f"{holding['ticker']}: "
            f"{format_money(holding['position_value'])} "
            f"({format_percent(holding['allocation_percent'])})"
        )
    print()

    print("Most Overvalued By Model")
    print("------------------------------")
    for holding in portfolio["most_overvalued"]:
        print(
            f"{holding['ticker']}: "
            f"{holding['overvaluation_score']}/100 - "
            f"{holding['valuation_label']}"
        )
    print()

    print("All Holdings")
    print("------------------------------")
    for holding in portfolio["holdings"]:
        print(f"{holding['ticker']}")
        print(f"  Shares: {holding['shares']}")
        print(f"  Current Price: {format_money(holding['current_price'])}")
        print(f"  Position Value: {format_money(holding['position_value'])}")
        print(f"  Cost Basis Total: {format_money(holding['cost_basis_total'])}")
        print(f"  Gain/Loss: {format_money(holding['gain_loss_dollars'])}")
        print(f"  Gain/Loss %: {format_percent(holding['gain_loss_percent'])}")
        print(f"  Allocation: {format_percent(holding['allocation_percent'])}")
        print(f"  Overvaluation Score: {holding['overvaluation_score']}/100")
        print(f"  Valuation: {holding['valuation_label']}")
        print()


def print_watchlist_report():
    """Print a watchlist sorted from least to most overvalued."""
    try:
        watchlist = analyze_watchlist()
    except FileNotFoundError:
        print("\nCould not find data/watchlist.csv.")
        return

    print("\n==============================")
    print("Watchlist")
    print("==============================")
    print("Sorted from least to most overvalued by this simple model.")
    print()

    for stock in watchlist:
        print(f"{stock['ticker']} - {stock['company_name']}")
        print(f"  Current Price: {format_money(stock['current_price'])}")
        print(f"  Trailing P/E: {stock['trailing_pe'] or 'N/A'}")
        print(f"  Price/Sales: {stock['price_to_sales'] or 'N/A'}")
        print(f"  Score: {stock['overvaluation_score']}/100")
        print(f"  Valuation: {stock['valuation_label']}")
        print(f"  Educational Action: {stock['action']}")
        print()


def show_menu():
    """Show the main CLI menu."""
    print("==============================")
    print("Francis AI Investing")
    print("==============================")
    print("1. Analyze One Stock")
    print("2. Analyze Portfolio")
    print("3. Watchlist")
    print("4. Exit")


def main():
    """Run the command-line app."""
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            ticker = input("Enter ticker symbol: ")
            print_stock_report(ticker)
        elif choice == "2":
            print_portfolio_report()
        elif choice == "3":
            print_watchlist_report()
        elif choice == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nPlease choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
