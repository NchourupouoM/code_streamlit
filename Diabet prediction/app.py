import pandas as pd
import streamlit as st
import pandas as pd
import seaborn as sns
import pickle
import numpy as np
import base64
import matplotlib.pyplot as plt

@st.cache_data
def load_data(dataset):
    df = pd.read_csv(dataset)
    return df

def file_download():
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<href data:file/csv;base64,{b64}"download="diabete_predictions.csv">'
    return href

st.sidebar.image('diabets.jpg',width=200)

data = load_data('diabetes.csv')
def main():
    st.markdown("<h1 style='text-align:center;color:brown;'> Stremlit Diabets App </h1>")
    st.markdown("<h1 style='text-align:center;color:brown;'> Diabetis study in cameroun </h1>")

    menu = ['Home','Analysis','Data visualisation','Machine Learning']
    choice = st.sidebar.selectbox('Select Menu',menu)
    if choice=='Home':
        left, middle ,right = st.columns((2,3,2))
        with middle:
            st.image('telechargement.jpg', width=300)
        st.write("This is an app that will analyse diabets Datas")
        st.subheader('Diabetis informations')
        st.write('In cameroon, the prevelence of diabetes in adults')
        data = load_data('diabetes.csv')
    if choice == 'Analysis':
        st.subheader("Diabetes Dataset")
        st.write(data.head())
        if st.checkbox('summary'):
            st.write(data.describe())

        elif st.checkbox('Correlation'):
            fig = plt.figure(figsize=(15,15))
            st.write(sns.heatmap(data=data.corr(),annot=True))
            st.pyplot(fig)
    if choice == 'Data visualisation':
        if st.checkbox('Countplot'):
            fig = plt.figure(figsize=(15,15))
            sns.countplot(x='Age',data=data)
            st.pyplot(fig)
    elif choice == 'Machine Learning':
        tab1, tab2, tab3 = st.tabs([])
        uploader_file = st.sidebar.file_uploader('Upload your csv', type=['csv'])
        if uploader_file:
            df = load_data(uploader_file)

            with tab1:
                st.subheader('loaded dataset')
                st.write(df)
            with tab2:
                st.subheader('Histogram Glucose')
                fig = plt.figure(x='Glucose',data=df)
                st.pyplot(fig=fig)
            with tab3:
                model = pickle.load(open('model_dump.pkl','rb'))
                prediction = model.predict(df)
                st.subheader('prediction')
                pp = pd.DataFrame(prediction, columns=['prediction'])
                ndf =pd.concat([df, pp],axis=1)
                ndf.prediction.replace(0, "No Diabete Risk", inplace=True)
                ndf.prediction.replace(1, "Diabete Risk", inplace=True)
                st.write(ndf)

                button = st.button()

if __name__ == '__main__':
    main()