import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd



header = st.beta_container()
dataset = st.beta_container()
with header:
    st.title("""Analysis of Nigerian Food Prices (Jan 2017 - July 2022)""")
    st.text("By Zaynab Arowosegbe")
    st.text("More Info on the analysis")

with dataset:
    st.header("About the dataset")

    price_data = pd.read_csv("prices.csv")
    price_data["Date"] = pd.to_datetime(price_data["Date"])
    low_high = pd.read_csv("lowest_highest.csv")
    st.write(price_data.head())
    st.write(low_high.head())

    line = pd.DataFrame(price_data["Beef Bone in"].value_counts()).head()
    st.bar_chart(line)







