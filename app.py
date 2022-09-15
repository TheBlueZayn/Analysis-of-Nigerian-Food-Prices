from turtle import color
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# Create subsections 
header = st.container()
dataset = st.container()
analyse_data = st.container()
geo_zones = st.container()
six_states = st.container()
correl = st.container()
covid = st.container()
causes  = st.container()

# Load datasets
# Data 1
price_data = pd.read_csv("prices.csv")
price_data["Date"] = pd.to_datetime(price_data["Date"], format="%d/%m/%Y")

# Round values to 2 decimal place
#price_data= price_data.round(2)

# Data 2
low_high = pd.read_csv("lowest_highest.csv")

# Data 3
zones = pd.read_csv("zone_prices.csv")

# Data 4
current_price = pd.read_csv("current_price_six_states.csv")

# Data 5 
m_y = pd.read_csv("MoM_YoY.csv")

# Data 6
attack = pd.read_csv("attacks_deaths .csv")

# Data 7
most_attacked= attack.sort_values(by=['attacks'], ascending=False)[:10]

# Data 8
economic = pd.read_csv("economic-indicators.csv")

with header:
    st.title("""Analysis of Nigerian Food Prices (Jan 2017 - July 2022)""")
    st.markdown("**By Zaynab Arowosegbe**")
    st.markdown("Nigeria has been facing food price inflation for the past few years and it is no news that the country has been fighting insecurity in form of insurgency, gang activities and an uptick in general social crimes. Analysis of available data shows that much of Nigeria's food-producing states are battling these violent activities. ")
    st.markdown("In this report, I would analyse the prices of 42 food items, their average prices, prices across the states in the country and the price changes from January 2017 to July 2022 and would be answering the following questions:")
    st.markdown("- What has been the trend of the prices across the years?")
    st.markdown("- What is the current average national price and what states have the lowest and highest price?")
    st.markdown("- What are the variations across the six geopolitical zones?")
    st.markdown("- Are there correlations among some of the food prices?")
    st.markdown("- What has been the influence of covid19 pandemic on food prices?")
    st.markdown("- What states have the most attacks and what has been the death count in the last few years?")
    st.markdown("- Has this insecurity led to inflation of prices across the states? especially in the southern region where the prices are higher.")




with dataset:
    st.header("About the dataset")
    st.markdown("For this analysis, I depended on the data from Nigeria's National Bureau of Statistics, which collects and publishes food prices across the country every month. This data has been consistent for more than 5 years and in this analysis, I used the food price index data from January 2017 to  July 2022. This main data was then split into smaller datasets used in the analysis.")
    st.markdown("I needed another data that gives an insight into the security issues of Nigeria, the best I could find is the Council on Foreign Affairs which collates data on different forms of violent activities in the country and I used its security tracker data.")
    st.markdown("Below are frist five rows from tables of the split dataset")

    # Show data
    st.write(price_data.head())
    st.write(low_high.head())

    
