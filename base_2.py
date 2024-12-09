import streamlit as st
import pandas as pd

# importer une image

#st.image("lien", caption="This is my image",width=600)

# Audio et video

#st.audio("lien")
#st.video("lien")

# Checkbox
state = st.checkbox("checked the box")
if state:
    st.write("You checked the box")
else:
    st.write("waiting for checked")

# Bouton radio 
radio_btn = st.radio("In which country do you live ?", options=("US","UK","Canada"))

# Button 
btn = st.button("Click me")

#select box
st.selectbox("What is your favorite car", options=("AUDI","BMW","FERRARI"))

#Multiselect
st.multiselect("Choose your favorite compagny",options=('Microsoft',"Meta","Google","Apple"))