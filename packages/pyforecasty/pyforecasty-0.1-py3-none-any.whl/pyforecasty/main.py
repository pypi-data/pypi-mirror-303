def ts():
    num = int(input())
    if(num==1):
        print(
            '''
################### Practical 01 ##############################################
 
#Q1) 
#years <- 1996:2019
#observations <- c(150.3, 150.9, 151.4, 151.9, 152.5, 152.9, 153.2, 153.7, 153.6, 153.5,
 #                 154.4, 154.9, 155.7, 156.3, 156.6, 156.7, 157, 157.3, 157.8, 158.3, 
  #                158.6, 158.6, 159.1, 159.3)
 
install.packages("forecast")
library(forecast)
 
 
# Time series data
years <- 1996:2019
observations <- c(150.3, 150.9, 151.4, 151.9, 152.5, 152.9, 153.2, 153.7, 153.6, 153.5,
                  154.4, 154.9, 155.7, 156.3, 156.6, 156.7, 157, 157.3, 157.8, 158.3, 
                  158.6, 158.6, 159.1, 159.3)
 
# Create time series object
ts_data <- ts(observations, start=1996, end=2019)
ts_data
 
# Simple Exponential Smoothing with alpha = 0.3
ses_model <- ses(ts_data, alpha=0.3, initial="simple")
ses_model
 
# Holt's Exponential Smoothing with alpha = 0.3 and beta = 0.2
holt_model <- holt(ts_data, alpha=0.3, beta=0.2, initial="simple")
holt_model
 
# Plotting the original series, SES, and Holt's smoothing
plot(ts_data, col="black", lwd=2, ylab="Observations", main="Comparison of Smoothing Methods")
lines(fitted(ses_model), col="blue", lwd=2)
lines(fitted(holt_model), col="red", lwd=2)
legend("topleft", legend=c("Original Series", "SES (α=0.3)", "Holt's (α=0.3, β=0.2)"),
       col=c("black", "blue", "red"), lty=1, lwd=2)
 
 
 
#Characteristics of SES:
#SES is effective for time series data without a trend or seasonality. In this case, 
#it smooths the data using a constant smoothing parameter 
#𝛼=0.3
#The SES line follows the original data closely, capturing the general level of 
#the data but without adapting to any potential trends or changes over time.
#Since SES does not account for trends, its fitted line appears relatively 
#flat and may lag behind the actual data if a trend exists.
#Characteristics of Holt's Exponential Smoothing:
#Holt's method extends SES by including a second smoothing parameter, 
#β, to account for trends in the data.
#With parameters 
#𝛼=0.3
#α=0.3 and β=0.2, the Holt model captures both the level and the trend, allowing it to adjust more dynamically to changes in the data.
#The red line representing Holt's fitted values follows the original series more closely, 
#especially in periods where the data shows an upward trend.
#Comparative Analysis:
 
#Trend Adaptation: Holt's model outperforms SES in tracking the overall trend of the 
#time series data. As the values are steadily increasing over the years, 
#Holt's model successfully captures this upward movement, while SES may lag behind due to 
#its constant smoothing approach.
#Flexibility: Holt's method is more flexible, making it suitable for data with trends. 
#SES, while simple and effective for stationary data, may not provide accurate forecasts 
#if the underlying data has a clear trend.
 
 
#####################
#Q2) 
#Year 	Average CO2 Concentration
#1991	355.62
#1992	356.36
#1993	357.1
#1994	358.86
#1995	360.9
#1996	362.58
#1997	363.84
#1998	366.58
#1999	368.3
#2000	369.47
#2001	371.03
#2002	373.61
#2003	357.61
 
# Given Data
# Given Data
years <- 1991:2003
co2_concentration <- c(355.62, 356.36, 357.1, 358.86, 360.9, 
                       362.58, 363.84, 366.58, 368.3, 
                       369.47, 371.03, 373.61, 357.61)
 
# Create a time series object
co2_ts <- ts(co2_concentration, start = 1991, frequency = 1)
co2_ts
# a) Make a time series plot of the given data
plot(co2_ts, type = "o", col = "blue", 
     main = "Atmospheric CO2 Concentration at Mauna Loa (1991-2003)", 
     xlab = "Year", ylab = "CO2 Concentration (ppm)")
 
# b) Forecast 2004 value by 3-year moving average smoothing method
# Get the last three years of data
last_three_years <- tail(co2_ts, 3)
last_three_years
# Calculate the forecast for 2004 as the average of the last three years
forecast_2004 <- mean(last_three_years)
forecast_2004
# Print the forecasted value
cat("Forecasted CO2 Concentration for 2004:", forecast_2004, "ppm\n")
 
 
 
# Q3) Apply the holt -winters method to AirPassengers data and forecast next 12 months data.
 
#QUESTION 3
# Load necessary libraries
install.packages("forecast")
library(forecast)
 
# Load the AirPassengers data
data("AirPassengers")
 
# Plot the original data
plot(AirPassengers, main = "AirPassengers Data", ylab = "Number of Passengers", xlab = "Year")
 
# Apply Holt-Winters Multiplicative Model
holt_winters_model <- HoltWinters(AirPassengers, gamma = TRUE, seasonal = "multiplicative")
holt_winters_model
# Forecast the next 12 months
forecasted_values <- forecast(holt_winters_model, h = 12)
forecasted_values
 
# Plot the forecasts
plot(forecasted_values, main = "Holt-Winters Forecast for AirPassengers", ylab = "Number of Passengers", xlab = "Year")
 
#seasonal = "multiplicative": 
#This specifies that the seasonal component is multiplicative, 
#meaning that the seasonal effect changes in proportion to the level of the series. 
#In other words, the effect of seasonality increases as the level of the series increases.
 

'''
        )
    elif(num==2):
        print(
            '''
################## PRACTICAL 2 ######################
#AR(1) Process
#The AR(1) process is defined by the equation:
#Xt=0.5Xt−1+ϵt mean 0 and variance 1
 
# 1 (a) Simulate 100 observations from AR(1) process
set.seed(42)
n <- 100
phi <- 0.5
ar1_process <- arima.sim(model = list(ar = phi), n = n)
ar1_process
 
 
# 1 (b) Plot the time series
plot.ts(ar1_process, main = "Simulated AR(1) Process", ylab = "X_t", col = "blue")
 
 
# 1 (c) Estimate AR(1) parameter using arima function
ar1_fit <- arima(ar1_process, order = c(1, 0, 0))
phi_estimated <- ar1_fit$coef[1]
phi_estimated  # Print estimated phi
 
#AR(1) Process
#The AR(1) process is defined by the equation:
#Xt=0.5Xt−1+ϵt mean 0 and variance 1
#i)	  plot acf  pacf of the series 
# 2 (i) Plot ACF and PACF of the series
par(mfrow = c(1, 2))  # Set up a 1x2 plotting grid
acf(ar1_process, main = "ACF of AR(1) Process")
pacf(ar1_process, main = "PACF of AR(1) Process")
par(mfrow = c(1, 1))  # Reset plotting grid
 
#ii) Discuss the behaviour of acf and pacf For AR(1) process 
#For an AR(1) process, the behavior of the ACF 
#(Autocorrelation Function) and PACF (Partial Autocorrelation Function) 
#follows distinct patterns, which can help identify the process when analyzing time series data.
 
#ACF (Autocorrelation Function) of AR(1):
#Decay Pattern: In an AR(1) process, the ACF will show 
#an exponentially decaying behavior. This occurs because each observation 
#is correlated with the one before it, but this correlation weakens over time.
#Interpretation: The ACF captures how observations at different time lags are related to each other. 
#For AR(1), the lag-1 autocorrelation will be the highest, and it will decrease as the lag increases. 
#The decay is characteristic of autoregressive models, especially AR(1), 
#and the rate of decay depends on the value of 𝜙
#The closer 𝜙 is to 1, the slower the decay.
 
#PACF (Partial Autocorrelation Function) of AR(1):
#Cutoff at Lag 1: The PACF of an AR(1) process will have a significant spike at lag 1, 
#and will then drop to zero for all higher lags. 
#This is because the PACF shows the correlation between an observation and 
#its lagged values after removing the effects of any intermediate lags. 
#In an AR(1) process, only the first lag is directly correlated with the current observation, 
#while higher-order lags have no partial autocorrelation.
 
# 3)
# 3 (i) Fit AR(1) or AR(2) model to the data
ar_fit <- arima(ar1_process, order = c(1, 0, 0))  # AR(1)
ar_fit
ar_fit_2 <- arima(ar1_process, order = c(2, 0, 0))  # AR(2)
ar_fit_2
 
# 3 (ii) Forecast the next 10 observations and plot the forecast
forecasted_values <- forecast(ar_fit, h = 10)
forecasted_values
plot(forecasted_values, main = "Forecast of AR(1) Process", col = "red")

'''
        )
    elif(num==3):
        print(
            '''
################# Practical 03 ###########################################
 
#Auto regressive Moving Average(ARMA) 
#Q.1
#Time	Values 
#1	100
#2	110
#3	120
#4	130
#5	140
#6	150
#7	160
#8	170
#9	180
#10	190
#11	200
#12	210
#13	220
#14	230
#15	240
 
 
# Load necessary libraries
library(forecast)
library(tseries)
 
# Time series data
time_series <- ts(c(100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240))
 
# 1. Log transform the data to stabilize variance (optional but can help in some cases)
log_time_series <- log(time_series)
 
# 2. Use auto.arima() to automatically fit the best ARIMA model
# This function will choose the appropriate order of AR and MA terms, as well as differencing
auto_model <- auto.arima(log_time_series)
 
# Print the model summary to check what ARIMA model was fitted
summary(auto_model)
 
# 3. Diagnostic checks of residuals
checkresiduals(auto_model)  # Check if residuals look like white noise
 
# 4. Forecast the next 10 values
forecasted_values <- forecast(auto_model, h = 10)
 
# Print forecasted values (on the log scale)
print(forecasted_values)
 
# 5. Plot the original time series and the forecasted values
plot(forecasted_values, main = "Original Time Series and Forecasted Values (Log Transformed)")
 
 
# Q2 ) 
#1	500
#2	520
#3	540
#4	560
#5	580
#6	600
#7	620
#8	640
#9	660
#10	680
#11	700
#12	720
 
# Load necessary libraries
library(forecast)
library(tseries)
 
# Time series data (Sales)
sales_data <- c(500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720)
time_series <- ts(sales_data, frequency = 1)  # Frequency can be set to 1 for quarterly data
 
# 1. Plot the ACF and PACF of the original time series
par(mfrow = c(1, 2))  # Set up a 1x2 grid
acf(time_series, main = "ACF of Original Series")   # Plot ACF
pacf(time_series, main = "PACF of Original Series") # Plot PACF
par(mfrow = c(1, 1))  # Reset plotting grid
 
# 2. Fit an ARMA(1,1) model to the data
arma_model <- arima(time_series, order = c(1, 0, 1))  # Fitting ARMA(1,1)
summary(arma_model)  # Print the summary of the model
 
# 3. Check the residual diagnostics of the fitted model
tsdiag(arma_model)  # Diagnostic plots for residuals (ACF of residuals, etc.)
Box.test(arma_model$residuals, lag = 10, type = "Ljung-Box")  # Ljung-Box test
 
# 4. Forecast the next 12 values using the fitted model
forecasted_values <- forecast(arma_model, h = 12)
 
# Print the forecasted values
print(forecasted_values)
 
# 5. Plot the original time series, fitted values, and forecasted values
plot(forecasted_values, main = "Original Time Series and Forecasted Values", ylab = "Sales", xlab = "Time")
lines(time_series, col = "blue", lwd = 2)  # Add original series in blue
 
# Add a legend
legend("topleft", legend = c("Original Series", "Forecasted Values"), col = c("blue", "red"), lty = 1)
'''
        )
    elif(num==4):
        print(
            '''
# Load the necessary libraries
library(forecast)
 
#Question 1: Data Preparation
#You are given a dataset containing monthly sales data for a retail store over the past five years. 
#The data shows a clear seasonal pattern.
#a) Plot the time series and describe its key features (trend, seasonality, and noise).
#b) Before applying SARIMA, how would you transform the data to achieve stationarity?
  
  
# Create the sales data
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280, 310, 330, 
                220, 230, 250, 240, 260, 280, 320, 300, 290, 310, 330, 350, 
                240, 250, 270, 260, 280, 300, 340, 320, 310, 330, 350, 370, 
                260, 270, 290, 280, 300, 320, 360, 340, 330, 350, 370, 390, 
                280, 290, 310, 300, 320, 340, 380, 360, 350, 370, 390, 410)
 
# Convert to time series object
sales_ts <- ts(sales_data, start = c(2019, 1), frequency = 12)
sales_ts
# a) Plot the sales data
plot(sales_ts, main = "Monthly Sales Data", xlab = "Time", ylab = "Sales", col = "blue", lwd = 2)
 
# Observations: Check for seasonality and trend by inspecting the plot
 
#b]
# Differencing to remove trend
diff_sales_ts <- diff(sales_ts, differences = 1)
diff_sales_ts
plot(diff_sales_ts, main = "Differenced Sales Data", xlab = "Time", ylab = "Differenced Sales")
 
#a) After plotting the time series, 
#we may observe a long-term increasing trend with a recurring seasonal pattern. 
#The series might also show random fluctuations.
#b) To achieve stationarity, the data may require differencing 
#(to remove the trend) and possibly seasonal differencing (to remove the seasonal component). 
#Log transformation can also stabilize the variance.
 
###################################################################
#Question 2: Model Identification
#Given the same dataset:
# a) Explain how you would identify the order of differencing required for the series (d in ARIMA).
#b) How would you determine the seasonal differencing term (D) for the SARIMA model?
#c) Identify the potential AR and MA orders (p, q, P, Q) using the ACF and PACF plots.
 
#A)
# Perform Augmented Dickey-Fuller test for stationarity
library(tseries)
adf_test <- adf.test(sales_ts)
print(adf_test)
# If p-value > 0.05, differencing is needed (non-stationary).
 
#B)
# Seasonal differencing can be checked by examining the ACF plot
Acf(sales_ts)
# Look for seasonal lags in the ACF plot (e.g., significant peaks at 12 months).
 
#c)
# ACF and PACF plots
Acf(diff_sales_ts, main="ACF of Differenced Sales Data")
Pacf(diff_sales_ts, main="PACF of Differenced Sales Data")
 
 
#a) The order of differencing (d) can be determined by checking the stationarity of 
#the series using methods like the Augmented Dickey-Fuller (ADF) test. 
#If the p-value is above a threshold (e.g., 0.05), differencing is needed.
#b) The seasonal differencing term (D) is usually determined by checking for 
#seasonality at the seasonal lag (e.g., 12 months for yearly seasonality). 
#This can be confirmed through ACF plots showing peaks at seasonal lags.
#c) The ACF and PACF plots are used to identify the AR (p) and MA (q) terms, 
#and the seasonal AR (P) and MA (Q) terms by looking at significant lags.
 
 
 
#Question 3: SARIMA Model Fitting
#After identifying the appropriate (p, d, q) and (P, D, Q, m) orders for the seasonal data:
#a) Fit a SARIMA model to the data.
#b) Interpret the model output and residual diagnostics.
#c) If the residuals show autocorrelation, what steps would you take to improve the model?
  
#a) Fit a SARIMA Model to the Data
# Load necessary libraries
library(forecast)
 
# Assuming you have already created the time series object `sales_ts`
 
# Fit a SARIMA model, e.g., SARIMA(1, 1, 1)(1, 1, 1)[12]
# Replace (1, 1, 1)(1, 1, 1)[12] with your chosen orders
sarima_model <- Arima(sales_ts, order = c(1, 1, 1), seasonal = c(1, 1, 1), lambda = 0)
 
# Print the summary of the model
summary(sarima_model)
 
#b) Interpret the Model Output and Residual Diagnostics
# Residual diagnostics
checkresiduals(sarima_model)  # This function gives ACF plot of residuals and performs the Ljung-Box test
 
# You can also plot the residuals
plot(sarima_model$residuals, main = "Residuals of SARIMA Model", ylab = "Residuals", xlab = "Time")
 
#c) 
#a) Use SARIMA(p, d, q)(P, D, Q, s) to fit the model using statistical software like  R.
#b) Interpret the coefficients and check residual diagnostics, including ACF plots 
#and tests for white noise (Ljung-Box test).
#c) If autocorrelation remains, consider refining the AR and MA terms, 
#adding additional seasonal terms, or applying further differencing.
 
 
 
#Q4 ) 
#Question 4: Forecasting with SARIMA
#Using the SARIMA model from the previous question:
#a) Forecast the sales for the next 12 months.
#b) Plot the forecasted values along with the original time series data. 
#How well does the model capture the seasonality?
# Load necessary libraries
library(forecast)
library(tseries)
 
# Step 1: Create the monthly sales data
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280,
                310, 330, 220, 230, 250, 240, 260, 280, 320, 300,
                290, 310, 330, 350, 240, 250, 270, 260, 280, 300,
                340, 320, 310, 330, 350, 370, 260, 270, 290, 280,
                300, 320, 360, 340, 330, 350, 370, 390, 280, 290,
                310, 300, 320, 340, 380, 360, 350, 370, 390, 410)
 
# Create a time series object
sales_ts <- ts(sales_data, start = c(2019, 1), frequency = 12)
 
# Step 2: Check for NA or infinite values
if (any(is.na(sales_ts)) || any(!is.finite(sales_ts))) {
  stop("Data contains NA or infinite values.")
}
 
# Visualize the time series
plot(sales_ts, main="Sales Data", ylab="Sales", xlab="Time")
 
# Step 3: Check for stationarity
adf_test <- adf.test(sales_ts)
print(adf_test)
 
# If needed, apply differencing
# diff_sales_ts <- diff(sales_ts)
 
# Step 4: Fit a simpler SARIMA model
sarima_model_simple <- Arima(sales_ts, order = c(1, 1, 0), seasonal = c(0, 1, 0))
 
# Step 5: Check residuals
checkresiduals(sarima_model_simple)
 
# Step 6: Automatic model selection
sarima_model_auto <- auto.arima(sales_ts)
 
# Print the automatic model summary
summary(sarima_model_auto)
 
# Step 7: Forecast the sales for the next 12 months
forecasted_values <- forecast(sarima_model_auto, h = 12)
 
# Step 8: Plot the forecasted values along with the original time series data
plot(forecasted_values, main = "Sales Forecast for the Next 12 Months", 
     ylab = "Sales", xlab = "Time", col = "blue", flty = 2)
 
# Add the original time series data for comparison
lines(sales_ts, col = "black", lwd = 2)
 
# Add a legend to the plot
legend("topleft", legend = c("Original Series", "Forecasted Values"),
       col = c("black", "blue"), lty = 1, lwd = 2)
 
#a) Use the fitted SARIMA model to generate 12-month forecasts 
#using the predict or forecast function.
#b) Plot the original and forecasted values. 
#The SARIMA model should effectively capture the seasonality and trend, 
#but model performance can be evaluated using metrics like RMSE or MAPE
 
###############
Question 5: Model Comparison
You decide to compare the SARIMA model with a simple ARIMA model:
  a) Fit an ARIMA model without seasonality.
b) Compare the performance of the SARIMA and ARIMA models using appropriate evaluation metrics (AIC, BIC, RMSE).
c) Based on your findings, which model would you recommend and why?
  
  
#Question 5: Model Comparison
#You decide to compare the SARIMA model with a simple ARIMA model:
#a) Fit an ARIMA model without seasonality.
#b) Compare the performance of the SARIMA and 
#ARIMA models using appropriate evaluation metrics (AIC, BIC, RMSE).
#c) Based on your findings, which model would you recommend and why?
  
  #a)
  # Load necessary library
library(forecast)
 
# Load necessary library
library(forecast)
 
# Assuming sales_ts is your time series object
 
# Step 1: Fit an ARIMA model without seasonality
arima_model <- Arima(sales_ts, order = c(1, 1, 1))  # Adjust order as necessary
arima_model
# Fit the SARIMA model
sarima_model <- Arima(sales_ts, order = c(1, 1, 1), seasonal = c(1, 1, 1))
 
# Step 2: Compare performance metrics
arima_aic <- AIC(arima_model)
sarima_aic <- AIC(sarima_model)
 
arima_bic <- BIC(arima_model)
sarima_bic <- BIC(sarima_model)
 
arima_rmse <- sqrt(mean(residuals(arima_model)^2))
sarima_rmse <- sqrt(mean(residuals(sarima_model)^2))
 
# Create a comparison table
comparison <- data.frame(
  Model = c("ARIMA", "SARIMA"),
  AIC = c(arima_aic, sarima_aic),
  BIC = c(arima_bic, sarima_bic),
  RMSE = c(arima_rmse, sarima_rmse)
)
 
print(comparison)
 
# Step 3: Recommendation based on the comparison
if (sarima_aic < arima_aic && sarima_bic < arima_bic && sarima_rmse < arima_rmse) {
  cat("Recommendation: The SARIMA model is preferred due to lower AIC, BIC, and RMSE.\n")
} else {
  cat("Recommendation: The ARIMA model is preferred due to lower AIC, BIC, and RMSE.\n")
}
 
#a) Fit an ARIMA model without seasonal terms using the same dataset.
#b) Compare the models using metrics like AIC 
#(Akaike Information Criterion), BIC (Bayesian Information Criterion), 
#and RMSE (Root Mean Squared Error). SARIMA typically performs better with seasonal data.
#c) SARIMA is usually recommended for datasets with strong seasonal components, 
#as it captures the seasonality more effectively than ARIMA.
 
 
#############
#Question 6: Holiday Adjustment in SARIMA
#Suppose the retail store experiences a surge in sales during certain holiday months, 
#which is not captured by the original SARIMA model.
#a) How would you modify the SARIMA model to account for the holiday effect?
#b) Refit the modified SARIMA model and compare the results with the previous model.
 
#a)
# Suppose you have a holiday variable (1 for holiday, 0 for non-holiday)
# Add holiday variable as external regressor
holiday_effect <- c(rep(0, 11), 1, rep(0, 11), 1, rep(0, 11), 1, rep(0, 11), 1, rep(0, 11), 1)
 
# Fit SARIMA with external regressors
sarima_with_holiday <- auto.arima(sales_ts, xreg = holiday_effect, seasonal = TRUE)
summary(sarima_with_holiday)
 
 
#b)
# Compare the SARIMA with and without holiday adjustments using AIC, BIC, and RMSE
sarima_holiday_aic <- AIC(sarima_with_holiday)
sarima_holiday_bic <- BIC(sarima_with_holiday)
sarima_holiday_rmse <- sqrt(mean(residuals(sarima_with_holiday)^2))
 
print(paste("SARIMA with holiday AIC:", sarima_holiday_aic, "BIC:", sarima_holiday_bic, "RMSE:", sarima_holiday_rmse))
#a) Incorporate holiday effects as external regressors (exogenous variables) in the SARIMA model.
#b) After refitting the model with the holiday adjustment, 
#check whether the model's performance improves by comparing metrics like AIC, BIC, or RMSE.
'''
        )
 
    else:
        print(
            '''
        1: ses & holt
        2: ar and ma
        3 :  arima and sarima
        4 : 5th prac
        


'''
        )