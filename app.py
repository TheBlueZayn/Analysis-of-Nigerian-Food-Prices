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
zones_1 = pd.read_csv("zones_1.csv")

# Data 4
current_price = pd.read_csv("current_price_six_states.csv")

# Data 5 
m_y = pd.read_csv("MoM_YoY.csv")

# Data 6
attack = pd.read_csv("attacks_and_deaths .csv")

# Data 7
most_attacked= attack.sort_values(by=['attacks'], ascending=False)[:10]

# Data 8
economic = pd.read_csv("economic-indicators.csv")

with header:
    st.title("""Analysis of Nigerian Food Prices (January 2017 - July 2022)""")
    st.markdown("**Zaynab Arowosegbe**")
    st.markdown("Do you know how wide the imbalance of food prices are in Nigeria? Read through to know more.")
    st.markdown("Nigeria has been facing food price inflation for the past few years, coupled with economic crises and poverty. it is also no news that the country has been fighting insecurity in forms of insurgency, gang activities and an uptick in general social crimes. Analysis of available data shows that much of Nigeria's food-producing states are battling these violent activities.")
    st.markdown("In this report, I would analyse the prices of 42 food items, their average prices on a national level, state level and the price changes from January 2017 to July 2022 and answering the following questions:")
    st.markdown("- What has been the trend of the prices across the years?")
    st.markdown("- What is the current average national price and what states have the lowest and highest price?")
    st.markdown("- What are the variations across the six geopolitical zones?")
    st.markdown("- Are there correlations among some of the food prices?")
    st.markdown("- What has been the influence of covid19 pandemic on food prices?")
    st.markdown("- What states have the most attacks and what has been the death count in the last few years?")
    st.markdown("- Has this insecurity led to inflation of prices across the states? especially in the southern region where the prices are higher.")




with dataset:
    st.header("About the dataset")
    st.markdown("For this analysis, I used the data from Nigeria's National Bureau of Statistics [NBS](https://nigerianstat.gov.ng/elibrary/read/1241203), which collects and publishes food prices across the country at the end of every month. This data has been consistent for more than 5 years and in this analysis, I used the food price index data from January 2017 to  July 2022. This main data was then split into smaller datasets used in the analysis.")
    st.markdown("I needed another data that gives an insight into the security issues of Nigeria, the best I could find was from [github](https://github.com/kfalayi/Food-price-Nigeria/blob/main/attacks.xlsx) which contain from data on different forms of violent activities in the country collated by the Council on Foreign Affairs from its security tracker. I also used a dataset from from [OpenAfrica](https://africaopendata.org/nl/dataset/nigeria-employment-statistics/resource/e90dcf62-d944-4237-83b5-43228af0519f) that shows the economic indications of Nigeria in the last three years.")

    
