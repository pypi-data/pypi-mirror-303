def help():
    help_code = '''
    arma()
    arnma()
    expo()
    moving()
    holtswin()
    sarima()
    pre()
    '''
    print("Available methods in tsacode package:\nExample :\n\timport tsacode as ng\n\tng.moving()")
    print(f"\n{help_code}")

def arma():
    code = '''
# QUESTION 1
install.packages("forecast")
install.packages("tseries")
install.packages("ggplot2")

# Load required libraries
library(forecast)
library(ggplot2)

# Create the time series data
time <- 1:15
values <- c(100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240)
ts_data <- ts(values, start = 1, frequency = 1)

acf(ts_data, main = "ACF of Original Time Series")
pacf(ts_data, main = "PACF of Original Time Series")

#auto.arima(ts_data)

# b. Fit an ARMA(1,1) model to the data
arma_model <- Arima(ts_data, order = c(1, 0, 1))

print(summary(arma_model))

#residual diagnostics of the fitted model
checkresiduals(arma_model) 

#next 10 values
forecasted_values <- forecast(arma_model, h = 10)

print(forecasted_values)

plot(ts_data, main = "Original and Forecasted Values", xlab = "Time", ylab = "Values", col = "blue", lwd = 2, xlim = c(1, 30), ylim=c(100,260))
lines(fitted(arma_model), col = "green", lwd = 2)  # Add fitted values from the model

# Add forecasted values as points for better visibility
points((length(ts_data) + 1):(length(ts_data) + 10), forecasted_values$mean, col = "red", pch = 16)  # Plot forecasted points
lines(forecasted_values$mean, col = "red", lwd = 2)  # Connect forecasted values with a line

legend("bottomright", legend = c("Original", "Fitted", "Forecasted"), col = c("blue", "green", "red"), lwd = 2, pch = c(NA, NA, 5))

###################################################

install.packages("forecast")
install.packages("tseries")
install.packages("ggplot2")

# Load necessary libraries
library(forecast)
library(tseries)
library(ggplot2)

# Create the time series data
sales_data <- c(500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720)
ts_data <- ts(sales_data, frequency = 4)  # Frequency set to 4 for quarterly data

# a. Plot the ACF and PACF of the original time series
par(mfrow=c(1,2))  # Set up the plotting area
acf(ts_data, main="ACF of Original Time Series")
pacf(ts_data, main="PACF of Original Time Series")

# b. Fit an ARMA(1,1) model to the data
arma_model <- Arima(ts_data, order = c(1, 0, 1))  # ARMA(1,1) implies differencing=0

# c. Check the residual diagnostics of the fitted model
checkresiduals(arma_model)

# d. Forecast the next 12 values using the fitted model
forecasted_values <- forecast(arma_model, h = 12)

# Print the forecasted values
print(forecasted_values)

# e. Plot the original time series, the fitted values, and the forecasted values
plot(ts_data, main = "Original and Forecasted Values", xlab = "Time", ylab = "Values", col = "blue", lwd = 2)
lines(fitted(arma_model), col = "green", lwd = 2)  # Add fitted values from the model

# Add forecasted values as points for better visibility
points((length(ts_data) + 1):(length(ts_data) + 10), forecasted_values$mean, col = "red", pch = 16)  # Plot forecasted points
lines(forecasted_values$mean, col = "red", lwd = 2)  # Connect forecasted values with a line

legend("topleft", legend = c("Original", "Fitted", "Forecasted"), col = c("blue", "green", "red"), lwd = 2, pch = c(NA, NA, 16))

grid()
    '''
    print(code)


