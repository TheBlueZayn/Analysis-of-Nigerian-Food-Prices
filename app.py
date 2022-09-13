import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



header = st.container()
dataset = st.container()
analyse_data = st.container()
geo_zones = st.container()
six_states = st.container()
causes  = st.container()
with header:
    st.title("""Analysis of Nigerian Food Prices (Jan 2017 - July 2022)""")
    st.text("By Zaynab Arowosegbe")
    st.text("More Info on the analysis")

with dataset:
    st.header("About the dataset")
    st.text("The dataset was gotten from nhuhedh")

    # Load datasets
    price_data = pd.read_csv("prices.csv")
    price_data["Date"] = pd.to_datetime(price_data["Date"], format="%d/%m/%Y")
    low_high = pd.read_csv("lowest_highest.csv")
    zones = pd.read_csv("zone_prices")
    # Show data
    st.write(price_data.head())
    st.write(low_high.head())

    
with analyse_data:
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
    price_data.set_index("Date", inplace=True)
    st.subheader("Prices(₦) of "+ food_item + " (Jan 2017 - July 2022)")
    line = pd.DataFrame(price_data[food_item])
    st.line_chart(line)
    # Show states with lowest and highest prices
    st.subheader("State with lowest and highest price of " + food_item)
    st.write(low_high[low_high["Food Item"] == food_item].set_index("Food Item"))


    # Comparing accresso geopolitical zones
with geo_zones:
    st.header("Comparing current prices (July 2022) of major food items accross geopolitical zones")
    # Get column names from zones dataset
    columns = ['Beans brown,sold loose', 'Beef (boneless)', 'Bread sliced 500g',
    'Gaari white (sold loose)', 'Onion bulb',
    'Palm oil: 1 bottle (specify bottle)', 'Rice local (sold loose)',
    'Tomato', 'Wheat flour: prepacked (golden penny 2kg)', 'Yam tuber']
     # Create list "max" that contains the highest price per item
    max = []
    for c in columns:
        max.append(zones[c].max())

    val = [
    [386.1840411, 379.0323035, 487.9978871, 853.1927586, 579.927014, 598.0036126],
    [1524.440217, 1576.95147, 1945.430477, 2579.403467, 2115.790993, 2084.20833],
    [332.4028314,326.6637037,440.2701763,645.9435902,505.5209314,502.2926772],
    [272.9531667, 270.6920883, 521.499012, 390.268378, 285.6521444, 296.5013584],
    [207.0223462, 188.1759649, 510.140152, 536.0682546, 601.0026235, 441.9778229],
    [572.4250284,606.1546032,1065.537336,1094.023935,850.4868658,1014.104108],
    [401.7234927,419.7734734,796.0259923,467.8275394,463.0285133,519.6446083],
    [227.3305247,194.7206519,656.9394016,678.8038337,609.7815379,496.2086505],
    [819.4621459,838.4580111,1129.354545,1342.914286,1057.081982,1155.383191],
    [191.8493924, 168.1551907, 543.979936, 479.0973747, 468.6454505, 538.0165566]
        ]
    font_color = ['rgb(40,40,40)'] + [['rgb(255,0,0)' if v == 853.1927586 or v == 2579.403467 or v == 645.9435902 or 
                                                     v ==  521.499012 or v == 601.0026235 or v == 1094.023935 or
                                                     v == 796.0259923 or v == 678.8038337 or v == 1342.914286 or
                                                     v == 543.979936
                                                   else 'rgb(10,10,10)' for m in max for v in val[k]] for k in range(10)]
    # Plot data
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(zones.columns),
                align='left',
                font = dict(color=['rgb(45,45,45)']*2, size=14)),
    cells=dict(values=zones.transpose().values.tolist(),
               align='left', font = dict(color = font_color),
               format = [None, ",.2f"],
               prefix = [None, '₦', '₦', '₦', '₦', '₦', '₦', '₦', '₦', '₦', '₦']))
                ])
    fig.update_layout(title="Average Prices of Selected Food Items per Geopolitical Zones (July 2022)<br>(Highest Prices in Red)")
    st.write(fig)

with six_states:
    st.header("Comparing current prices (July 2022) of six food items accross six states")
    
with causes:
    st.header("What are the causes of foof inflation?")










