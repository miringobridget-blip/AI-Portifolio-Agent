import streamlit as st
import pandas as pd
from portfolio_analysis import load_portfolio, calculate_portfolio_metrics


st.set_page_config(
    page_title="AI Portfolio Manager",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Portfolio Manager")
st.subheader("Portfolio Management & Risk Monitoring Agent")

st.write(
    """
    This system analyses an investment portfolio, calculates
    performance and allocation, and identifies potential
    portfolio risks for human review.
    """
)

st.divider()

st.header("📁 Portfolio Data")

uploaded_file = st.file_uploader(
    "Upload your portfolio CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    portfolio = pd.read_csv(uploaded_file)

else:

    st.info("No file uploaded. The system will use the sample portfolio.")

    portfolio = load_portfolio("data/sample_portfolio.csv")


# Calculate portfolio metrics
portfolio_results, total_value = calculate_portfolio_metrics(portfolio)


st.header("📊 Portfolio Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Portfolio Value",
        f"${total_value:,.2f}"
    )

with col2:
    total_profit = portfolio_results["Profit_Loss"].sum()

    st.metric(
        "Total Profit / Loss",
        f"${total_profit:,.2f}"
    )

with col3:
    total_initial = portfolio_results["Initial_Value"].sum()

    total_return = (
        total_profit / total_initial * 100
    )

    st.metric(
        "Portfolio Return",
        f"{total_return:.2f}%"
    )


st.divider()

st.header("📋 Portfolio Analysis")

st.dataframe(
    portfolio_results,
    use_container_width=True
)


st.header("🥧 Portfolio Allocation")

allocation_chart = portfolio_results[
    ["Asset", "Allocation_Percentage"]
].set_index("Asset")

st.bar_chart(allocation_chart)


st.header("📈 Asset Returns")

return_chart = portfolio_results[
    ["Asset", "Return_Percentage"]
].set_index("Asset")

st.bar_chart(return_chart)


st.success(
    "Portfolio analysis completed successfully. "
    "Risk monitoring and AI recommendations will be added next."
)
