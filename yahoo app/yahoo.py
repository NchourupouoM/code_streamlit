import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import base64

# st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('S&P 500 APP')

st.markdown("""
This app retrieves the list of the S&P 500 (from Wikipedia) and its corresponding stock closing price (year-to-date)!
* Python libraries: base64, pandas, streamlit, numpy, matplotlib, seaborn
* Data source: [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header("User Input Features")

## Web scrapping de S&P 500

@st.cache_data() # permet de mettre les donnees une fois scrappees dans le cache.
def load_data():
    url  = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url,header=0)
    df = html[0]
    return df

df = load_data()
# group by sector column 
sector = df.groupby('GICS Sector')

sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector',sorted_sector_unique)

# Filtering Datas
df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]
st.header('Display compagnies in selected sector')
st.write('Data Dimension:' + str(df_selected_sector.shape[0])+'row and'+ str(df_selected_sector.shape[1])+ 'columns')

#Download S&P 500
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">File download</a>'
    return href

st.markdown(filedownload(df_selected_sector),unsafe_allow_html=True)

# yahoo finance
try:
    data = yf.download(
        tickers=list(df_selected_sector[:10].Symbol),
        period='ytd',
        interval='1d',
        group_by='ticker',
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None
    )
except:
    print("Select compagnies in select sector")

#plot Closing Price of query Symbol
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df.Date = df.index
    fig, ax = plt.subplots()
    plt.fill_between(df.Date, df.Close, color='skyblue',alpha=0.3)
    plt.plot(df.Date, df.Close, color='skyblue',alpha=0.8)
    plt.xticks(rotation=45)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date', fontweight='bold')
    plt.ylabel('Closing price', fontweight='bold')
    return st.pyplot(fig)

num_compagny = st.sidebar.slider('Number of compagnies',1,5)

if st.button('Show plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_compagny]:
        price_plot(i)