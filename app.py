import streamlit as st
import pandas as pd
# import time
#
# st.title('Indian Startup Dashboard')
# st.header('A Data Analysis Project')
# st.subheader('Created by Vamshi Kumar Munukuntla')
# st.write('Action Speaks Louder than Words.')
#
# st.markdown("""
# # markdown
# ## markdown
# ### markdown
# #### markdown
# ##### markdown
# """)
#
# st.code("""
# [i for in range(1,10)]
# """)
#
# st.write('x^2 + y^2 +2 = 0')
#
# st.latex('x^2 + y^2 +2 = 0')
#
# st.sidebar.title("Vamshi Kumar Munukuntla")
#
# col1, col2 = st.columns(2)
#
# with col1:
#     st.metric('Revenue', 'Rs 3L', '3%')
#
# with col2:
#     st.metric('Revenue', 'Rs 3L', '-3%')
#
# st.error('Login Failed')
#
# st.success('Login Successful')
#
# st.info('Info')
#
# st.warning('Warning')
#
# progress_bar = st.progress(0)
#
# for i in range(1, 101):
#     progress_bar.progress(i)
#
# email = st.text_input('Please Enter your Email: ')
# number = st.number_input('Please Enter Your Contact Number: ')
# date = st.date_input('Please Enter your Birth Date: ')
#

email = st.text_input('User name: ')
password = st.text_input('Password: ')
st.selectbox("Select Gender", ['male', 'female'])
st.radio("Select Gender", ['male', 'female'])
st.radio("Select Gender", ['male', 'female'], horizontal=True)

btn = st.button('Sign in')

if btn:
    if email == 'Vamshi' and password == 'V':
        st.success('Login Successful')
        st.balloons()
    else:
        st.error('Username or password is incorrect.')

file = st.file_uploader('Upload a CSV File')

if file is not None:
    df = pd.read_csv(file)
    st.write("Numerical", df.describe())
    st.write("Categorical", df.describe(include='O'))