with analyse_data:
    st.header("Analysis of the various food items")
    st.markdown("The average national price of all the food items is visualised over the timeframe. The current national price and the states where the price is cheapest and most expensive as at July 2022 are annotated on the graph. The grains are **sold loose** and this means it is nit prepacked and is sold by measurement of thr grain.")
    # Create input colums
    sel_col, disp_col = st.columns(2)
    price_data.set_index("Date", inplace=True)

    food_item = sel_col.selectbox("Select the food item to analyse", options=['Agric eggs (medium size)', 'Agric egg (medium size)',
       'Beans (brown)', 'Beans (white black eye)', 'Beef (bone in)',
       'Beef (boneless)', 'Bread sliced 500g', 'Bread unsliced 500g',
       'Broken Rice (Ofada)', 'Catfish (dried)',
       'Catfish (obokun) fresh', 'Catfish (smoked)', 'Chicken Feet',
       'Chicken Wings', 'Dried Fish Sardine',
       'Evaporated tinned milk carnation', 'Evaporated tinned milk(peak) ',
       'Frozen chicken', 'Gaari white', 'Gaari yellow', 'Groundnut oil',
       'Iced Sardine', 'Irish potato', 'Mackerel (frozen)',
       'Maize grain white', 'Maize grain yellow', 'Mudfish (aro) fresh',
       'Mudfish (aro) dried', 'Onion bulb', 'Palm oil', 'Plantain (ripe)',
       'Plantain (unripe)', 'Rice agric', 'Rice local (ofada)',
       'Rice Medium Grained', 'Rice (imported high quality)', 'Sweet potato',
       'Tilapia fish (epiya) fresh', 'Titus (frozen)', 'Tomato',
       'Vegetable oil', 'Wheat flour:', 'Yam tuber'] ) 
    

    # Create variables
    dic = {'Agric eggs (medium size)':0, 'Agric egg (medium size)':1,
       'Beans (brown)':2, 'Beans (white black eye)':3, 'Beef (bone in)':4,
       'Beef (boneless)':5, 'Bread sliced 500g':6, 'Bread unsliced 500g':7,
       'Broken Rice (Ofada)':8, 'Catfish (dried)':9,
       'Catfish (obokun) fresh':10, 'Catfish (smoked)':11, 'Chicken Feet':12,
       'Chicken Wings':13, 'Dried Fish Sardine':14,
       'Evaporated tinned milk carnation':15, 'Evaporated tinned milk(peak) ':16,
       'Frozen chicken':17, 'Gaari white':18, 'Gaari yellow':19, 'Groundnut oil':20,
       'Iced Sardine':21, 'Irish potato':22, 'Mackerel (frozen)':23,
       'Maize grain white':24, 'Maize grain yellow':25, 'Mudfish (aro) fresh':26,
       'Mudfish (aro) dried':27, 'Onion bulb':28, 'Palm oil':29, 'Plantain (ripe)':30,
       'Plantain (unripe)':31, 'Rice agric':32, 'Rice local (ofada)':33,
       'Rice Medium Grained':34, 'Rice (imported high quality)':35, 'Sweet potato':36,
       'Tilapia fish (epiya) fresh':37, 'Titus (frozen)':38, 'Tomato':39,
       'Vegetable oil':40, 'Wheat flour:':41, 'Yam tuber':42}
    

    label = "Price per " + low_high["Description"]
    high = "Most expensive in " + low_high["Highest"]
    low = "Cheapest in " + low_high["Lowest"]
    max = price_data[food_item].max()
    min = price_data[food_item].min()
    price = price_data[food_item].tail(1)[0]

    # plot graph
    st.subheader("National Price(₦) of "+ food_item + " (Jan 2017 - July 2022)")
    fig_line, ax = plt.subplots(figsize=(15,10))
    ax.plot(price_data[food_item])
    #ax.vlines(2020, ymin=min, ymax=max, color="k", alpha=0.5)
    plt.ylabel("Price in Naira (₦)", fontsize=15)
    plt.xlabel("Year", fontsize=15)
    fig_line.text(0.67, 0.14, high[dic[food_item]], fontsize=15)
    fig_line.text(0.67, 0.17, low[dic[food_item]], fontsize=15)
    fig_line.text(0.67, 0.20, "Current national price at " + "₦"+ str(price), fontsize=15)
    fig_line.text(0.67, 0.23, label[dic[food_item]] + " as at July 2022", fontsize=15)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    st.write(fig_line)    


