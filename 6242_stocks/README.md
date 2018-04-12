# Short Term Stock Price Prediction Using Recurrent Neural Network
OHLC Average Prediction Using LSTM Recurrent Neural Network

# Dataset:
The dataset is taken from Quandl. The dataset consists of Open, High, Low and Closing Prices 
# Price Indicator:
Stock traders mainly use three indicators for prediction: OHLC average (average of Open, High, Low and Closing Prices), HLC average (average of High, Low and Closing Prices) and Closing price, In this project, OHLC average has been used.
# Data Pre-processing:
After converting the dataset into OHLC average, it becomes one column data. This has been converted into two column time series data, 1st column consisting stock price of time t, and second column of time t+1. All values have been normalized between 0 and 1.
# Model: 
Two sequential LSTM layers have been stacked together and one dense layer is used to build the RNN model using Keras deep learning library. Since this is a regression task, 'linear' activation has been used in final layer.
# Training:
75% data is used for training. Adagrad (adaptive gradient algorithm) optimizer is used for faster convergence.
After training starts it will look like:

# Test:
Test accuracy metric is root mean square error (RMSE).




