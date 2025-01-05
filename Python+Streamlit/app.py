import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import pandas as pd


df=pd.read_csv("C:/Users/SIDDHI/Desktop/Hackaton/Cleandata.csv")

st.title("Google Playstore Analysis")
st.markdown("This Streamlit application presents an analysis of Google Play Store app data. The analysis focuses on trends in app ratings, categories, installations, pricing, content ratings, and how these factors have evolved over time. Browse through the charts and tables to explore the data yourself")

st.sidebar.title("Main Menu")
#sidebar
cat_col=['Category','Size Range','Installs','Type','Content Rating']
num_col=['Rating','Year']

all_cols=cat_col+num_col
selected_col=st.sidebar.selectbox("Select the column to compare",all_cols)

#ploting
if selected_col:
    if selected_col in cat_col:
        fig = px.bar(df, x=selected_col, y='Price', color='Category',title=f'Price Variation by {selected_col}')

    else:
        fig=px.scatter(df,x=selected_col,y='Price',trendline="ols",title=f'Price Vs {selected_col}')

    st.plotly_chart(fig)