# Comparing across geopolitical zones
with geo_zones:
    st.header("Comparing current price (July 2022) of major food items across geopolitical zones")

    # Get column names from zones dataset
    columns = ['Beans brown,sold loose', 'Beef (boneless)', 'Bread sliced 500g',
    'Gaari white (sold loose)', 'Onion bulb',
    'Palm oil: 1 bottle (specify bottle)', 'Rice local (sold loose)',
    'Tomato', 'Wheat flour: prepacked (golden penny 2kg)', 'Yam tuber']

    # Create list "max" that contains the highest price per item
    max = []
    for c in columns:
        max.append(zones[c].max())

    val = [[386.1840411,1524.440217,332.4028314,272.9531667,207.0223462,572.4250284,401.7234927,227.3305247,819.4621459,191.8493924],
      [379.0323035,1576.95147,326.6637037,270.6920883,188.1759649,606.1546032,419.7734734,194.7206519,838.4580111,168.1551907],
      [487.9978871,1945.430477,440.2701763,521.499012,510.140152,1065.537336,796.0259923,656.9394016,1129.354545,543.979936],
      [853.1927586,2579.403467, 645.9435902,390.268378,536.0682546,1094.023935,467.8275394,678.8038337,1342.914286,479.0973747],
      [579.927014,2115.790993,505.5209314,285.6521444,601.0026235,850.4868658,463.0285133,609.7815379,1057.081982,468.6454505],
      [598.0036126,2084.20833,502.2926772,296.5013584,441.9778229,1014.104108,519.6446083,496.2086505,1155.383191,538.0165566]]

    font_color = ['rgb(40,40,40)'] + [['rgb(255,0,0)' if v == 853.1927586 or v == 2579.403467 or v == 645.9435902 or 
                                                     v ==  521.499012 or v == 601.0026235 or v == 1094.023935 or
                                                     v == 796.0259923 or v == 678.8038337 or v == 1342.914286 or
                                                     v == 543.979936
                                                   else 'rgb(10,10,10)' for m in max for v in val[k]] for k in range(6)]
    # Plot data
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(zones_1.columns),
                align='left',
                font = dict(color=['rgb(45,45,45)']*2, size=14)),
    cells=dict(values=zones_1.transpose().values.tolist(),
               align='left', font = dict(color = font_color),
               format = [None, ",.2f"],
               prefix = [None, '₦', '₦', '₦', '₦', '₦', '₦', '₦', '₦', '₦', '₦']))
                ])
    fig.update_layout(height=900, width = 700, autosize=False)
    fig.update_traces(cells_font=dict(size = 15))
    #st.markdown("**(Highest Prices in Red)**")
    st.markdown("The prices of **ten** food items are compared across the geopolitical zones, the highest prices are annotated in red. We can observe that food is generally more expensive in the **south east** with north-west coming in next. Food is cheaper in the **north central** except **yam** that is cheaper in North East (*Taraba is one of the yam-producing states in the country.*) The **north** central comprises the major food-producing states like Benue, Nassarawa, Platea and Niger.")
    st.markdown("(*View table in full screen mode to better see the values or scroll if viewing on mobile*)")
    st.markdown("**Highest prices in red**")
    #st.markdown("<p style="color: red;">Highest prices in red</p>")
    st.write(fig)

