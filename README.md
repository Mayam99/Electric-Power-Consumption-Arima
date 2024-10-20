# Electric-Power-Consumption-Arima

Electric Power Consumption Time Series Forecasting

This project focuses on time series forecasting using the Electric Power Consumption dataset from Kaggle. The dataset contains household electricity consumption data recorded over time, which includes features such as global active power, voltage, and energy sub-metering.

In this analysis, we apply the ARIMA (AutoRegressive Integrated Moving Average) model to forecast future power consumption based on past trends. The workflow involves data preprocessing, exploratory data analysis, parameter tuning, and model evaluation to ensure accurate forecasting.

Key Features:

1. Dataset: Historical time series data of household electric power consumption.
2. Model: ARIMA model for univariate time series forecasting.
3. Libraries Used: Pandas, Matplotlib, Statsmodels, Scikit-learn.
4. Analysis Includes:
* Visualizing historical consumption patterns.
* Selecting ARIMA parameters (p, d, q) based on ACF and PACF.
* Evaluating model performance with metrics like MAE, MSE, and RMSE.
* Forecasting future consumption and comparing with observed values.

This repository contains all the necessary code and documentation to reproduce the analysis and gain insights into electricity consumption forecasting.
