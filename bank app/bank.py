import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

df = pd.read_csv('bank.csv')

st.set_page_config(
    page_title="Real Time Data science Dashboard",
    page_icon=' ',
    layout='wide'
)

#Dashbord Title
st.title("Real Time/ Live Data science Dashbord")
#selection su le type de job
job_filter = st.selectbox("Select The job ",pd.unique(df['job']))

# Filtrage du job 
df = df[df['job']==job_filter]

# creation des kpi 
avg_age = np.mean(df.age)
count_married = int(df[df.marital=='married']["marital"].count())
balance = np.mean(df.balance)

kp1, kp2, kp3 = st.columns(3)
kp1.metric(label='Age',value=round(avg_age),delta=round(avg_age)-10)
kp2.metric(label="Married count", value=int(count_married),delta=-10+count_married)
kp3.metric(label="A/C Balance $", value=f"$ {round(balance, 2)}", delta=-round(balance/count_married)*100)

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.markdown("### First Chart")
    fig = px.density_heatmap(data_frame=df, y="age",x="marital")
    st.write(fig)
with fig_col2:
    st.markdown("### Second chart")
    fig2 = px.histogram(data_frame = df, x="age")
    st.write()

st.markdown("### Detailed Data view")
st.dataframe(df)

#time.sleep(1)
