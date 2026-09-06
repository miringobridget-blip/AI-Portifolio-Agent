import streamlit as st
import pandas as pd

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

# Load our simulated portfolio
portfolio = pd.read_csv("data/sample_portfolio.csv")

st.dataframe(
    portfolio,
    use_container_width=True
)
