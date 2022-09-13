import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd



header = st.container()
dataset = st.container()
analyse_data = st.container()
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
    price_data.set_index("Date", inplace=True)
    st.write(low_high.head())

    
with dataset:
    st.title("Analysis of the various food items")
    st.text("jxhiuih")
    sel_col, disp_col = st.columns(2)

    food_item = sel_col.selectbox("Select the food item to analyse", options=[
        'Agric eggs medium size', 'Agric eggs(medium size price of one)',
       'Beans brown,sold loose', 'Beans:white black eye. sold loose',
       'Beef Bone in', 'Beef,boneless', 'Bread sliced 500g',
       'Bread unsliced 500g', 'Broken Rice (Ofada)', 'Catfish (dried)',
       'Catfish (obokun) fresh', 'Catfish (Smoked)', 'Chicken Feet',
       'Chicken Wings', 'Dried Fish Sardine',
       'Evaporated tinned milk carnation 170g',
       'Evaporated tinned milk(peak) 170g', 'Frozen chicken',
       'Gaari white, sold loose', 'Gaari yellow, sold loose',
       'Groundnut oil, 1 bottle', 'Iced Sardine', 'Irish potato',
       'Mackerel : frozen', 'Maize grain white,  sold loose',
       'Maize grain yellow, sold loose', 'Mudfish (aro) fresh',
       'Mudfish (dried)', 'Onion bulb', 'Palm oil: 1 bottle',
       'Plantain (ripe)', 'Plantain (unripe)', 'Rice agric, sold loose',
       'Rice local (ofada), sold loose', 'Rice Medium Grained',
       'Rice (imported high quality),  sold loose', 'Sweet potato',
       'Tilapia fish (epiya) fresh', 'Titus (frozen)', 'Tomato',
       'Vegetable oil:1 bottle', 'Wheat flour: prepacked (golden penny 2kg)',
       'Yam tuber'])    
    
    st.subheader("Prices(₦) of "+ food_item + " (Jan 2017 - July 2022)")
    line = pd.DataFrame(price_data[food_item])
    st.line_chart(line)