with six_states:
    #st.header("Current percentage monthly and yearly increase in the price of food items on a national level")
    #st.markdown("The top 5 food items that increased the **most** from last month and their corresponding yearly increase.")
    #st.markdown("- **MoM** = Month on Month")
    #st.markdown("- **YoY** = Year on Year")
    #st.write(m_y.head())
    #st.markdown("The top 5 food items that increased the **least** from last month and their corresponding yearly increase.")
    #st.write(m_y.tail())
    st.subheader("Comparing current price (July 2022) of six food items across six states")
    st.markdown("Some food items have a high monthly and yearly increase, the current price of **six** major food items (*from high and low percentage increase*) of a state in the six geopolitical zones is visualised.")
    st.markdown("This emphasises the price inflation in the southeast state (**Imo**) compared to other states like **Borno** that sells at a much lesser price.")
    # First plot
    fig1, (ax1, ax2) = plt.subplots(1,2, figsize=(40,25))
    color_1 = ["grey" for i in range(6)]
    color_1[2] = color_1[3] = "#1f77b4"
    ax1.bar(current_price["State"], current_price["Beans brown,sold loose"], color = color_1)
    ax1.set_title("Brown Beans", fontsize=60)
    ax1.tick_params(axis='x', labelsize=40)
    ax1.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax1.spines[s].set_visible(False)
    # Second plot
    color_2 = ["grey" for i in range(6)]
    color_2[2] = color_2[3] = "#1f77b4"
    ax2.bar(current_price["State"], current_price["Bread sliced 500g"], color=color_2)
    ax2.set_title("Bread (500g)", fontsize=60)
    ax2.tick_params(axis='x', labelsize=40)
    ax2.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax2.spines[s].set_visible(False)
    st.write(fig1)
    st.write("               ")
    st.write("               ")
    st.write("               ")

    fig2, (ax3, ax4) = plt.subplots(1,2, figsize=(40,25))
    # Thirdplot
    color_3 = ["grey" for i in range(6)]
    color_3[0] = color_3[3] = "#1f77b4"
    ax3.bar(current_price["State"], current_price["Rice local sold loose"], color=color_3)
    ax3.set_title("Local Rice", fontsize=60)
    ax3.tick_params(axis='x', labelsize=40)
    ax3.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax3.spines[s].set_visible(False)
    # Fourth plot
    color_4 = ["grey" for i in range(6)]
    color_4[4] = color_4[3] = "#1f77b4"
    ax4.bar(current_price["State"], current_price["Gari white,sold loose"], color=color_4)
    ax4.set_title("White Gaari", fontsize=60)
    ax4.tick_params(axis='x', labelsize=40)
    ax4.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax4.spines[s].set_visible(False)
    st.write(fig2)
    st.write("       ")
    st.write("       ")
    st.write("       ")


    # Fifth plot
    fig3, (ax5, ax6) = plt.subplots(1,2, figsize=(40,25))
    color_5 = ["grey" for i in range(6)]
    color_5[2] = color_5[3] = "#1f77b4"
    ax5.bar(current_price["State"], current_price["Vegetable oil:1 bottle,specify bottle"], color=color_5)
    ax5.set_title("Vegetable Oil", fontsize=60)
    ax5.tick_params(axis='x', labelsize=40)
    ax5.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax5.spines[s].set_visible(False)
    # Sixth plot
    color_6 = ["grey" for i in range(6)]
    color_6[2] = color_6[3] = "#1f77b4"
    ax6.bar(current_price["State"], current_price["Palm oil: 1 bottle,specify bottle"], color=color_6)
    ax6.set_title("Palm Oil", fontsize=60)
    ax6.tick_params(axis='x', labelsize=40)
    ax6.tick_params(axis='y', labelsize=40)
    for s in ['top', 'right']:
        ax6.spines[s].set_visible(False)
    st.write(fig3)


   
with correl:
    st.header("What are the correlations among the various food items?")
    st.markdown("Correlation is a **statistical measure** that expresses the extent to which two variables are linearly related (meaning they change together at a constant rate). **A heatmap is used to visualise the correlation matrix**.")
    st.markdown("The closer the correlation coefficient is to 1, the more correlated they are. A correlation coefficient of +1 means a positive correlation (they both increase and decrease together, *the lightest shade*). A correlation coefficient of -1 means a negative correlation (if one increases, the other decreases, *the darkest shade*).")
    st.markdown("*See Heatmap in appendix*")
    st.markdown("**Correlation between dry and fresh mudfish**")
    # visualise
    fig_mud, ax = plt.subplots(figsize=(15,10))
    ax.plot(price_data["Mudfish (aro) fresh"], label="Fresh Mudfish")
    ax.plot(price_data["Mudfish (aro) dried"], label="Dried Mudfish")
    plt.ylabel("Price in Naira (₦)", fontsize=18)
    plt.xlabel("Year", fontsize=15)
    ax.legend(loc="lower right", fontsize=15)
    ax.tick_params(axis='y', labelsize=13)
    fig_mud.text(0.38, 1, "As interesting negative correlation is observed from the data.", fontsize=18)
    fig_mud.text(0.38, 0.95,"This is between dried mudfish and fresh mudfish ", fontsize=18)
    fig_mud.text(0.38, 0.90,"Fresh mudfish is cheaper than dried mudfish", fontsize=18, fontweight="bold")
    for s in ['top', 'right']:
         ax.spines[s].set_visible(False)
    st.write(fig_mud)
    
