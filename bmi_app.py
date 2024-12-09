import streamlit as st
import pandas as pd

st.title("Welcome to BMI calculator")

weight = st.number_input("Enter your weight in (Kgs)")
status = st.radio("Select your height format", ("cms","meters","feet"))
try:
    if status=="cms":
        height = st.number_input("centimeters")
        bmi = weight/((height/100)**2)
    elif status=="meters":
        height = st.number_input("metres")
        bmi = weight/((height)**2)
    elif status=="feet":
        height = st.number_input("feet")
        bmi = weight/((height/3.28)**2)
except:
    print("Zero Division Error")

if (st.button("calculate BMI")):
    st.write(f"Your BMI index is {round(bmi)}")

    if (bmi<16):
        st.error("You are extremly underweight")
    elif (bmi>=16 and bmi<25):
        st.warning("Your are underweight")
    elif (bmi>=25 and bmi<30):
        st.success("You are Healthy")
    elif bmi >= 30:
        st.error("You are overweight")
    st.balloons()