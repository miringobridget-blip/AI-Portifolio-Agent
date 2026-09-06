import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Portfolio Manager",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LANGUAGE SELECTION
# ============================================================

language = st.sidebar.selectbox(
    "🌍 Select Language / Sarudza Mutauro / Khetha Ulimi",
    [
        "English",
        "Français",
        "Shona",
        "Ndebele"
    ]
)


# ============================================================
# TRANSLATIONS
# ============================================================

translations = {

    "English": {

        "title": "📊 AI-Powered Portfolio Manager",
        "description": "An AI-assisted portfolio management and risk monitoring system.",

        "portfolio_input": "📁 Portfolio Input",
        "upload": "Upload your portfolio CSV file",

        "holdings": "📋 Portfolio Holdings",
        "summary": "📊 Portfolio Summary",

        "initial_value": "Initial Value",
        "current_value": "Current Value",
        "profit_loss": "Profit / Loss",
        "portfolio_return": "Portfolio Return",

        "risk": "⚠️ Risk & Volatility Analysis",
        "asset_risk": "Asset Risk",
        "overall_risk": "Overall Portfolio Risk",
        "portfolio_volatility": "Annualised Portfolio Volatility",
        "risk_level": "Portfolio Risk Level",
        "risk_alerts": "🚨 Risk Alerts",
        "asset_volatility": "📉 Asset Volatility",

        "benchmark": "📈 Benchmark Comparison",

        "allocation": "⚖️ Portfolio Allocation Analysis",
        "current_target": "Current vs Target Allocation",
        "allocation_alerts": "🚨 Allocation Alerts",

        "recommendation": "🤖 AI-Assisted Portfolio Recommendation",
        "diagnosis": "Portfolio Diagnosis",
        "recommended_action": "💡 Recommended Action",

        "human": "👤 Human Oversight Checkpoint",

        "review": "Review recommendation",
        "approve": "Approve recommendation for further consideration",
        "reject": "Reject recommendation",

        "upload_success": "Your portfolio has been uploaded successfully.",
        "using_sample": "No portfolio uploaded. The system is currently using simulated data.",

        "completed": "Portfolio analysis completed successfully.",
        "risk_completed": "Risk and volatility analysis completed successfully.",

        "disclaimer": "This prototype is for educational and decision-support purposes only. It does not constitute financial advice."
    },


    "Français": {

        "title": "📊 Gestionnaire de Portefeuille Alimenté par l'IA",
        "description": "Un système assisté par l'IA pour la gestion du portefeuille et le suivi des risques.",

        "portfolio_input": "📁 Données du portefeuille",
        "upload": "Téléchargez votre fichier CSV de portefeuille",

        "holdings": "📋 Actifs du portefeuille",
        "summary": "📊 Résumé du portefeuille",

        "initial_value": "Valeur initiale",
        "current_value": "Valeur actuelle",
        "profit_loss": "Profit / Perte",
        "portfolio_return": "Rendement du portefeuille",

        "risk": "⚠️ Analyse des risques et de la volatilité",
        "asset_risk": "Risque des actifs",
        "overall_risk": "Risque global du portefeuille",
        "portfolio_volatility": "Volatilité annualisée du portefeuille",
        "risk_level": "Niveau de risque du portefeuille",
        "risk_alerts": "🚨 Alertes de risque",
        "asset_volatility": "📉 Volatilité des actifs",

        "benchmark": "📈 Comparaison avec l'indice de référence",

        "allocation": "⚖️ Analyse de l'allocation du portefeuille",
        "current_target": "Allocation actuelle vs cible",
        "allocation_alerts": "🚨 Alertes d'allocation",

        "recommendation": "🤖 Recommandation assistée par l'IA",
        "diagnosis": "Diagnostic du portefeuille",
        "recommended_action": "💡 Action recommandée",

        "human": "👤 Contrôle humain",

        "review": "Examiner la recommandation",
        "approve": "Approuver la recommandation pour examen complémentaire",
        "reject": "Rejeter la recommandation",

        "upload_success": "Votre portefeuille a été téléchargé avec succès.",
        "using_sample": "Aucun portefeuille téléchargé. Le système utilise actuellement des données simulées.",

        "completed": "Analyse du portefeuille terminée avec succès.",
        "risk_completed": "Analyse des risques et de la volatilité terminée avec succès.",

        "disclaimer": "Ce prototype est destiné à des fins éducatives et d'aide à la décision uniquement. Il ne constitue pas un conseil financier."
    },


    "Shona": {

        "title": "📊 AI Portfolio Manager",
        "description": "Hurongwa hunoshandisa AI kubatsira pakutarisira portfolio uye kuongorora njodzi.",

        "portfolio_input": "📁 Portfolio Data",
        "upload": "Isa portfolio yako CSV file",

        "holdings": "📋 Investments dziri muPortfolio",
        "summary": "📊 Pfupiso yePortfolio",

        "initial_value": "Mari yekutanga",
        "current_value": "Mari iripo iye zvino",
        "profit_loss": "Purofiti / Kurasikirwa",
        "portfolio_return": "Portfolio Return",

        "risk": "⚠️ Kuongorora Njodzi neVolatility",
        "asset_risk": "Njodzi dzeInvestments",
        "overall_risk": "Njodzi yePortfolio yose",
        "portfolio_volatility": "Annualised Portfolio Volatility",
        "risk_level": "Chikamu cheNjodzi yePortfolio",
        "risk_alerts": "🚨 Nyevero dzeNjodzi",
        "asset_volatility": "📉 Volatility yeInvestments",

        "benchmark": "📈 Kuenzanisa neBenchmark",

        "allocation": "⚖️ Kuongorora Portfolio Allocation",
        "current_target": "Allocation iripo vs Target",
        "allocation_alerts": "🚨 Nyevero dzeAllocation",

        "recommendation": "🤖 AI-Assisted Portfolio Recommendation",
        "diagnosis": "Kuongororwa kwePortfolio",
        "recommended_action": "💡 Zano Rinokurudzirwa",

        "human": "👤 Kuongororwa neMunhu",

        "review": "Ongorora zano",
        "approve": "Gamuchira zano kuti riongororwe zvakare",
        "reject": "Ramba zano",

        "upload_success": "Portfolio yako yaiswa zvakanaka.",
        "using_sample": "Hapana portfolio yaiswa. Hurongwa huri kushandisa data rekuyedza.",

        "completed": "Portfolio analysis yapera zvakanaka.",
        "risk_completed": "Kuongororwa kwenjodzi nevolatility kwapera zvakanaka.",

        "disclaimer": "Iyi prototype ndeyekudzidza nekubatsira pakuita sarudzo chete. Haisi financial advice."
    },


    "Ndebele": {

        "title": "📊 AI Portfolio Manager",
        "description": "Uhlelo olusebenzisa i-AI ukuncedisa ekuphatheni i-portfolio lokuhlola ubungozi.",

        "portfolio_input": "📁 Portfolio Data",
        "upload": "Faka i-portfolio yakho njenge-CSV file",

        "holdings": "📋 Ama-Investments akuhlelo",
        "summary": "📊 Isifinyezo se-Portfolio",

        "initial_value": "Inani lokuqala",
        "current_value": "Inani lamanje",
        "profit_loss": "Inzuzo / Ilahleko",
        "portfolio_return": "Portfolio Return",

        "risk": "⚠️ Ukuhlolwa Kobungozi ne-Volatility",
        "asset_risk": "Ubungozi bama-Investments",
        "overall_risk": "Ubungozi be-Portfolio yonke",
        "portfolio_volatility": "Annualised Portfolio Volatility",
        "risk_level": "Izinga Lobungozi be-Portfolio",
        "risk_alerts": "🚨 Izexwayiso Zobungozi",
        "asset_volatility": "📉 Volatility yama-Investments",

        "benchmark": "📈 Ukuqhathanisa le-Benchmark",

        "allocation": "⚖️ Ukuhlolwa kwe-Portfolio Allocation",
        "current_target": "Allocation yamanje vs Target",
        "allocation_alerts": "🚨 Izexwayiso ze-Allocation",

        "recommendation": "🤖 AI-Assisted Portfolio Recommendation",
        "diagnosis": "Ukuhlolwa kwe-Portfolio",
        "recommended_action": "💡 Isinyathelo Esinconyiweyo",

        "human": "👤 Ukuhlolwa Ngumuntu",

        "review": "Hlola isincomo",
        "approve": "Vumela isincomo ukuthi sihlolwe futhi",
        "reject": "Yala isincomo",

        "upload_success": "I-portfolio yakho ifakwe ngempumelelo.",
        "using_sample": "Akukho portfolio efakiweyo. Uhlelo lusebenzisa idatha yokulingisa.",

        "completed": "Ukuhlolwa kwe-portfolio kuqediwe ngempumelelo.",
        "risk_completed": "Ukuhlolwa kobungozi ne-volatility kuqediwe ngempumelelo.",

        "disclaimer": "Le prototype ngeyokufunda kanye lokuncedisa ekuthatheni izinqumo kuphela. Ayisiyo financial advice."
    }
}


