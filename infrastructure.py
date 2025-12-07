# This program use yfinance to fetch stock data and perform basic analysis.
# has a function called get_data() and dowload all hourly data for the previous  days fot the following stocks: AAPL, MSFT, GOOGL, AMZN, TSLA.
# Meta, Apple, Amazon, Netflix and Google are the FAANG stocks.
# The fuction will save the data into a folder called 'data' in the current working directory.

# import necessary libraries
import yfinance as yf
import os
from datetime import datetime, timedelta
import pandas as pd
