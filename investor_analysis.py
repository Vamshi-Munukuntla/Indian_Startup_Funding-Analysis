import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Startup_V01.csv', parse_dates=['Date'])


def load_investor_details(investor):
    st.markdown(f"## Investor:  {investor}")

    # Load the recent 5 Investments
    recent_5 = df[df['Investors'].str.contains(investor)].head()[
        ['Date', 'Startup', 'Vertical', 'Location', 'Investment_Round', 'Amount']]
    st.markdown('### 5 Recent Investments')
    st.dataframe(recent_5)

    col1, col2 = st.columns(2)
    with col1:
        # 5 Biggest Investments
        big_5 = df[df['Investors'].str.contains(investor)] \
            .groupby('Startup')['Amount'].sum().sort_values(ascending=False).head()
        st.markdown('### 5 Biggest Investments')
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.bar(big_5.index, big_5.values)
        st.pyplot(fig)

    # Top 5 Verticals
    with col2:
        value_counts = df[df['Investors'].str.contains(investor)].groupby('Vertical') \
            ['Amount'].sum().sort_values(ascending=False).head()
        st.markdown('### Top 5 Invested Sectors')
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=0, wedgeprops=dict(width=0.4))
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        rounds = df[df['Investors'].str.contains(investor)].groupby('Investment_Round') \
            ['Amount'].sum().sort_values(ascending=False).head()
        st.markdown('### Top 5 Invested Sectors')
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.pie(rounds, labels=rounds.index, autopct='%1.1f%%', startangle=0, wedgeprops=dict(width=0.4))
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

    with col2:
        # Investments Year wise
        df.loc[:, 'Year'] = df['Date'].dt.year
        big_5 = df[df['Investors'].str.contains(investor)].groupby('Year')['Amount'].sum()
        st.markdown('### YOY Investment')
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.plot(big_5.index, big_5.values)
        st.pyplot(fig)
