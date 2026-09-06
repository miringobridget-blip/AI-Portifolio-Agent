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

# ---------------------------------------------------
# Risk & Volatility Analysis
# ---------------------------------------------------

st.divider()

st.header("⚠️ Risk & Volatility Analysis")

# Load simulated historical prices
historical_prices = pd.read_csv(
    "data/historical_prices.csv"
)

# Convert Date column to datetime
historical_prices["Date"] = pd.to_datetime(
    historical_prices["Date"]
)

# Set Date as the index
historical_prices = historical_prices.set_index("Date")


# Calculate weekly percentage returns
historical_returns = historical_prices.pct_change().dropna()


# Calculate annualised volatility
volatility = historical_returns.std() * (52 ** 0.5)


# Convert to percentage
volatility_percentage = volatility * 100


# Create risk table
risk_table = pd.DataFrame({
    "Asset": volatility_percentage.index,
    "Annualised Volatility (%)": volatility_percentage.values
})


# Sort from highest to lowest risk
risk_table = risk_table.sort_values(
    "Annualised Volatility (%)",
    ascending=False
)


# Display risk table
st.subheader("Asset Risk")

st.dataframe(
    risk_table,
    use_container_width=True
)


# ---------------------------------------------------
# Portfolio volatility
# ---------------------------------------------------

# Portfolio weights based on current portfolio value

portfolio_weights = (
    portfolio.set_index("Asset")["Current_Value"]
    / portfolio["Current_Value"].sum()
)


# Keep only assets that have historical prices
common_assets = portfolio_weights.index.intersection(
    historical_returns.columns
)

weights = portfolio_weights[common_assets]

returns_for_portfolio = historical_returns[
    common_assets
]


# Calculate portfolio historical returns
portfolio_returns = (
    returns_for_portfolio * weights
).sum(axis=1)


# Calculate annualised portfolio volatility
portfolio_volatility = (
    portfolio_returns.std() * (52 ** 0.5) * 100
)


st.subheader("Overall Portfolio Risk")

st.metric(
    "Annualised Portfolio Volatility",
    f"{portfolio_volatility:.2f}%"
)


# ---------------------------------------------------
# Risk classification
# ---------------------------------------------------

if portfolio_volatility < 10:

    risk_level = "Low"

elif portfolio_volatility < 20:

    risk_level = "Moderate"

else:

    risk_level = "High"


st.metric(
    "Portfolio Risk Level",
    risk_level
)


# ---------------------------------------------------
# Identify unusually risky assets
# ---------------------------------------------------

st.subheader("🚨 Risk Alerts")

high_risk_assets = risk_table[
    risk_table["Annualised Volatility (%)"] >= 20
]


if len(high_risk_assets) > 0:

    for _, row in high_risk_assets.iterrows():

        st.warning(
            f"{row['Asset']} has relatively high "
            f"annualised volatility of "
            f"{row['Annualised Volatility (%)']:.2f}%."
        )

else:

    st.success(
        "No unusually high-volatility assets "
        "were detected."
    )


# ---------------------------------------------------
# Volatility chart
# ---------------------------------------------------

st.subheader("📉 Asset Volatility")

volatility_chart = risk_table.set_index(
    "Asset"
)[["Annualised Volatility (%)"]]

st.bar_chart(
    volatility_chart
)


# ---------------------------------------------------
# Completion message
# ---------------------------------------------------

st.success(
    "Risk and volatility analysis completed successfully."
)
# ---------------------------------------------------
# Benchmark Comparison
# ---------------------------------------------------

st.divider()

st.header("📈 Benchmark Comparison")

# SPY is used as our simulated benchmark
benchmark_name = "SPY"