def arnma():
    code = '''
# Load required libraries
install.packages("forecast")
install.packages("ggplot2")   
install.packages("stats")       

library(stats)  
library(ggplot2)
library(forecast)

set.seed(123)

n <- 100
phi <- 0.5  # AR(1) parameter
epsilon <- rnorm(n, mean = 0, sd = 1)  # White noise
X <- numeric(n)  # Initialize the series
X[1] <- epsilon[1]  # First observation
print(X)
for (t in 2:n) {
  X[t] <- phi * X[t - 1] + epsilon[t]
}

#Plot the time series
plot.ts(X, main = "AR(1) Process Time Series", ylab = "X_t", xlab = "Time", col = "blue")

#AR(1) parameter
ar_model <- arima(X, order = c(1, 0, 0))  # Fit AR(1) model
phi_est <- ar_model$coef[1]  # Extract estimated phi
cat("Estimated AR(1) parameter (phi):", phi_est, "\n")

#ACF and PACF
par(mfrow = c(1, 2))
acf(X, main = "ACF of AR(1) Process")
pacf(X, main = "PACF of AR(1) Process")
par(mfrow = c(1, 1))

# (ii) Discuss the behaviour of ACF and PACF
cat("Behavior of ACF and PACF for AR(1) Process:\n")
cat("ACF: Decays exponentially, indicating a dependency on past values.\n")
cat("PACF: Cuts off after lag 1, confirming the AR(1) nature of the process.\n")

# (i) Fit AR(1) or AR(2) model to the data
ar2_model <- arima(X, order = c(2, 0, 0))
cat("AR(2) Model Coefficients:\n")
print(ar2_model$coef)

#Forecast10 observations
forecasted_values <- forecast(ar2_model, h = 10)
plot(forecasted_values, main = "Forecast for AR(2) Model", ylab = "X_t", xlab = "Time")

###########################################################


install.packages("forecast")
install.packages("ggplot2")   
install.packages("stats")       

library(stats)  
library(ggplot2)
library(forecast)


set.seed(123)

n <- 100
theta <- 0.5
epsilon <- rnorm(n, mean = 0, sd = 1)
X <- numeric(n)
X[1] <- epsilon[1]

# Generate the MA(1) series
for (t in 2:n) {
  X[t] <- epsilon[t] + theta * epsilon[t-1]
}

# Plot
plot.ts(X, main = "Simulated MA(1) Process", ylab = "X_t", col = "blue")

#Plot ACF and PACF
acf(X, main = "ACF of MA(1) Process")
pacf(X, main = "PACF of MA(1) Process")

model_ma1 <- arima(X, order = c(0, 0, 1))  # MA(1) model
summary(model_ma1)

#next 10 observations
forecast_ma1 <- forecast(model_ma1, h = 10)
forecast_ma1
# Plot the forecast
plot(forecast_ma1, main = "Forecast from MA(1) Model")

# Estimate the MA(1) parameter
theta_est <- coef(model_ma1)["ma1"]
cat("Estimated MA(1) parameter (θ):", theta_est, "\n")
    '''
    print(code)


def expo():
    code= '''
install.packages("forecast")
library(forecast)
library(tseries)

years <- 1996:2019
observations <- c(150.3, 150.9, 151.4, 151.9, 152.5, 152.9, 153.2, 153.7, 153.6, 153.5,
                  154.4, 154.9, 155.7, 156.3, 156.6, 156.7, 157, 157.3, 157.8, 158.3, 
                  158.6, 158.6, 159.1, 159.3)

ts_data <- ts(observations, start=1996, end=2019)

ses_model <- ses(ts_data, alpha=0.3, initial="simple")
summary(ses_model)

holt_model <- holt(ts_data, alpha=0.3, beta=0.2, initial="simple")
summary(holt_model)

# Plotting
plot(ts_data, col="black", lwd=2, ylab="Observations", main="Comparison of Smoothing Methods")
lines(fitted(ses_model), col="blue", lwd=2)
lines(fitted(holt_model), col="red", lwd=2)
legend("topleft", legend=c("Original Series", "SES (α=0.3)", "Holt's (α=0.3, β=0.2)"),
       col=c("black", "blue", "red"), lty=1, lwd=2)
    '''
    print(code)


def holtswin():
    code = '''
library(forecast)
library(tseries)
a=data("AirPassengers")
print(a)
# Display the first few rows of the data
head(AirPassengers)

# Plot the original time series
plot(AirPassengers, main="AirPassengers Data", ylab="Number of Passengers", 
     xlab="Year", col="blue", lwd=2)

# Apply Holt-Winters method with multiplicative model
hw_model <- HoltWinters(AirPassengers, seasonal="multiplicative")

# Display the model parameters
hw_model

# Forecast the next 12 months
forecast_hw <- forecast(hw_model, h=12)

# Display the forecasted values
forecast_hw

# Plot the forecast along with the original data
plot(forecast_hw, main="Holt-Winters Forecast for AirPassengers", 
     ylab="Number of Passengers", xlab="Year")
    '''
    print(code)

