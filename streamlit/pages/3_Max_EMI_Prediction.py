import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Max EMI Prediction",
    page_icon="💰",
    layout="wide"
)

regressor = joblib.load("../models/best_regressor.pkl")

st.title("💰 Maximum Affordable EMI Prediction")

with st.expander("👤 Personal Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=80,
            value=30
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    with col2:

        marital_status = st.selectbox(
            "Marital Status",
            ["Single", "Married"]
        )

        education = st.selectbox(
            "Education",
            [
                "High School",
                "Graduate",
                "Post Graduate"
            ]
        )

# -------------------------
# Employment Information
# -------------------------

with st.expander("💼 Employment Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        employment_type = st.selectbox(
            "Employment Type",
            ["Salaried", "Self Employed"]
        )

        years_of_employment = st.number_input(
            "Years of Employment",
            min_value=0.0,
            value=5.0
        )

    with col2:

        company_type = st.selectbox(
            "Company Type",
            ["Private", "Government"]
        )

# -------------------------
# Household Information
# -------------------------

with st.expander("🏠 Household Information", expanded=False):

    col1, col2 = st.columns(2)

    with col1:

        house_type = st.selectbox(
            "House Type",
            ["Owned", "Rented"]
        )

        family_size = st.number_input(
            "Family Size",
            min_value=1,
            value=4
        )

    with col2:

        dependents = st.number_input(
            "Dependents",
            min_value=0,
            value=2
        )

# -------------------------
# Financial Information
# -------------------------

with st.expander("💰 Financial Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        monthly_salary = st.number_input(
            "Monthly Salary",
            min_value=10000,
            value=50000
        )

        bank_balance = st.number_input(
            "Bank Balance",
            min_value=0,
            value=100000
        )

        emergency_fund = st.number_input(
            "Emergency Fund",
            min_value=0,
            value=50000
        )

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=900,
            value=700
        )

    with col2:

        monthly_rent = st.number_input(
            "Monthly Rent",
            value=10000
        )

        school_fees = st.number_input(
            "School Fees",
            value=2000
        )

        college_fees = st.number_input(
            "College Fees",
            value=0
        )

        travel_expenses = st.number_input(
            "Travel Expenses",
            value=3000
        )

        groceries_utilities = st.number_input(
            "Groceries & Utilities",
            value=8000
        )

        other_monthly_expenses = st.number_input(
            "Other Monthly Expenses",
            value=5000
        )

# -------------------------
# Loan Information
# -------------------------

with st.expander("🏦 Loan Information", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        existing_loans = st.selectbox(
            "Existing Loans",
            ["Yes", "No"]
        )

        current_emi_amount = st.number_input(
            "Current EMI Amount",
            value=0
        )

    with col2:

        requested_amount = st.number_input(
            "Requested Amount",
            value=500000
        )

        requested_tenure = st.number_input(
            "Requested Tenure (Months)",
            value=60
        )

        emi_scenario = st.selectbox(
            "EMI Scenario",
            [
                "Comfortable",
                "Moderate",
                "Risky"
            ]
        )
total_expenses = (
    monthly_rent
    + school_fees
    + college_fees
    + travel_expenses
    + groceries_utilities
    + other_monthly_expenses
)

debt_to_income_ratio = (
    current_emi_amount / monthly_salary
)

expense_ratio = (
    total_expenses / monthly_salary
)

savings_ratio = (
    (bank_balance + emergency_fund)
    / monthly_salary
)

financial_cushion = (
    bank_balance + emergency_fund
)

employment_stability = (
    years_of_employment * credit_score
)

loan_burden_ratio = (
    requested_amount / monthly_salary
)

available_income = (
    monthly_salary
    - total_expenses
    - current_emi_amount
)
input_df = pd.DataFrame({

    "age":[age],
    "gender":[gender],
    "marital_status":[marital_status],
    "education":[education],
    "monthly_salary":[monthly_salary],
    "employment_type":[employment_type],
    "years_of_employment":[years_of_employment],
    "company_type":[company_type],
    "house_type":[house_type],
    "monthly_rent":[monthly_rent],
    "family_size":[family_size],
    "dependents":[dependents],
    "school_fees":[school_fees],
    "college_fees":[college_fees],
    "travel_expenses":[travel_expenses],
    "groceries_utilities":[groceries_utilities],
    "other_monthly_expenses":[other_monthly_expenses],
    "existing_loans":[existing_loans],
    "current_emi_amount":[current_emi_amount],
    "credit_score":[credit_score],
    "bank_balance":[bank_balance],
    "emergency_fund":[emergency_fund],
    "emi_scenario":[emi_scenario],
    "requested_amount":[requested_amount],
    "requested_tenure":[requested_tenure],

    "total_expenses":[total_expenses],
    "debt_to_income_ratio":[debt_to_income_ratio],
    "expense_ratio":[expense_ratio],
    "savings_ratio":[savings_ratio],
    "financial_cushion":[financial_cushion],
    "employment_stability":[employment_stability],
    "loan_burden_ratio":[loan_burden_ratio],
    "available_income":[available_income]

})
predict_btn = st.button(
    "💰 Predict Maximum EMI",
    use_container_width=True
)
if predict_btn:

    prediction = regressor.predict(input_df)

    max_emi = prediction[0]
    st.markdown(
        f"""
        <div style="
            background-color:#14532d;
            padding:30px;
            border-radius:12px;
            text-align:center;
            color:white;
        ">
            <h2>💰 Maximum Affordable EMI</h2>
            <h1>₹ {max_emi:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Monthly Salary",
            f"₹{monthly_salary:,.0f}"
        )

    with col2:
        st.metric(
            "Available Income",
            f"₹{available_income:,.0f}"
        )

    with col3:
        st.metric(
            "Credit Score",
            credit_score
        )
    with col4:
        emi_percentage = (max_emi / monthly_salary) * 100
        st.metric(
            "EMI as % of Salary",
            f"{emi_percentage:.1f}%"
            )