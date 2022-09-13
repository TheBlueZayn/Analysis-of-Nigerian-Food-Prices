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

    # Load datasets
price_data = pd.read_csv("prices.csv")
low_high = pd.read_csv("lowest_highest.csv")
st.write(price_data.head())
st.write(low_high.head())

    #defining variables
high = "Highest price is from " + low_high["Highest"]
low = "Lowest price is from " + low_high["Lowest"]
max = price_data["Beef Bone in"].max()
min = price_data["Beef Bone in"].min()
price = price_data["Beef Bone in"].tail(1)[0]
y = (max - min) / price

    # # plot graph
    # fig, ax = plt.subplots(figsize=(15,10))
    # ax.plot(price_data['Beef Bone in'])
    # plt.ylabel("Price in Naira (₦)", fontsize=15)
    # plt.xlabel("Year", fontsize=15)
    # fig.text(0.15, 0.85, "Beef Bone in (Jan 2017 - July 2022)", fontsize=18)
    # fig.text(0.67, 0.17, high[4], fontsize=13)
    # fig.text(0.67, 0.20, low[4], fontsize=13)
    # fig.text(0.85, y, "₦ "+ str(price))
    # for s in ['top', 'right']:
    #     ax.spines[s].set_visible(False)
    # # Show plot
    # st.pyplot(fig)


