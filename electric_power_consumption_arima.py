# -*- coding: utf-8 -*-
"""Electric Power Consumption-Arima.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mml8Zyce1qg0X5HcdYilD2hz7Aw09xjF

##Electric Power Consumption Dataset Analysis
###This project focuses on analyzing the Electric Power Consumption dataset, sourced from Kaggle. The dataset records the power usage of a household, capturing various time-series measurements that include features such as global active power, global reactive power, voltage, and energy sub-metering. Our primary goal is to explore the dataset for trends, patterns, and insights that can help better understand consumption behaviors and potentially predict future power demand.

###We will be leveraging Python’s data science libraries such as Pandas, NumPy, and Matplotlib for data manipulation and visualization. To enhance the efficiency of our analysis, we will also employ machine learning techniques to model and forecast consumption patterns, ensuring we account for seasonality and other factors impacting electricity use.

###The insights gained from this analysis can have practical implications for energy conservation efforts, grid management, and personalized power consumption strategies for households.

##Features:

* Date Time: Time window of ten minutes.
* Temperature: Weather Temperature.
* Humidity: Weather Humidity.
* Wind Speed: Wind Speed.
* General Diffuse Flows: “Diffuse flow” is a catchall term to describe low-temperature (< 0.2° to ~ 100°C) fluids that slowly discharge through sulfide mounds, fractured lava flows, and assemblages of bacterial mats and macrofauna.
* Diffuse Flows

##Target:

* Zone 1 Power Consumption
* Zone 2 Power Consumption
* Zone 3 Power Consumption

##Importing Necessary Libraries.
"""

import pandas as pd #It imports the pandas library and assigns it the alias "pd" for easier use.
import numpy as np #It brings in a tool called numpy, nicknamed "np", to help with number crunching in your code.
import matplotlib.pyplot as plt #It imports plotting tools from matplotlib, nicknamed "plt", for creating visualizations.
import seaborn as sn #It imports the seaborn library, nicknamed "sns", for making statistical visualizations
from statsmodels.tsa.arima.model import ARIMA #It imports the ARIMA model class from the statsmodels library for time series analysis.
from sklearn.metrics import mean_absolute_error, mean_squared_error #It imports functions to calculate mean absolute error and mean squared error for model evaluation.

"""##Loading the Dataframe"""

df = pd.read_csv("powerconsumption.csv", parse_dates=['Datetime'], index_col='Datetime') #It reads data from the "powerconsumption.csv" file and stores it in a table called "df" using pandas
#parse_dates=['Datetime']: This argument tells read_csv to try and interpret the values in the column named 'Datetime' as dates and times. This is crucial for time-series analysis.
#index_col='Datetime': This part sets the 'Datetime' column as the index of the DataFrame. This means the rows of your DataFrame will be identified by their corresponding date and time values, which is essential for working with time-series data.

df

df.isnull().sum()
#Essentially tells us how many missing values there are in each column of your DataFrame, df.
#This information is crucial for data cleaning and preprocessing before further analysis.

"""##Line plot visualizing the electric power consumption of Zone 1 over time."""

df['PowerConsumption_Zone1'].plot(figsize=(10, 6))
plt.title('Electric Power Consumption Over Time')
plt.show()

"""##Line plot visualizing the electric power consumption of Zone 2 over time."""

df['PowerConsumption_Zone2'].plot(figsize=(10, 6))
plt.title('Electric Power Consumption Over Time')
plt.show()

"""##Line plot visualizing the electric power consumption of Zone 3 over time."""

df['PowerConsumption_Zone3'].plot(figsize=(10, 6))
plt.title('Electric Power Consumption Over Time')
plt.show()

"""##Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots for the 'PowerConsumption_Zone1'"""

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# ACF and PACF plots for selecting p and q
plot_acf(df['PowerConsumption_Zone1'])
plt.show()

plot_pacf(df['PowerConsumption_Zone1'])
plt.show()

"""##Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots for the 'PowerConsumption_Zone2'"""

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# ACF and PACF plots for selecting p and q
plot_acf(df['PowerConsumption_Zone2'])
plt.show()

plot_pacf(df['PowerConsumption_Zone2'])
plt.show()

