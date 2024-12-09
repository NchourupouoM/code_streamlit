import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align:center;'> User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 1"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First name")
    l_name = col2.text_input("Last name")
    st.text_input("Email")
    st.text_input("Confirm Password")

    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    st_state = st.form_submit_button("Submit")
    if st_state:
        if f_name=="" and l_name == "":
            st.warning("Please fill above filds")
        else:
            st.success("Submitted successfully")
    p = st.sidebar.radio("select a style of graph",options=('line','bar','graph'))