with causes:
    st.header("What are the causes of food inflation?")
    st.markdown("From a publication by [premium times](https://www.premiumtimesng.com/agriculture/agric-news/540069-five-reasons-food-prices-remain-high-in-nigeria-in-2022.html), the five major reasons food remains high in Nigeria in 2022 are;")
    st.markdown("- Fuel scarcity")
    st.markdown("- Electricity shortage")
    st.markdown("- Russia-Ukraine crisis (*strain on the food supply chain as Nigeria imports some agricultural products*)")
    st.markdown("- Insecurity and")
    st.markdown("- Foreign exchange problem")
    st.markdown("I'll be looking into some other factors.")


    # Covid-19 influence
    st.subheader("Effect of Covid-19 pandemic")
    #st.markdown("Introduce covid19")
    st.markdown("On a general scale, all the food prices had a rise from **2021** but the prices of certain food items were geatly influenced by the covid19 pandemic as a huge rise is observed. The food items are;") 
    st.markdown("- White, yellow gaari, White, yellow maize, the four forms of rice, Vegetable oil, groundnut oil and Palm oil")
    st.markdown("It is also observe that they were majorly grains and two of them are shown below.")
    st.markdown("*See more visualisation on the other food item in the appendix*")
   

    # Plot line plot
    fig_cov1, (ax1, ax2) = plt.subplots(1,2,figsize=(30,15))
    ax1.plot(price_data["Beans (brown)"], label= "Brown Beans")
    ax1.plot(price_data["Beans (white black eye)"], label="White Beans", color="c")

    for s in ['top', 'right']:
         ax1.spines[s].set_visible(False)
    ax1.set_title("Covid19 Pandemic Influence on Price of Beans", fontsize=23, fontweight="bold")
    ax1.legend(fontsize=15)

    ax2.plot(price_data["Maize grain white"], label="White Maize")
    ax2.plot(price_data["Maize grain yellow"], label="Yellow Maize", color="c")

    for s in ['top', 'right']:
      ax2.spines[s].set_visible(False)
    ax2.set_title("Covid19 Pandemic Influence on Price of Maize", fontsize=23, fontweight="bold")
    ax2.legend(fontsize=15)
    st.write(fig_cov1)
    st.markdown("From the plot above, we can observe a sharp **rise** in the price of both grains around early 2020 which was the start of covid19 pandemic in the country")


    # Attacks
    st.subheader("Effect of Insecurities in the Country")
    st.markdown("In Nigeria, the leading food producing states include; Niger, Kano, Jigawa, Zamfara, Kebbi, Sokoto, Katsina, Kaduna, Adamawa, Yobe, Borno, Taraba, Plateau, Nasarawa, Bauchi, and Gombe and the top attacked states in the country in the last 9 years is visualised")

    # plot barplot
    incidents = pd.melt(most_attacked, id_vars = ["state"], value_vars=["attacks", "deaths"], var_name="incident", value_name="value")
    fig_bar, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(data=incidents, x="state", y="value", hue="incident", ax = ax, palette=["#1f77b4", "grey"])
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_tick_params(labelsize = 18)
    plt.legend(fontsize=15)
    fig_bar.text(0.15, 0.95, "Top 10 Most Attacked States and Death Count (2013 - 2021)", fontsize=20)
    st.write(fig_bar)
    st.markdown("*See appendix for distribution accross the country*")

    st.markdown("From the plots above we can observe that the top attacked states are (**Borno and Zamfara**) which are both food-producing states and the number of attacks per state is way higher than the number of attacks")
    st.markdown("Insecurity in these part of the country would hinder the proper production and transportation of food items to other part of the country which leads to inflation and price imbalance.")
    

    # Economic indicators
    st.subheader("Economic Indicators")
    st.markdown("An economic indicator is a metric used to assess, measure, and evaluate the overall state of health of the economy at large.")
    st.markdown("The economic indicators of Nigeria in the last three years is shown below")
    st.write(economic)
    st.markdown("From the values in the last three years, we can observe that the health of the country is declining and there is an increase in CPI inflation rate.")
    st.markdown("A consumer price index (CPI) is estimated as a series of summary measures of the period-to-period proportional change in the prices of a fixed set of consumer goods and services of constant quantity and characteristics, acquired, used or paid for by the reference population.")
    st.markdown("According to an [article](https://www.premiumtimesng.com/news/headlines/554166-updated-nigerias-inflation-rate-surges-17-year-high-to-20-5.html), the data from [Nigerian Bureau of statistics](https://www.nigerianstat.gov.ng/) reported that Nigeria’s inflation rate surged to 20.52% in August 2022, the highest since September 2005")
    
    # Conclusion
    st.markdown("**In Conclusion**, there is a price imbalance in Nigeria as food-producing states sell at cheaper price but due to insecurity, inflation and other economic indicator the prices changes as it gets to other states in the country.")
    st.markdown("Thank you for reading")
    st.markdown("View codes and data on my [github](https://github.com/TheBlueZayn/Analysis-of-Nigerian-Food-Prices)")
    st.markdown("You can connect with me [here](https://www.linkedin.com/in/zaynab-arowosegbe-b292781a4/)")



    # Appendix
    st.subheader("Appendix")
    st.markdown("**Correlation Heatmap**")
    corr = price_data.corr()
    fig, ax = plt.subplots(figsize=(20,15))
    sns.heatmap(corr, ax=ax)
    st.write(fig)
    # st.markdown("From the visualisation, we can observe a:")
    # st.markdown("**Positive correlation between**")
    # st.markdown("- Both forms of bread, beans, gaari and maaize")
    # st.markdown("- The four forms of rice (imported, ofada, broken and medium grained)")
    # st.markdown("- Groundnut oil, palm oil and vegetable oil")
    # st.markdown("- Irish potato, palm oil and vegetable oil")
    # st.markdown("- Milk, bread, veg oil and wheat flour")
    # st.markdown("- Maize and vegetable oil")
    # st.markdown("**Negative correlation between**")
    # st.markdown("- Fresh mudfish and dried mudfish")
    # st.markdown("- Iced sardine, dried fish sardine and catfish")


    st.markdown("**Influence of Covid-19**")
    fig_cov2, (ax1, ax2) = plt.subplots(1,2,figsize=(30,15))
    ax1.plot(price_data["Rice agric"], label="Agric Rice", color="c")
    ax1.plot(price_data["Rice local (ofada)"], label="Ofada Rice", color="grey")
    ax1.plot(price_data["Rice Medium Grained"], label="Medium Grained Rice")
    ax1.plot(price_data["Broken Rice (Ofada)"], label="Broken Rice", color="#4a90e2")

    for s in ['top', 'right']:
         ax1.spines[s].set_visible(False)
    ax1.set_title("Covid19 Pandemic influence on Price of Rice", fontsize=23, fontweight="bold")
    ax1.legend(fontsize=15)

    ax2.plot(price_data["Vegetable oil"], label="Vegetable Oil")
    ax2.plot(price_data["Palm oil"], label="Palm Oil", color="grey")
    ax2.plot(price_data["Groundnut oil"], label="Groundnut Oil", color="c")

    for s in ['top', 'right']:
         ax2.spines[s].set_visible(False)
    ax2.set_title("Covid19 Pandemic influence on Price of Cooking Oil", fontsize=23, fontweight="bold")
    ax2.legend(fontsize=15)
    st.write(fig_cov2)



    # Plot map
    fig_geo = px.scatter_geo(
    attack, lat="lat", lon="lon",
    size="attacks", 
    color="deaths",
    hover_name="state",
    fitbounds="locations"
    )
    fig_geo.update_layout(title="(Hover for State name)<br>Size of circle represents number of attacks")
    fig_geo.update_geos(
    visible=False, resolution=110,
    showcountries=True, countrycolor="Black"
    )
    st.markdown("**Distribution of attcks accross Nigeria (2013 - 2021)**")
    st.write(fig_geo)









