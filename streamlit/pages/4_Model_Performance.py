import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")

st.markdown("""
Comparison of all Classification and Regression models developed for the EMI Prediction System.
""")
############################# Classification Results ####################################
st.subheader("🎯 Classification Models")

classification_df = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy":[
        79.44,
        87.82,
        96.79
    ],
    "F1 Score":[
        84.38,
        90.20,
        96.30
    ]
})
############################# Classification Chart ############################
st.dataframe(
    classification_df,
    use_container_width=True
)
fig = px.bar(
    classification_df,
    x="Model",
    y="Accuracy",
    color="Model",
    text="Accuracy",
    title="Classification Accuracy Comparison"
)

fig.update_traces(
    texttemplate='%{text:.2f}%',
    textposition='outside'
)

st.plotly_chart(
    fig,
    use_container_width=True
)
############################# Regression Results ############################
st.subheader("💰 Regression Models")

regression_df = pd.DataFrame({
    "Model":[
        "Linear Regression",
        "Random Forest",
        "XGBoost"
    ],
    "RMSE":[
        4092.60,
        991.11,
        674.06
    ],
    "MAE":[
        2933.61,
        298.44,
        226.30
    ],
    "R²":[
        0.7163,
        0.9834,
        0.9923
    ]
})

st.dataframe(
    regression_df,
    use_container_width=True
)
############################# Regression Chart ############################
fig = px.bar(
    regression_df,
    x="Model",
    y="R²",
    color="Model",
    text="R²",
    title="Regression R² Comparison"
)

fig.update_traces(
    texttemplate='%{text:.4f}',
    textposition='outside'
)

st.plotly_chart(
    fig,
    use_container_width=True
)
################################### Best Models Section ##############################

st.subheader("🏆 Best Performing Models")

col1, col2 = st.columns(2)

with col1:

    st.success("""
    ### Classification Winner

    🥇 XGBoost Classifier

    Accuracy: 96.79%

    F1 Score: 96.30%
    """)

with col2:

    st.success("""
    ### Regression Winner

    🥇 XGBoost Regressor

    R² Score: 0.9923

    RMSE: 674.06
    """)

############################## Model Insights #################################
st.subheader("📌 Key Insights")

st.info("""
• XGBoost significantly outperformed Logistic Regression and Random Forest in EMI Eligibility Classification.

• XGBoost Regressor achieved an excellent R² score of 0.9923 for Maximum EMI Prediction.

• Feature Engineering improved predictive performance substantially.

• MLflow was used for experiment tracking and model management.
""")