if benchmark_name in historical_returns.columns:

    # Calculate cumulative benchmark return
    benchmark_return = (
        (1 + historical_returns[benchmark_name]).prod() - 1
    ) * 100

    # Calculate cumulative portfolio return
    portfolio_return = (
        (1 + portfolio_returns).prod() - 1
    ) * 100

    # Difference between portfolio and benchmark
    performance_difference = (
        portfolio_return - benchmark_return
    )

    # Display results
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Portfolio Return",
            f"{portfolio_return:.2f}%"
        )

    with col2:
        st.metric(
            "Benchmark Return",
            f"{benchmark_return:.2f}%"
        )

    with col3:
        st.metric(
            "Difference",
            f"{performance_difference:+.2f}%"
        )

    # Interpretation
    if performance_difference > 0:

        st.success(
            f"✅ The portfolio outperformed the "
            f"{benchmark_name} benchmark by "
            f"{performance_difference:.2f} percentage points."
        )

    elif performance_difference < 0:

        st.warning(
            f"⚠️ The portfolio underperformed the "
            f"{benchmark_name} benchmark by "
            f"{abs(performance_difference):.2f} percentage points."
        )

    else:

        st.info(
            "The portfolio performed approximately "
            "in line with the benchmark."
        )

else:

    st.error(
        "Benchmark data is unavailable."
    )
# ---------------------------------------------------
# Portfolio Allocation & Over/Underweight Analysis
# ---------------------------------------------------

st.divider()

st.header("⚖️ Portfolio Allocation Analysis")

# Target allocation for our simulated portfolio
target_allocation = {
    "Equity": 50,
    "Bond": 25,
    "Commodity": 10,
    "ETF": 15
}

# Calculate current value by asset class
allocation_by_class = (
    portfolio.groupby("Asset_Class")["Current_Value"]
    .sum()
)

# Calculate percentage allocation
allocation_percentage = (
    allocation_by_class
    / portfolio["Current_Value"].sum()
    * 100
)

# Create allocation table
allocation_table = pd.DataFrame({
    "Asset Class": allocation_percentage.index,
    "Current Allocation (%)": allocation_percentage.values
})

# Add target allocation
allocation_table["Target Allocation (%)"] = (
    allocation_table["Asset Class"]
    .map(target_allocation)
)

# Calculate difference
allocation_table["Difference (%)"] = (
    allocation_table["Current Allocation (%)"]
    - allocation_table["Target Allocation (%)"]
)


# ---------------------------------------------------
# Classify allocation
# ---------------------------------------------------

def classify_allocation(difference):

    if difference > 5:
        return "Overweight"

    elif difference < -5:
        return "Underweight"

    else:
        return "Within Target"


allocation_table["Status"] = (
    allocation_table["Difference (%)"]
    .apply(classify_allocation)
)


# Round numbers
allocation_table["Current Allocation (%)"] = (
    allocation_table["Current Allocation (%)"].round(2)
)

allocation_table["Target Allocation (%)"] = (
    allocation_table["Target Allocation (%)"].round(2)
)

allocation_table["Difference (%)"] = (
    allocation_table["Difference (%)"].round(2)
)


# ---------------------------------------------------
# Display allocation table
# ---------------------------------------------------

st.subheader("Current vs Target Allocation")

st.dataframe(
    allocation_table,
    use_container_width=True
)


# ---------------------------------------------------
# Allocation alerts
# ---------------------------------------------------

st.subheader("🚨 Allocation Alerts")

overweight_assets = allocation_table[
    allocation_table["Status"] == "Overweight"
]

underweight_assets = allocation_table[
    allocation_table["Status"] == "Underweight"
]


if len(overweight_assets) > 0:

    for _, row in overweight_assets.iterrows():

        st.warning(
            f"⚠️ {row['Asset Class']} is overweight by "
            f"{row['Difference (%)']:.2f} percentage points."
        )


if len(underweight_assets) > 0:

    for _, row in underweight_assets.iterrows():

        st.info(
            f"ℹ️ {row['Asset Class']} is underweight by "
            f"{abs(row['Difference (%)']):.2f} percentage points."
        )


if len(overweight_assets) == 0 and len(underweight_assets) == 0:

    st.success(
        "✅ All asset classes are within the target allocation range."
    )


# ---------------------------------------------------
# Allocation chart
# ---------------------------------------------------

st.subheader("📊 Current vs Target Allocation")

allocation_chart = allocation_table.set_index(
    "Asset Class"
)[[
    "Current Allocation (%)",
    "Target Allocation (%)"
]]