def moving():
    code = '''
library(tseries)
library(forecast)
# Input the data
years <- 1991:2003
co2_concentration <- c(355.62, 356.36, 357.1, 358.86, 360.9, 362.58, 363.84, 366.58, 
                       368.3, 369.47, 371.03, 373.61, 357.61)

# Create a time series object
ts_co2 <- ts(co2_concentration, start=1991, end=2003)

# Plot the time series data
plot(ts_co2, type="o", col="blue", lwd=2, ylab="Average CO2 Concentration", 
     xlab="Year", main="Atmospheric CO2 Concentration at Mauna Loa (1991-2003)")

# Calculate the 3-year moving average (sides=1 for future forecasting)
moving_avg <- filter(ts_co2, filter=rep(1/3, 3), sides=1)
print(moving_avg)
# Extract the last moving average value as the forecast for 2004
forecast_2004 <- tail(moving_avg, 1)

# Print the forecasted value for 2004
cat("Forecasted CO2 Concentration for 2004:", round(forecast_2004, 2), "\n")

# Combine the forecasted value with the original data
co2_concentration_forecast <- c(co2_concentration, forecast_2004)
ts_co2_forecast <- ts(co2_concentration_forecast, start=1991, end=2004)

# Plot the time series including the forecasted value for 2004
plot(ts_co2_forecast, type="o", col="blue", lwd=2, ylab="Average CO2 Concentration", 
     xlab="Year", main="Atmospheric CO2 Concentration with 2004 Forecast")

# Highlight the forecasted value for 2004
points(2004, forecast_2004, col="red", pch=19)
text(2004, forecast_2004, labels=paste("Forecasted 2004:", round(forecast_2004, 2)), 
     pos=4, col="red")

#############################################################

library(forecast)

years <- 1991:2003
co2_concentration <- c(355.62, 356.36, 357.1, 358.86, 360.9, 362.58, 363.84, 366.58, 
                       368.3, 369.47, 371.03, 373.61, 357.61)

ts_co2 <- ts(co2_concentration, start=1991, end=2003)

moving_avg <- filter(ts_co2, filter=rep(1/3, 3), sides=1)
forecast_2004 <- tail(moving_avg, 1)

# Add the forecasted value for 2004
co2_concentration_forecast <- c(co2_concentration, forecast_2004)
ts_co2_forecast <- ts(co2_concentration_forecast, start=1991, end=2004)

# Predict for future years up to 2009
for (year in 2005:2009) {
  # Update the moving average forecast with the latest 3 values
  moving_avg <- filter(ts_co2_forecast, filter=rep(1/3, 3), sides=1)
  forecast_next <- tail(moving_avg, 1)
  # Add the forecast to the time series
  co2_concentration_forecast <- c(co2_concentration_forecast, forecast_next)
  ts_co2_forecast <- ts(co2_concentration_forecast, start=1991, end=year)
}
print(ts_co2_forecast)

# Print the forecasted value for 2009
forecast_2009 <- tail(ts_co2_forecast, 1)
cat("Forecasted CO2 Concentration for 2009:", round(forecast_2009, 2), "\n")

#forecasted values up to 2009
plot(ts_co2_forecast, type="o", col="blue", lwd=2, ylab="Average CO2 Concentration", 
     xlab="Year", main="Atmospheric CO2 Concentration with Forecasts up to 2009")

# Highlight
points(2009, forecast_2009, col="red", pch=19)
text(2009, forecast_2009, labels=paste("Forecasted 2009:", round(forecast_2009, 2)), 
     pos=4, col="red")
    '''
    print(code)

