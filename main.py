import streamlit as st
import pandas as pd
import investor_analysis as inv
import overall_analysis as oa

st.set_page_config(layout='wide', page_title='Startup Analysis')


df = pd.read_csv('Startup_V01.csv', parse_dates=['Date'])
st.sidebar.markdown('# Indian Startup Funding')
# st.dataframe(df.head())

st.sidebar.markdown('## Created by Vamshi Munukuntla')
st.sidebar.title('')
option = st.sidebar.radio('Analysis by', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    btn0 = st.sidebar.button('Show Overall Analysis')
    if btn0:
        oa.load_overall_analysis()
elif option == 'Startup':
    st.title('Startup Analysis')
    startup = st.sidebar.selectbox('Select startup', df['Startup'].sort_values().unique().tolist())
    btn1 = st.sidebar.button(f'Click here to know more about ***{startup}***')
else:
    st.title('Investor Analysis')
    unique_investors = sorted(set(df['Investors'].str.split(',').sum()))
    selected_investor = st.sidebar.selectbox('Select startup', [item.strip() for item in unique_investors][1:])
    btn2 = st.sidebar.button(f'Click here to know more about ***{selected_investor}***')
    if btn2:
        inv.load_investor_details(selected_investor)