with analyse_data:
    st.header("Analysis of the various food items")
    st.markdown("The average national price of all the food items is visualised over the timeframe. The current national price and the states where the price is cheapest and most expensive are annotated on the graph. ")
    # Create input colums
    sel_col, disp_col = st.columns(2)
    price_data.set_index("Date", inplace=True)

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
    

    # Create variables
    dic = {'Agric eggs medium size':0, 'Agric eggs(medium size price of one)':1,
       'Beans brown,sold loose':2, 'Beans:white black eye. sold loose':3,
       'Beef Bone in':4, 'Beef,boneless':5, 'Bread sliced 500g':6,
       'Bread unsliced 500g':7, 'Broken Rice (Ofada)':8, 'Catfish (dried)':9,
       'Catfish (obokun) fresh':10, 'Catfish (Smoked)':11, 'Chicken Feet':12,
       'Chicken Wings':13, 'Dried Fish Sardine':14,
       'Evaporated tinned milk carnation 170g':15,
       'Evaporated tinned milk(peak) 170g':16, 'Frozen chicken':17,
       'Gaari white, sold loose':18, 'Gaari yellow, sold loose':19,
       'Groundnut oil, 1 bottle':20, 'Iced Sardine':21, 'Irish potato':22,
       'Mackerel : frozen':23, 'Maize grain white,  sold loose':24,
       'Maize grain yellow, sold loose':25, 'Mudfish (aro) fresh':26,
       'Mudfish (dried)':27, 'Onion bulb':28, 'Palm oil: 1 bottle':29,
       'Plantain (ripe)':30, 'Plantain (unripe)':31, 'Rice agric, sold loose':32,
       'Rice local (ofada), sold loose':33, 'Rice Medium Grained':34,
       'Rice (imported high quality),  sold loose':35, 'Sweet potato':36,
       'Tilapia fish (epiya) fresh':37, 'Titus (frozen)':38, 'Tomato':29,
       'Vegetable oil:1 bottle':40, 'Wheat flour: prepacked (golden penny 2kg)':41}

    high = "Most expensive in " + low_high["Highest"]
    low = "Cheapest in " + low_high["Lowest"]
    max = price_data[food_item].max()
    min = price_data[food_item].min()
    price = price_data[food_item].tail(1)[0]
    y = ((max - min) / price)

    # plot graph
    st.subheader("National Price(₦) of "+ food_item + " (Jan 2017 - July 2022)")
    fig_line, ax = plt.subplots(figsize=(15,10))
    ax.plot(price_data[food_item])
    #ax.vlines(2020, ymin=min, ymax=max, color="k", alpha=0.5)
    plt.ylabel("Price in Naira (₦)", fontsize=15)
    plt.xlabel("Year", fontsize=15)
    fig_line.text(0.67, 0.17, high[dic[food_item]], fontsize=15)
    fig_line.text(0.67, 0.20, low[dic[food_item]], fontsize=15)
    fig_line.text(0.85, y, "₦"+ str(price), fontsize=15)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    st.write(fig_line)    


    # st.subheader("Prices(₦) of "+ food_item + " (Jan 2017 - July 2022)")
    # line = pd.DataFrame(price_data[food_item])
    # st.line_chart(line)
    # # Show states with lowest and highest prices
    # st.subheader("State with lowest and highest price of " + food_item)
    # st.write(low_high[low_high["Food Item"] == food_item].set_index("Food Item"))


# Comparing across geopolitical zones
with geo_zones:
    st.header("Comparing current prices (July 2022) of major food items across geopolitical zones")

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
    fig.update_layout(width=1000, height=650,autosize=True)
    fig.update_traces(cells_font=dict(size = 15))
    #st.subheader("Current Average Prices of Selected Food Items per Geopolitical Zones (July 2022)")
    st.markdown("**(Highest Prices in Red)**")
    st.markdown("The prices of **ten** food items are compared across the geopolitical zones, the highest prices are annotated in red.")
    st.markdown("We can observe that food is generally more expensive in the **south east** with north-west coming in next. Food is cheaper in the **north central** except **yam** that is cheaper in North East (*Taraba is one of the yam-producing states in the country.*)")
    st.markdown("The north central comprises the major food-producing states like Benue, Nassarawa, Platea and Niger.")
    st.write(fig)

