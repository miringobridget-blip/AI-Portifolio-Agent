def generate_recommendation(
    portfolio_volatility,
    risk_level,
    risk_profile,
    performance_difference,
    high_concentration,
    overweight_assets,
    underweight_assets
):
    """
    Generate an AI-assisted portfolio recommendation
    using portfolio risk, performance, allocation,
    concentration and investor risk profile.
    """

    findings = []
    actions = []
    priority = "Low"

    # --------------------------------------------------------
    # 1. RISK PROFILE
    # --------------------------------------------------------

    acceptable_volatility = {
        "Conservative": 10,
        "Moderate": 20,
        "Aggressive": 30
    }

    threshold = acceptable_volatility.get(
        risk_profile,
        20
    )

    if portfolio_volatility > threshold:

        findings.append(
            f"Portfolio volatility of "
            f"{portfolio_volatility:.2f}% is above the "
            f"illustrative threshold for the "
            f"{risk_profile.lower()} investor profile."
        )

        actions.append(
            "Review portfolio risk and consider whether "
            "the current level of volatility is appropriate "
            "for the investor's objectives."
        )

        priority = "High"

    else:

        findings.append(
            f"Portfolio volatility of "
            f"{portfolio_volatility:.2f}% appears consistent "
            f"with the selected {risk_profile.lower()} "
            f"investor profile."
        )


    # --------------------------------------------------------
    # 2. CONCENTRATION RISK
    # --------------------------------------------------------

    if len(high_concentration) > 0:

        for _, row in high_concentration.iterrows():

            findings.append(
                f"{row['Asset']} represents "
                f"{row['Portfolio Weight (%)']:.2f}% "
                f"of the portfolio."
            )

            actions.append(
                f"Review the concentration of {row['Asset']} "
                f"and assess whether greater diversification "
                f"is appropriate."
            )

        priority = "High"


    # --------------------------------------------------------
    # 3. ALLOCATION
    # --------------------------------------------------------

    if len(overweight_assets) > 0:

        for _, row in overweight_assets.iterrows():

            findings.append(
                f"{row['Asset Class']} is overweight by "
                f"{row['Difference (%)']:.2f} percentage points."
            )

            actions.append(
                f"Review the allocation to "
                f"{row['Asset Class']} against the target allocation."
            )

        if priority != "High":
            priority = "Medium"


    if len(underweight_assets) > 0:

        for _, row in underweight_assets.iterrows():

            findings.append(
                f"{row['Asset Class']} is underweight by "
                f"{abs(row['Difference (%)']):.2f} percentage points."
            )

            actions.append(
                f"Review whether the allocation to "
                f"{row['Asset Class']} should be closer to "
                f"the target allocation."
            )

        if priority == "Low":
            priority = "Medium"


    # --------------------------------------------------------
    # 4. BENCHMARK PERFORMANCE
    # --------------------------------------------------------

    if performance_difference > 0:

        findings.append(
            f"The portfolio is outperforming the benchmark "
            f"by {performance_difference:.2f} percentage points."
        )

    elif performance_difference < 0:

        findings.append(
            f"The portfolio is underperforming the benchmark "
            f"by {abs(performance_difference):.2f} percentage points."
        )

        actions.append(
            "Review the portfolio's asset performance and "
            "allocation to understand the source of the "
            "underperformance."
        )

        if priority == "Low":
            priority = "Medium"

    else:

        findings.append(
            "The portfolio is performing approximately "
            "in line with the benchmark."
        )


    # --------------------------------------------------------
    # 5. OVERALL DIAGNOSIS
    # --------------------------------------------------------

    if priority == "High":

        diagnosis = (
            "The portfolio requires closer review because "
            "one or more significant risk indicators have "
            "been identified."
        )

    elif priority == "Medium":

        diagnosis = (
            "The portfolio shows some areas that may benefit "
            "from further review."
        )

    else:

        diagnosis = (
            "The portfolio appears relatively well aligned "
            "with the selected risk profile and current "
            "portfolio objectives."
        )


    # --------------------------------------------------------
    # 6. FINAL RECOMMENDATION
    # --------------------------------------------------------

    if priority == "High":

        recommendation = (
            "Conduct a detailed human review of portfolio "
            "risk, concentration and allocation before "
            "considering any investment changes."
        )

    elif priority == "Medium":

        recommendation = (
            "Review the identified allocation and performance "
            "issues and determine whether adjustments are "
            "appropriate."
        )

    else:

        recommendation = (
            "Continue monitoring portfolio performance, "
            "risk and allocation against the investor's "
            "objectives."
        )


    # --------------------------------------------------------
    # Return structured result
    # --------------------------------------------------------

    return {
        "priority": priority,
        "diagnosis": diagnosis,
        "findings": findings,
        "actions": actions,
        "recommendation": recommendation
    }
