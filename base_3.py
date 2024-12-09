import streamlit as st
import pandas as pd

#Upload d'un fichier
# st.title("Upload d'un fichier")
# image = st.file_uploader("**plaese upload an image**", type=["png","jpg","jpeg"])
# if image:
    # st.image(image=image)

# video = st.file_uploader("**Please upload a video**",type=["avi","mp4"])
# if video:
    # st.video(data=video)

# slider
st.slider("**This is a slider**",min_value=20,max_value=60,value=30)

# text input 
st.text_input("Enter the text to be translate")

# text area input 
st.text_area("Course description")

# Data input 
st.date_input("Enter your registration date")