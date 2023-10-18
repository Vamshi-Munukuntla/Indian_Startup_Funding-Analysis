import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Startup_V01.csv', parse_dates=['Date'])


def load_overall_analysis():
    st.title(f"Overall Analysis")

    # total invested amount
    total = round(df['Amount'].sum())

    # max amount infused in a startup
    max_raised = round(df.groupby('Startup')['Amount'].max().sort_values(ascending=False).max())

    # avg amount infused in a startup
    avg_raised = round(df.groupby('Startup')['Amount'].sum().mean())

    # Number of Startups
    unique_startups = df['Startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('Total', f"{total} Cr")
    with col2:
        st.metric('Maximum', f"{max_raised} Cr")
    with col3:
        st.metric('Average', f"{avg_raised} Cr")
    with col4:
        st.metric('Number of Startups funded', f"{unique_startups} Cr" )