# Get selected language
t = translations[language]


# ============================================================
# TITLE
# ============================================================

st.title(t["title"])

st.write(t["description"])

st.divider()


# ============================================================
# PORTFOLIO INPUT
# ============================================================

st.header(t["portfolio_input"])

uploaded_file = st.file_uploader(
    t["upload"],
    type=["csv"]
)


# ============================================================
# SIMULATED PORTFOLIO
# ============================================================

sample_data = {

    "Asset": [
        "AAPL",
        "MSFT",
        "BND",
        "GLD",
        "SPY"
    ],

    "Asset_Class": [
        "Equity",
        "Equity",
        "Bond",
        "Commodity",
        "ETF"
    ],

    "Quantity": [
        20,
        10,
        30,
        15,
        10
    ],

    "Purchase_Price": [
        180,
        400,
        70,
        180,
        450
    ],

    "Current_Price": [
        210,
        430,
        72,
        190,
        475
    ]
}

sample_portfolio = pd.DataFrame(sample_data)


# ============================================================
# SELECT PORTFOLIO
# ============================================================

if uploaded_file is not None:

    portfolio = pd.read_csv(uploaded_file)

    st.success(t["upload_success"])

else:

    portfolio = sample_portfolio

    st.info(t["using_sample"])


# ============================================================
# PORTFOLIO CALCULATIONS
# ============================================================