with six_states:
    st.header("Current percentage monthly and yearly increase in the price of food items on a national level")
    st.markdown("The top 5 food items that increased the **most** from last month and their corresponding yearly increase.")
    st.markdown("- **MoM** = Month on Month")
    st.markdown("- **YoY** = Year on Year")
    st.write(m_y.head())
    st.markdown("The top 5 food items that increased the **least** from last month and their corresponding yearly increase.")
    st.write(m_y.tail())
    st.subheader("Comparing current prices (July 2022) of six food items across six states")
    st.markdown("The current price of **six** major food items (*from high and low percentage increase*) of a state in the six geopolitical zones is visualised")
    st.markdown("This emphasises the price inflation in the southeast state (**Imo**) compared to other states like **Borno** that sells at the least price")
    # First plot
    fig1, (ax1, ax2) = plt.subplots(1,2, figsize=(40,25))
    color_1 = ["grey" for i in range(6)]
    color_1[2] = color_1[3] = "#1f77b4"
    ax1.bar(current_price["State"], current_price["Beans brown,sold loose"], color = color_1)
    ax1.set_title("Brown Beans", fontsize=80)
    ax1.tick_params(axis='x', labelsize=40)
    ax1.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax1.spines[s].set_visible(False)
    # Second plot
    color_2 = ["grey" for i in range(6)]
    color_2[2] = color_2[3] = "#1f77b4"
    ax2.bar(current_price["State"], current_price["Bread sliced 500g"], color=color_2)
    ax2.set_title("Bread (500g)", fontsize=80)
    ax2.tick_params(axis='x', labelsize=40)
    ax2.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax2.spines[s].set_visible(False)
    st.write(fig1)

    fig2, (ax3, ax4) = plt.subplots(1,2, figsize=(40,25))
    # Thirdplot
    color_3 = ["grey" for i in range(6)]
    color_3[0] = color_3[3] = "#1f77b4"
    ax3.bar(current_price["State"], current_price["Rice local sold loose"], color=color_3)
    ax3.set_title("Local Rice", fontsize=80)
    ax3.tick_params(axis='x', labelsize=40)
    ax3.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax3.spines[s].set_visible(False)
    # Fourth plot
    color_4 = ["grey" for i in range(6)]
    color_4[4] = color_4[3] = "#1f77b4"
    ax4.bar(current_price["State"], current_price["Gari white,sold loose"], color=color_4)
    ax4.set_title("White Gaari", fontsize=80)
    ax4.tick_params(axis='x', labelsize=40)
    ax4.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax4.spines[s].set_visible(False)
    st.write(fig2)

    # Fifth plot
    fig3, (ax5, ax6) = plt.subplots(1,2, figsize=(40,25))
    color_5 = ["grey" for i in range(6)]
    color_5[2] = color_5[3] = "#1f77b4"
    ax5.bar(current_price["State"], current_price["Vegetable oil:1 bottle,specify bottle"], color=color_5)
    ax5.set_title("Vegetable Oil", fontsize=80)
    ax5.tick_params(axis='x', labelsize=40)
    ax5.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax5.spines[s].set_visible(False)
    # Sixth plot
    color_6 = ["grey" for i in range(6)]
    color_6[2] = color_6[3] = "#1f77b4"
    ax6.bar(current_price["State"], current_price["Palm oil: 1 bottle,specify bottle"], color=color_6)
    ax6.set_title("Palm Oil", fontsize=80)
    ax6.tick_params(axis='x', labelsize=40)
    ax6.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax6.spines[s].set_visible(False)
    st.write(fig3)

   
with correl:
    st.header("What are the correlations among the various food items?")
    st.markdown("Correlation is a **statistical measure** that expresses the extent to which two variables are linearly related (meaning they change together at a constant rate).")
    st.markdown("The closer the correlation coefficient is to 1, the more correlated they are. A correlation coefficient of +1 means a positive correlation(they both increase and decrease together, *the lightest shade*). A correlation coefficient of -1 means a negative correlation(if one increases, the other decreases, *the darkest shade*).")
    st.markdown("From the heatmap below that augments the correlation matrix below, we can observe that:")
    st.markdown("- Positive correlation between both forms of bread, beans, gaari and rice.")
    st.markdown("- Positive correlation between groundnut oil, palm oil and vegetable oil.")
    st.markdown("- Positive correlation between Irish potato, palm oil and veg oil.")
    st.markdown("- Positive correlation between milk, bread, veg oil and wheat flour.")
    st.markdown("- Positive correlation between maize and vegetable oil.")
    st.markdown("- Negative correlation between dried mudfish, smoked catfish and dried fish.")
    st.markdown("- Negative correlation between iced sardine, and catfish.")
    st.markdown("- Negative correlation between Iced sardine and dried fish sardine.")
    #st.markdown("- ")
    corr = price_data.corr()
    fig, ax = plt.subplots(figsize=(20,15))
    sns.heatmap(corr, ax=ax)
    st.write(fig)
    
with causes:
    st.header("What are the causes of food inflation?")
    st.markdown("hedee")
    st.subheader("States with the most frequent attacks (2013-2021)")
    # Plot map
    fig_geo = px.scatter_geo(
    attack, lat="lat", lon="lon",
    size="attacks", 
    color="deaths",
    hover_name="state",
    fitbounds="locations"
    )
    fig_geo.update_layout(title="jjj(Hover for State name)<br>Size of circle represents number of deaths")
    fig_geo.update_geos(
    visible=False, resolution=110,
    showcountries=True, countrycolor="Black"
    )
    st.write(fig_geo)

    st.subheader("Most Attacked States(2013-2021)")
    fig_bar = px.bar(most_attacked, x="state", y=["attacks", "deaths"], barmode="group")
    fig_bar.update_layout(width=900)
    st.write(fig_bar)
    
    st.subheader("Economic Indicators in the Last Three Years")
    st.write(economic)