st.bar_chart(allocation_chart)
# ---------------------------------------------------
# AI-Assisted Portfolio Recommendation
# ---------------------------------------------------

st.divider()

st.header("🤖 AI-Assisted Portfolio Recommendation")

st.write(
    """
    The recommendation engine reviews portfolio performance,
    risk and allocation results to provide decision-support insights.
    """
)


# ---------------------------------------------------
# Collect portfolio findings
# ---------------------------------------------------

recommendations = []


# Check allocation
if len(overweight_assets) > 0:

    for _, row in overweight_assets.iterrows():

        recommendations.append(
            f"{row['Asset Class']} is overweight by "
            f"{row['Difference (%)']:.2f} percentage points."
        )


if len(underweight_assets) > 0:

    for _, row in underweight_assets.iterrows():

        recommendations.append(
            f"{row['Asset Class']} is underweight by "
            f"{abs(row['Difference (%)']):.2f} percentage points."
        )


# Check portfolio risk
if portfolio_volatility >= 20:

    recommendations.append(
        f"Portfolio volatility is high at "
        f"{portfolio_volatility:.2f}%."
    )

elif portfolio_volatility >= 10:

    recommendations.append(
        f"Portfolio volatility is moderate at "
        f"{portfolio_volatility:.2f}%."
    )

else:

    recommendations.append(
        f"Portfolio volatility is relatively low at "
        f"{portfolio_volatility:.2f}%."
    )


# Check benchmark performance
if performance_difference > 0:

    recommendations.append(
        f"The portfolio is outperforming the benchmark "
        f"by {performance_difference:.2f} percentage points."
    )

elif performance_difference < 0:

    recommendations.append(
        f"The portfolio is underperforming the benchmark "
        f"by {abs(performance_difference):.2f} percentage points."
    )

else:

    recommendations.append(
        "The portfolio is performing approximately "
        "in line with the benchmark."
    )


# ---------------------------------------------------
# Display portfolio diagnosis
# ---------------------------------------------------

st.subheader("Portfolio Diagnosis")

for recommendation in recommendations:

    st.write(f"• {recommendation}")


# ---------------------------------------------------
# Generate recommendation
# ---------------------------------------------------

st.subheader("💡 Recommended Action")


if portfolio_volatility >= 20:

    st.warning(
        """
        The portfolio shows elevated risk.

        Consider reviewing highly volatile assets,
        portfolio concentration and the investor's
        risk tolerance before making any changes.
        """
    )

elif len(overweight_assets) > 0:

    st.warning(
        """
        The portfolio contains one or more overweight
        asset classes.

        Consider reviewing the current allocation against
        the investor's target allocation and risk objectives.
        """
    )

elif performance_difference < 0:

    st.info(
        """
        The portfolio is currently underperforming its
        benchmark.

        Review asset performance, allocation and risk
        before considering any portfolio adjustments.
        """
    )

else:

    st.success(
        """
        The portfolio appears reasonably aligned with
        the current target allocation and risk indicators.

        Continue monitoring performance and risk.
        """
    )


# ---------------------------------------------------
# Human Oversight Checkpoint
# ---------------------------------------------------

st.divider()

st.subheader("👤 Human Oversight Checkpoint")

st.warning(
    """
    IMPORTANT: This system provides AI-assisted decision support.
    It does not automatically execute trades or make final
    investment decisions.
    """
)


human_decision = st.radio(
    "How would you like to proceed?",
    [
        "Review recommendation",
        "Approve recommendation for further consideration",
        "Reject recommendation"
    ]
)


if human_decision == "Review recommendation":

    st.info(
        "Recommendation requires human review before any action."
    )

elif human_decision == "Approve recommendation for further consideration":

    st.success(
        "Recommendation marked for further human consideration."
    )

else:

    st.error(
        "Recommendation rejected by the human reviewer."
    )


# ---------------------------------------------------
# Disclaimer
# ---------------------------------------------------

st.caption(
    "This prototype is for educational and decision-support "
    "purposes only. It does not constitute financial advice."
)