portfolio["Initial_Value"] = (
    portfolio["Quantity"]
    * portfolio["Purchase_Price"]
)

portfolio["Current_Value"] = (
    portfolio["Quantity"]
    * portfolio["Current_Price"]
)

portfolio["Profit_Loss"] = (
    portfolio["Current_Value"]
    - portfolio["Initial_Value"]
)

portfolio["Return_Percentage"] = (
    portfolio["Profit_Loss"]
    / portfolio["Initial_Value"]
    * 100
)


# ============================================================
# TOTAL PORTFOLIO
# ============================================================

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


# ============================================================
# PORTFOLIO SUMMARY
# ============================================================

st.divider()

st.header(t["summary"])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        t["initial_value"],
        f"${total_initial_value:,.2f}"
    )

with col2:
    st.metric(
        t["current_value"],
        f"${total_current_value:,.2f}"
    )

with col3:
    st.metric(
        t["profit_loss"],
        f"${total_profit_loss:,.2f}"
    )

with col4:
    st.metric(
        t["portfolio_return"],
        f"{total_return:.2f}%"
    )


# ============================================================
# HOLDINGS
# ============================================================

st.divider()

st.header(t["holdings"])

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


# ============================================================
# PORTFOLIO ALLOCATION
# ============================================================

total_value = portfolio["Current_Value"].sum()

portfolio["Allocation_Percentage"] = (
    portfolio["Current_Value"]
    / total_value
    * 100
)

st.divider()

st.subheader(t["allocation"])

allocation_chart = portfolio[
    ["Asset", "Allocation_Percentage"]
].set_index("Asset")

st.bar_chart(allocation_chart)


# ============================================================
# ASSET PERFORMANCE
# ============================================================

st.subheader("📈 Asset Performance")

performance_chart = portfolio[
    ["Asset", "Return_Percentage"]
].set_index("Asset")

st.bar_chart(performance_chart)


# ============================================================
# HISTORICAL DATA
# ============================================================

historical_prices = pd.read_csv(
    "data/historical_prices.csv"
)

historical_prices["Date"] = pd.to_datetime(
    historical_prices["Date"]
)

historical_prices = historical_prices.set_index(
    "Date"
)

historical_returns = (
    historical_prices
    .pct_change()
    .dropna()
)


# ============================================================
# VOLATILITY
# ============================================================

st.divider()

st.header(t["risk"])

volatility = (
    historical_returns.std()
    * (52 ** 0.5)
)

volatility_percentage = (
    volatility * 100
)

risk_table = pd.DataFrame({

    "Asset":
        volatility_percentage.index,

    "Annualised Volatility (%)":
        volatility_percentage.values
})

risk_table = risk_table.sort_values(
    "Annualised Volatility (%)",
    ascending=False
)

st.subheader(t["asset_risk"])

st.dataframe(
    risk_table,
    use_container_width=True
)


# ============================================================
# PORTFOLIO RISK
# ============================================================

portfolio_weights = (
    portfolio
    .set_index("Asset")["Current_Value"]
    / portfolio["Current_Value"].sum()
)

common_assets = (
    portfolio_weights.index
    .intersection(historical_returns.columns)
)

weights = portfolio_weights[common_assets]

returns_for_portfolio = historical_returns[
    common_assets
]

portfolio_returns = (
    returns_for_portfolio
    * weights
).sum(axis=1)

portfolio_volatility = (
    portfolio_returns.std()
    * (52 ** 0.5)
    * 100
)

st.subheader(t["overall_risk"])

