import streamlit as st

st.set_page_config(
    page_title="EMIPredict AI",
    page_icon="💳",
    layout="wide"
)

st.title("💳 EMIPredict AI")

st.markdown("""
## Intelligent EMI Eligibility & Affordability Prediction System

This project helps financial institutions evaluate:

- EMI Eligibility Classification
- Maximum Affordable EMI Prediction
- Customer Financial Risk Analysis

### Models Used

#### Classification
- Logistic Regression
- Random Forest
- XGBoost (Best Model)

#### Regression
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor (Best Model)

### Key Results

| Task | Best Model | Performance |
|--------|--------|--------|
| EMI Eligibility | XGBoost Classifier | 96.79% Accuracy |
| Max EMI Prediction | XGBoost Regressor | R² = 0.9923 |

---
Created using:
Python • Scikit-Learn • XGBoost • MLflow • Streamlit
""")