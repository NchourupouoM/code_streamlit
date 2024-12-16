import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout='wide'
)

df = pd.read_csv("india.csv")
list_of_state = list(df['State'].unique())
list_of_state.insert(0,"overall India")

st.sidebar.title("India Data viz")
selected_state = st.sidebar.selectbox("select a state",list_of_state)
primary = st.sidebar.selectbox("Select first Parameter: ", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select secondary Parameter: ", sorted(df.columns[5:]))

plot = st.sidebar.button("Plot a graph")
if plot:
    st.text("Size represent primary parameter")
    st.text("Color represent secondary parameter")
    if selected_state == "overall India":
        # plot for India cart 
        fig = px.scatter_mapbox(df, lat="Latitude",lon="Longitude", size=primary,
                                color=secondary, zoom=4, size_max=35, mapbox_style="carto-positron",
                                width=1200, height=700, hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for a state
        state_df = df[df.State== selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude",lon="Longitude", size=primary,
                                color=secondary, zoom=4, size_max=35, mapbox_style="carto-positron",
                                width=1200, height=700, hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
