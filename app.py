import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()

with header:
    st.title("""Analysis of Nigerian Food Prices 2022
                By Zaynab Arowosegbe""")
    st.text("More Info on the analysis")

with dataset:
    st.header("About the dataset")
price_data = pd.read_csv("prices.csv")
st.write(price_data.head())


