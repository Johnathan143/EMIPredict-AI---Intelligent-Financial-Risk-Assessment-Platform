import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 EDA Dashboard")

df = pd.read_csv("../data/emi_feature_engineered.csv")

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric("Missing Values", int(df.isnull().sum().sum()))

st.divider()

st.subheader("EMI Eligibility Distribution")
fig = px.histogram(
    df,
    x="emi_eligibility",
    color="emi_eligibility"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Credit Score Distribution")
fig = px.histogram(
    df,
    x="credit_score",
    nbins=30
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Salary Distribution")
fig = px.histogram(
    df,
    x="monthly_salary",
    nbins=30
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Credit Score vs Eligibility")
fig = px.box(
    df,
    x="emi_eligibility",
    y="credit_score",
    color="emi_eligibility"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Salary vs Eligibility")
fig = px.box(
    df,
    x="emi_eligibility",
    y="monthly_salary",
    color="emi_eligibility"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlation Heatmap")
corr = df.select_dtypes(
    include=["int64","float64"]
).corr()
fig = px.imshow(
    corr,
    text_auto=False,
    aspect="auto"
)
st.plotly_chart(fig, use_container_width=True)
