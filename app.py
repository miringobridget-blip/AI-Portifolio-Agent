import streamlit as st
import pandas as pd


# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Portfolio Manager",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📊 AI-Powered Portfolio Manager")

st.write(
    """
    An AI-assisted portfolio management and risk monitoring system.
    Upload a portfolio to analyse its performance.
    """
)

st.divider()


# ---------------------------------------------------
# Portfolio Input
# ---------------------------------------------------

st.header("📁 Portfolio Input")

uploaded_file = st.file_uploader(
    "Upload your portfolio CSV file",
    type=["csv"]
)


# ---------------------------------------------------
# Simulated Portfolio
# ---------------------------------------------------

sample_data = {
    "Asset": ["AAPL", "MSFT", "BND", "GLD", "SPY"],
    "Asset_Class": [
        "Equity",
        "Equity",
        "Bond",
        "Commodity",
        "ETF"
    ],
    "Quantity": [20, 10, 30, 15, 10],
    "Purchase_Price": [180, 400, 70, 180, 450],
    "Current_Price": [210, 430, 72, 190, 475]
}

sample_portfolio = pd.DataFrame(sample_data)


# ---------------------------------------------------
# Select portfolio
# ---------------------------------------------------

if uploaded_file is not None:

    portfolio = pd.read_csv(uploaded_file)

    st.success("Your portfolio has been uploaded successfully.")

else:

    portfolio = sample_portfolio

    st.info(
        "No portfolio uploaded. "
        "The system is currently using simulated data."
    )


# ---------------------------------------------------
# Calculate investment values
# ---------------------------------------------------

portfolio["Initial_Value"] = (
    portfolio["Quantity"]
    * portfolio["Purchase_Price"]
)

portfolio["Current_Value"] = (
    portfolio["Quantity"]
    * portfolio["Current_Price"]
)


# ---------------------------------------------------
# Calculate profit/loss
# ---------------------------------------------------

portfolio["Profit_Loss"] = (
    portfolio["Current_Value"]
    - portfolio["Initial_Value"]
)


# ---------------------------------------------------
# Calculate return percentage
# ---------------------------------------------------

portfolio["Return_Percentage"] = (
    portfolio["Profit_Loss"]
    / portfolio["Initial_Value"]
    * 100
)


# ---------------------------------------------------
# Total portfolio calculations
# ---------------------------------------------------

total_initial_value = portfolio["Initial_Value"].sum()

total_current_value = portfolio["Current_Value"].sum()

total_profit_loss = (
    total_current_value
    - total_initial_value
)

total_return = (
    total_profit_loss
    / total_initial_value
    * 100
)


# ---------------------------------------------------
# Portfolio Summary
# ---------------------------------------------------

st.divider()

st.header("📊 Portfolio Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Initial Value",
        f"${total_initial_value:,.2f}"
    )

with col2:
    st.metric(
        "Current Value",
        f"${total_current_value:,.2f}"
    )

with col3:
    st.metric(
        "Profit / Loss",
        f"${total_profit_loss:,.2f}"
    )

with col4:
    st.metric(
        "Portfolio Return",
        f"{total_return:.2f}%"
    )


# ---------------------------------------------------
# Portfolio Holdings
# ---------------------------------------------------

st.divider()

st.header("📋 Portfolio Analysis")

display_columns = [
    "Asset",
    "Asset_Class",
    "Quantity",
    "Purchase_Price",
    "Current_Price",
    "Initial_Value",
    "Current_Value",
    "Profit_Loss",
    "Return_Percentage"
]

st.dataframe(
    portfolio[display_columns],
    use_container_width=True
)


# ---------------------------------------------------
# Portfolio allocation
# ---------------------------------------------------

total_value = portfolio["Current_Value"].sum()

portfolio["Allocation_Percentage"] = (
    portfolio["Current_Value"]
    / total_value
    * 100
)


st.divider()

st.header("🥧 Portfolio Allocation")

allocation_chart = portfolio[
    ["Asset", "Allocation_Percentage"]
].set_index("Asset")

st.bar_chart(allocation_chart)


# ---------------------------------------------------
# Asset performance
# ---------------------------------------------------

st.header("📈 Asset Performance")

performance_chart = portfolio[
    ["Asset", "Return_Percentage"]
].set_index("Asset")

st.bar_chart(performance_chart)


# ---------------------------------------------------
# Completion message
# ---------------------------------------------------

st.success(
    "Portfolio performance analysis completed successfully."
)
