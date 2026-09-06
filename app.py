import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="AI Portfolio Manager",
    page_icon="📊",
    layout="wide"
)


st.title("📊 AI-Powered Portfolio Manager")

st.write(
    """
    An AI-assisted portfolio management and risk monitoring system.
    Upload a portfolio to begin the analysis.
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
# Choose portfolio
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
# Display portfolio
# ---------------------------------------------------

st.subheader("Portfolio Holdings")

st.dataframe(
    portfolio,
    use_container_width=True
)


st.success("Portfolio data loaded successfully!")
