import streamlit as st 
import pandas as pd

st.title("Hello streamlit web app")
st.header("Streamlit we app")
st.subheader("Web app developement")
st.markdown("**Hello** *word*")
st.markdown("----------------------")
st.markdown("[Google](https://www.google.com)")
st.latex(r"\begin{pmatrix} a&b\\c&d\end{pmatrix}")

st.json({"a":"1","b":"2"})
code = """
 def funcy():
    return 0
"""
st.code(code)
st.write("Good Morning")
st.metric(label="wind speed", value="120Ms-1",delta="1.4ms-1")
tabel = pd.DataFrame({"Column1":[1,2,3],"Column2":[4,5,6]})
st.table(tabel)
st.dataframe(tabel,hide_index=True)