"""##Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots for the 'PowerConsumption_Zone3'"""

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# ACF and PACF plots for selecting p and q
plot_acf(df['PowerConsumption_Zone3'])
plt.show()

plot_pacf(df['PowerConsumption_Zone3'])
plt.show()

p, d, q = 1, 1, 1
#By setting p, d, and q to 1, 1, and 1, we are defining an ARIMA(1, 1, 1) model. This model:

#Uses one previous time step's value (AR component).
#Differences the data once to make it stationary (I component).
#Includes one previous error term (MA component).

"""#Predicting Power Consumption for Zone 1."""

model = ARIMA(df['PowerConsumption_Zone1'], order=(p, d, q))
#It creates an ARIMA model instance with specified order (p, d, q) using power consumption data.

model_fit = model.fit()
#This line essentially trains the ARIMA model on the power consumption data, allowing it to learn patterns and relationships within the time series.

forecast = model_fit.forecast(steps=30)
#This line instructs the fitted ARIMA model to predict the power consumption for the next 30 time periods.

plt.figure(figsize=(10,6))
plt.plot(df['PowerConsumption_Zone1'][-30:], label='Observed')  # Last 30 observations
plt.plot(forecast, label='Forecasted')
plt.title('Observed vs Forecasted Power Consumption')
plt.legend()
plt.show()
#It plots observed and forecasted power consumption for the last 30 time steps for comparison.

residuals = model_fit.resid
plt.figure(figsize=(10,6))
plt.plot(residuals)
plt.title('Residuals of the Model')
plt.show()
#It plots the residuals of the ARIMA model to assess its fit to the data

mae = mean_absolute_error(df['PowerConsumption_Zone1'][-30:], forecast)
mse = mean_squared_error(df['PowerConsumption_Zone1'][-30:], forecast)
rmse = np.sqrt(mse)

print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}')
#It calculates and prints the MAE, MSE, and RMSE to evaluate the forecast accuracy.

"""#Predicting Power Consumption for Zone 2."""

model = ARIMA(df['PowerConsumption_Zone2'], order=(p, d, q))

model_fit = model.fit()

forecast = model_fit.forecast(steps=30)  # Example: forecast for next 30 time periods

plt.figure(figsize=(10,6))
plt.plot(df['PowerConsumption_Zone2'][-30:], label='Observed')  # Last 30 observations
plt.plot(forecast, label='Forecasted')
plt.title('Observed vs Forecasted Power Consumption')
plt.legend()
plt.show()
#It plots observed and forecasted power consumption for the last 30 time steps for comparison.

residuals = model_fit.resid
plt.figure(figsize=(10,6))
plt.plot(residuals)
plt.title('Residuals of the Model')
plt.show()
#It plots the residuals of the ARIMA model to assess its fit to the data

mae = mean_absolute_error(df['PowerConsumption_Zone2'][-30:], forecast)
mse = mean_squared_error(df['PowerConsumption_Zone2'][-30:], forecast)
rmse = np.sqrt(mse)

print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}')
#It calculates and prints the MAE, MSE, and RMSE to evaluate the forecast accuracy.

"""#Predicting Power Consumption for Zone 3."""

model = ARIMA(df['PowerConsumption_Zone3'], order=(p, d, q))

forecast = model_fit.forecast(steps=30)  # Example: forecast for next 30 time periods

plt.figure(figsize=(10,6))
plt.plot(df['PowerConsumption_Zone3'][-30:], label='Observed')  # Last 30 observations
plt.plot(forecast, label='Forecasted')
plt.title('Observed vs Forecasted Power Consumption')
plt.legend()
plt.show()
#It plots observed and forecasted power consumption for the last 30 time steps for comparison.

residuals = model_fit.resid
plt.figure(figsize=(10,6))
plt.plot(residuals)
plt.title('Residuals of the Model')
plt.show()
#It plots the residuals of the ARIMA model to assess its fit to the data

mae = mean_absolute_error(df['PowerConsumption_Zone3'][-30:], forecast)
mse = mean_squared_error(df['PowerConsumption_Zone3'][-30:], forecast)
rmse = np.sqrt(mse)

print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}')
#It calculates and prints the MAE, MSE, and RMSE to evaluate the forecast accuracy.

