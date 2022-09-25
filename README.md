# Analysis of Nigerian Food Prices

Nigeria has been facing food price inflation for the past few years, coupled with economic crises and poverty. It is also no news that the country has been fighting insecurity in form of insurgency, gang activities and an uptick in general social crimes.
Analysis of available data shows that much of Nigeria's food-producing states are battling these violent activities.
 

## Datasets
For this analysis, I depended on the data from Nigeria's National Bureau of Statistics [(NBS)](https://nigerianstat.gov.ng/elibrary/read/1241203), which collects and publishes food prices across the country every month. This data has been consistent for more than 5 years and in this analysis, I used the food price index data from 2017 to  July 2022. This main data was then split into smaller datasets used in the analysis. 
I needed [another data](https://github.com/TheBlueZayn/Project/blob/main/Data%20Sources/attacks.xlsx) that gives an insight into the security issues of Nigeria, the best I could find is the Council on Foreign Affairs which collates data on different forms of violent activities in the country and I used its security tracker data.
I also used a [dataset](https://github.com/TheBlueZayn/Project/blob/main/economic-indicators.csv) from [OpenAfrica](https://africaopendata.org/nl/dataset/nigeria-employment-statistics/resource/e90dcf62-d944-4237-83b5-43228af0519f) that shows the economic indications of Nigeria in the last three years. 

## **Steps**
The [initial dataset](https://github.com/TheBlueZayn/Project/blob/main/Data%20Sources/SELECTED%20FOOD%20(JAN_2017%20-%20FEB%202022).xlsx) (*an excel file*) from NBS was collected which contained data from January 2017 to Febuary 2022 over the years, subsequent data was manually appended to the existing data. The initial form of the dataset had the dates as columns and food items as rows. While this is comvinient as a spreadsheet, it is not the best for analyis. The final dataset was exported to a python environment and transposed with pandas and then later exported to a spreadsheet for final cleaning. 
The original dataset contained extra information on the state with the lowest and highest price for a particular food item, the month-month increase, year-year increase, prices and geographcal zone and others. The individual data was split into smaller datesets to aid analysis. 

- [prices.ipynb](https://github.com/TheBlueZayn/Analysis-of-Nigerian-Food-Prices/blob/main/prices.ipynb) contains the codes of analysis
- [app.py](https://github.com/TheBlueZayn/Analysis-of-Nigerian-Food-Prices/blob/main/app.py) contains the codes to deploy on streamlit

The following libraries were used;
- Pandas for data wrangling and analysis
- Matplotlib for visualisations
- Plotly for an interactive visualisation interface


**View this analysis in an interactive form on the web [here](https://thebluezayn-analysis-of-nigerian-food-prices-app-gzo2up.streamlitapp.com/)**

## Contributions
To make a contribution, create a new branch and make a pull request