st.metric(
    t["portfolio_volatility"],
    f"{portfolio_volatility:.2f}%"
)


if portfolio_volatility < 10:

    risk_level = "Low"

elif portfolio_volatility < 20:

    risk_level = "Moderate"

else:

    risk_level = "High"


st.metric(
    t["risk_level"],
    risk_level
)


# ============================================================
# RISK ALERTS
# ============================================================

st.subheader(t["risk_alerts"])

high_risk_assets = risk_table[
    risk_table["Annualised Volatility (%)"] >= 20
]

if len(high_risk_assets) > 0:

    for _, row in high_risk_assets.iterrows():

        st.warning(
            f"⚠️ {row['Asset']} has relatively high "
            f"annualised volatility of "
            f"{row['Annualised Volatility (%)']:.2f}%."
        )

else:

    st.success(
        "No unusually high-volatility assets were detected."
    )


st.subheader(t["asset_volatility"])

volatility_chart = risk_table.set_index(
    "Asset"
)[["Annualised Volatility (%)"]]

st.bar_chart(volatility_chart)


# ============================================================
# BENCHMARK
# ============================================================

st.divider()

st.header(t["benchmark"])

benchmark_name = "SPY"

if benchmark_name in historical_returns.columns:

    benchmark_return = (
        (1 + historical_returns[benchmark_name]).prod()
        - 1
    ) * 100

    portfolio_return = (
        (1 + portfolio_returns).prod()
        - 1
    ) * 100

    performance_difference = (
        portfolio_return
        - benchmark_return
    )

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


# ============================================================
# TARGET ALLOCATION
# ============================================================

st.divider()

st.header(t["allocation"])

target_allocation = {

    "Equity": 50,
    "Bond": 25,
    "Commodity": 10,
    "ETF": 15
}

allocation_by_class = (
    portfolio
    .groupby("Asset_Class")["Current_Value"]
    .sum()
)

allocation_percentage = (
    allocation_by_class
    / portfolio["Current_Value"].sum()
    * 100
)

allocation_table = pd.DataFrame({

    "Asset Class":
        allocation_percentage.index,

    "Current Allocation (%)":
        allocation_percentage.values
})

allocation_table["Target Allocation (%)"] = (
    allocation_table["Asset Class"]
    .map(target_allocation)
)

allocation_table["Difference (%)"] = (
    allocation_table["Current Allocation (%)"]
    - allocation_table["Target Allocation (%)"]
)


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

allocation_table["Current Allocation (%)"] = (
    allocation_table["Current Allocation (%)"].round(2)
)

allocation_table["Target Allocation (%)"] = (
    allocation_table["Target Allocation (%)"].round(2)
)

allocation_table["Difference (%)"] = (
    allocation_table["Difference (%)"].round(2)
)


st.subheader(t["current_target"])

st.dataframe(
    allocation_table,
    use_container_width=True
)


# ============================================================
# ALLOCATION ALERTS
# ============================================================

st.subheader(t["allocation_alerts"])

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


if (
    len(overweight_assets) == 0
    and len(underweight_assets) == 0
):

    st.success(
        "✅ All asset classes are within the target allocation range."
    )


allocation_chart = allocation_table.set_index(
    "Asset Class"
)[[
    "Current Allocation (%)",
    "Target Allocation (%)"
]]

st.bar_chart(allocation_chart)


# ============================================================
# AI-ASSISTED RECOMMENDATION
# ============================================================

st.divider()

st.header(t["recommendation"])

st.write(
    """
    The recommendation engine reviews portfolio performance,
    risk and allocation results to provide decision-support insights.
    """
)

recommendations = []


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


# ============================================================
# DIAGNOSIS
# ============================================================

st.subheader(t["diagnosis"])

for recommendation in recommendations:

    st.write(f"• {recommendation}")


# ============================================================
# RECOMMENDED ACTION
# ============================================================

st.subheader(t["recommended_action"])


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
        """
    )


# ============================================================
# HUMAN OVERSIGHT
# ============================================================

st.divider()

st.subheader(t["human"])

st.warning(
    """
    IMPORTANT: This system provides AI-assisted decision support.
    It does not automatically execute trades or make final
    investment decisions.
    """
)

human_decision = st.radio(
    "Decision",
    [
        t["review"],
        t["approve"],
        t["reject"]
    ]
)


if human_decision == t["review"]:

    st.info(
        "Recommendation requires human review before any action."
    )

elif human_decision == t["approve"]:

    st.success(
        "Recommendation marked for further human consideration."
    )

else:

    st.error(
        "Recommendation rejected by the human reviewer."
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

st.success(t["completed"])

st.caption(t["disclaimer"])
