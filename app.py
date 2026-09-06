import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="AI Portfolio Manager",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Portfolio Manager")

st.write(
    "This system analyses investment portfolios "
    "and provides decision-support insights."
)

st.divider()

st.header("📁 Portfolio")

# Find the project folder reliably
project_folder = Path(__file__).parent

# Build the path to our simulated portfolio
portfolio_file = project_folder / "data" / "sample_portfolio.csv"

# Load the portfolio
portfolio = pd.read_csv(portfolio_file)

# Display the portfolio
st.dataframe(
    portfolio,
    use_container_width=True
)

st.success("Portfolio data loaded successfully!")
