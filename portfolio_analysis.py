import pandas as pd


def load_portfolio(file_path):
    """Load portfolio data from a CSV file."""
    return pd.read_csv(file_path)


def calculate_portfolio_metrics(portfolio):
    """Calculate basic portfolio metrics."""

    portfolio = portfolio.copy()

    # Calculate current value of each investment
    portfolio["Current_Value"] = (
        portfolio["Quantity"] * portfolio["Current_Price"]
    )

    # Calculate original investment value
    portfolio["Initial_Value"] = (
        portfolio["Quantity"] * portfolio["Purchase_Price"]
    )

    # Calculate profit or loss
    portfolio["Profit_Loss"] = (
        portfolio["Current_Value"] - portfolio["Initial_Value"]
    )

    # Calculate return percentage
    portfolio["Return_Percentage"] = (
        portfolio["Profit_Loss"]
        / portfolio["Initial_Value"]
        * 100
    )

    # Calculate total portfolio value
    total_value = portfolio["Current_Value"].sum()

    # Calculate portfolio allocation
    portfolio["Allocation_Percentage"] = (
        portfolio["Current_Value"]
        / total_value
        * 100
    )

    return portfolio, total_value