def sarima():
    code ='''
library(forecast)
library(tseries)
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280, 310, 330,
                220, 230, 250, 240, 260, 280, 320, 300, 290, 310, 330, 350,
                240, 250, 270, 260, 280, 300, 340, 320, 310, 330, 350, 370,
                260, 270, 290, 280, 300, 320, 360, 340, 330, 350, 370, 390,
                280, 290, 310, 300, 320, 340, 380, 360, 350, 370, 390, 410)

sales_ts <- ts(sales_data, start = c(2019, 1), frequency = 12)
sales_ts
plot(sales_ts, main = "Monthly Sales Data", ylab = "Sales", xlab = "Time", col = "blue")
# Decompose
dec = decompose(sales_ts)
plot(dec)
# Differencing the series to remove trend and seasonality
sales_diff <- diff(sales_ts, differences = 1)
sales_seasonal_diff <- diff(sales_ts, lag = 12)
# Plot the differenced series
plot(sales_diff, main = "Differenced Sales Data", ylab = "Sales", xlab = "Time", col = "red")
plot(sales_seasonal_diff, main = "Seasonally Differenced Sales Data", ylab = "Sales", xlab = "Time", col = "green")


*******************************************
library(forecast)
library(tseries)

# Sales time series data
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280, 310, 330,
                220, 230, 250, 240, 260, 280, 320, 300, 290, 310, 330, 350,
                240, 250, 270, 260, 280, 300, 340, 320, 310, 330, 350, 370,
                260, 270, 290, 280, 300, 320, 360, 340, 330, 350, 370, 390,
                280, 290, 310, 300, 320, 340, 380, 360, 350, 370, 390, 410)

# Create a time series object
sales_ts <- ts(sales_data, start = c(2019, 1), frequency = 12)
# 1. Visual Inspection: Plot the time series
plot(sales_ts, main = "Sales Time Series", ylab = "Sales", xlab = "Year")
# 2. ADF Test for Stationarity
adf_test <- adf.test(sales_ts)
cat("ADF Test p-value for original series:", adf_test$p.value, "\n")


# Plot ACF to check for remaining autocorrelation after differencing
acf(sales_ts, main = "ACF of Differenced Series")
pacf(sales_ts, main = "PACF of Differenced Series")

#find D P Q
# Seasonal differencing (if seasonal pattern is observed)
sales_seasonal_diff <- diff(sales_ts, lag = 12)
# Plot ACF and PACF for seasonal differencing
acf(sales_seasonal_diff, main = "ACF of Seasonally Differenced Series")
pacf(sales_seasonal_diff, main = "PACF of Seasonally Differenced Series")

# ADF test for seasonally differenced series
adf_test_seasonal_diff <- adf.test(sales_seasonal_diff)
cat("ADF Test p-value after seasonal differencing:", adf_test_seasonal_diff$p.value, "\n")
#auto.arima(sales_ts, seasonal=T)

*********************************************
  
install.packages("forecast")   
install.packages("tseries")    
install.packages("ggplot2")    
install.packages("ggfortify")  


# Load necessary libraries
library(forecast)   # for forecasting and time series analysis
library(tseries)    # for time series tests
library(ggplot2)    # for data visualization
library(ggfortify)  # for autoplotting time series

# Data Preparation
# Creating a time series object from the sales data
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280,
                310, 330, 220, 230, 250, 240, 260, 280, 320, 300,
                290, 310, 330, 350, 240, 250, 270, 260, 280, 300,
                340, 320, 310, 330, 350, 370, 260, 270, 290, 280,
                300, 320, 360, 340, 330, 350, 370, 390, 280, 290,
                310, 300, 320, 340, 380, 360, 350, 370, 390, 410)

# Create a time series object with a frequency of 12 (monthly data)
ts_sales <- ts(sales_data, start = c(2019, 1), frequency = 12)

# Plot the time series data
autoplot(ts_sales) + 
  ggtitle("Monthly Sales Data") +
  xlab("Year") + ylab("Sales")

# a) Fit a SARIMA model
# Assuming the identified orders are (p=1, d=0, q=1) and (P=1, D=0, Q=1, m=12)
fit_sarima <- Arima(ts_sales, order = c(1, 0, 1), seasonal = c(1, 0, 1))
# Summary of the fitted model
summary(fit_sarima)


# b) Interpret the model output and perform residual diagnostics
# Residual Diagnostics
checkresiduals(fit_sarima)  # Check for autocorrelation and residuals
# ANSWER: After fitting the SARIMA model, it is crucial to evaluate whether the residuals behave like white noise.
# ANSWER: Ljung-Box Test: This test checks for significant autocorrelations in the residuals. If the p-value is greater than 0.05, it suggests that the residuals are not autocorrelated, indicating a good model fit.


# c) If the residuals show autocorrelation, what steps to improve the model
# You can use the Ljung-Box test to check for autocorrelation
Box.test(residuals(fit_sarima), lag = 12, type = "Ljung-Box")
# Answers:
# If significant autocorrelation is found, you might consider:
# - Adding more AR or MA terms
# - Increasing the seasonal parameters (P, D, Q)
# - Differencing the series further or trying different orders

****************************************

install.packages("forecast")   
install.packages("ggplot2")

# Load necessary libraries
library(forecast)  
library(ggplot2)   

sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280, 310, 330,
                220, 230, 250, 240, 260, 280, 320, 300, 290, 310, 330, 350,
                240, 250, 270, 260, 280, 300, 340, 320, 310, 330, 350, 370,
                260, 270, 290, 280, 300, 320, 360, 340, 330, 350, 370, 390,
                280, 290, 310, 300, 320, 340, 380, 360, 350, 370, 390, 410)

# Define the time series object: Monthly data starting from Jan 2019
sales_ts <- ts(sales_data, start = c(2019, 1), frequency = 12)
sarima_model <- auto.arima(sales_ts, seasonal = TRUE)
print(sarima_model)
forecast_values <- forecast(sarima_model, h = 12)
print(forecast_values)
plot(forecast_values, main = "SARIMA Forecast for Next 12 Months")


**********************************************************

install.packages("forecast")
install.packages("tseries")
install.packages("Metrics")

# Load required libraries
library(forecast)  # For ARIMA and SARIMA modeling
library(tseries)   # For residual diagnostics and additional time series functions
library(Metrics)   # For RMSE calculation

# Part a) Fitting ARIMA model without seasonality --------------------------------
# Convert the data to a time series object
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280, 310, 330,
                220, 230, 250, 240, 260, 280, 320, 300, 290, 310, 330, 350,
                240, 250, 270, 260, 280, 300, 340, 320, 310, 330, 350, 370,
                260, 270, 290, 280, 300, 320, 360, 340, 330, 350, 370, 390,
                280, 290, 310, 300, 320, 340, 380, 360, 350, 370, 390, 410)

# Define the time series with monthly frequency starting from January 2019
sales_ts <- ts(sales_data, start = c(2019, 1), frequency = 12)

# Fit an ARIMA model without seasonality
arima_model <- auto.arima(sales_ts, seasonal = FALSE)
print(arima_model)  # Display the fitted ARIMA model

# Part b) Fitting SARIMA model and Model Comparison ------------------------------

# Fit a SARIMA model with automatic parameter selection
sarima_model <- auto.arima(sales_ts, seasonal = TRUE)
print(sarima_model)  # Display the fitted SARIMA model

# Evaluate models using AIC, BIC, and RMSE --------------------------------------

# Extract AIC and BIC for both models
arima_aic <- AIC(arima_model)
arima_bic <- BIC(arima_model)
sarima_aic <- AIC(sarima_model)
sarima_bic <- BIC(sarima_model)

# Forecasting using both models for comparison
arima_forecast <- forecast(arima_model, h = 12)
sarima_forecast <- forecast(sarima_model, h = 12)

# Calculate RMSE for both models based on the training data
arima_rmse <- rmse(sales_ts, fitted(arima_model))
sarima_rmse <- rmse(sales_ts, fitted(sarima_model))

# Display the evaluation metrics
cat("ARIMA Model: AIC =", arima_aic, ", BIC =", arima_bic, ", RMSE =", arima_rmse, "\n")
cat("SARIMA Model: AIC =", sarima_aic, ", BIC =", sarima_bic, ", RMSE =", sarima_rmse, "\n")

# Part c) Visual Comparison of Forecasts ----------------------------------------

# Plot forecasts for ARIMA model
plot(arima_forecast, main = "ARIMA Model Forecast", xlab = "Year", ylab = "Sales", col = "blue")
lines(sales_ts, col = "black", lty = 2)  # Add actual sales data for reference

# Plot forecasts for SARIMA model
plot(sarima_forecast, main = "SARIMA Model Forecast", xlab = "Year", ylab = "Sales", col = "red")
lines(sales_ts, col = "black", lty = 2)  # Add actual sales data for reference

# Part c) Interpretation and Recommendation --------------------------------------

# Interpret the comparison and recommend a model based on metrics
if (sarima_aic < arima_aic & sarima_rmse < arima_rmse) {
  cat("Recommendation: The SARIMA model performs better based on lower AIC, BIC, and RMSE.\n")
} else {
  cat("Recommendation: The ARIMA model performs adequately, but further improvements might be needed.\n")
}


***************************************************

install.packages("forecast")
install.packages("tseries")

# Load necessary libraries
library(forecast)
library(tseries)

# ========== (a) Data Preparation ========== #
# Create a time series object from the sales data
sales_data <- c(200, 220, 240, 210, 230, 250, 300, 270, 260, 280, 310, 330,
                220, 230, 250, 240, 260, 280, 320, 300, 290, 310, 330, 350,
                240, 250, 270, 260, 280, 300, 340, 320, 310, 330, 350, 370,
                260, 270, 290, 280, 300, 320, 360, 340, 330, 350, 370, 390,
                280, 290, 310, 300, 320, 340, 380, 360, 350, 370, 390, 410)

# Create a time series object starting from Jan 2019
ts_sales <- ts(sales_data, start = c(2019, 1), frequency = 12)

# ========== (b) Create Holiday Indicator ========== #
# Create an indicator for holiday months (e.g., December = 1, others = 0)
holiday_indicator <- rep(0, length(sales_data))
holiday_indicator[seq(12, length(sales_data), by = 12)] <- 1  # Set December as holiday

# ========== Fit the Original SARIMA Model ========== #
# Use auto.arima to find the best SARIMA model without holiday effect
sarima_model <- auto.arima(ts_sales, seasonal = TRUE)

# Display the summary of the original SARIMA model
print("=== Original SARIMA Model Summary ===")
summary(sarima_model)

# ========== Fit the Holiday-Adjusted SARIMAX Model ========== #
# Fit a SARIMAX model with the holiday indicator as an exogenous variable
sarimax_model <- auto.arima(ts_sales, xreg = holiday_indicator, seasonal = TRUE)

# Display the summary of the holiday-adjusted SARIMAX model
print("=== Holiday-Adjusted SARIMAX Model Summary ===")
summary(sarimax_model)

# ========== Compare Models ========== #
# Compare AIC values for both models
cat("AIC of SARIMA Model: ", AIC(sarima_model), "\n")
cat("AIC of Holiday-Adjusted SARIMAX Model: ", AIC(sarimax_model), "\n")

# ========== Forecast with Both Models ========== #
# Forecast for the next 12 months with both models
forecast_sarima <- forecast(sarima_model, h = 12)
forecast_sarimax <- forecast(sarimax_model, xreg = rep(1, 12), h = 12)  # Assume holidays continue

# Plot both forecasts for comparison
plot(forecast_sarima, main = "Forecast Comparison: SARIMA vs SARIMAX", col = "blue", xlab = "Year", ylab = "Sales")
lines(forecast_sarimax$mean, col = "red", lty = 2)

# Add legend for better understanding
legend("topleft", legend = c("SARIMA", "Holiday-Adjusted SARIMAX"), 
       col = c("blue", "red"), lty = c(1, 2))

# Display residual diagnostics for both models
print("=== Residual Diagnostics: Original SARIMA ===")
checkresiduals(sarima_model)

print("=== Residual Diagnostics: Holiday-Adjusted SARIMAX ===")
checkresiduals(sarimax_model)

# ANSWERS(a): I introduced a holiday indicator as an exogenous variable to capture the effect of holiday months on sales.

cat("\nAIC=248.24   AICc=249.17   BIC=255.73 AIC of SARIMA Model:  248.243 AIC of Holiday-Adjusted SARIMAX Model:  559.6383\n")
cat("\nThe higher AIC for the SARIMAX model indicates that the holiday effect may not significantly impact sales in this dataset. Thus, the original SARIMA model captures the essential features of the sales data more effectively without the added complexity of the holiday indicator.\n")
cat("\nBased on the AIC comparison, it is advisable to proceed with the SARIMA model for future analysis and forecasting of sales data, as it offers a more parsimonious and effective fit compared to the more complex holiday-adjusted model. \n")

    '''
    print(code)


def pre():
    code ='''
df = read.csv("data.csv")
df$month <- as.Date(df$month, format = "%d-%m-%Y")
start_year <- as.numeric(format(min(df$month), "%y")) #%m freq=1 or 4 %y freq 12  
data <- ts(df$value, start = c(start_year, 1), frequency = 12)
data
plot(data)
    '''
    print(code)