# this program create a function called get_data
# that downloads all hourly data for FAANG stocks for the past 5 days
# and saves each stock's data to a separate CSV file using a filename with the format YYYYMMDD-HHmmss.csv.
# and create the data folder if it does not exist.

# Dates and times
import datetime as dt 

# Yahoo Finance data
import yfinance as yf

# Operating system
import os

# import DataFrames
import pandas as pd

# import matplotlib for plotting
import matplotlib.pyplot as plt

# use shebang to run this file directly from the command line
#!/usr/bin/env python3

# create the function
def get_data():
    '''Download the FAANG hourly for the last 5 days and save it in a folder called (data)'''
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

    # Download hourly prices for the past 5 days
    df = yf.download(tickers, period="5d", interval="1h")
    
    
    # Save data as CSV
    # Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True) #This create a directory if doesn't exist

    '''Format to the data and time. We can use 'now.strftime'''
    # File name with format date and time.
    filename = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    filename_time = f"{data_dir}/{filename}"

    '''The return keyword is to exit a function and return a value. Source: https://www.w3schools.com/python/ref_keyword_return.asp'''
    df.to_csv(filename_time)
    return df, filename_time

# call the function
data, file_path = get_data()
print(f"Data saved to {file_path}")
# print the first 5 rows of the data
print(data.head())

# Plot the closing prices of FAANG stocks
# The function plot_data() opens the latest data file in the data folder and plots the Close prices for each of the five stocks. 
# The plot include axis labels, a legend, and the date as a title. 
# The function save the plot into a plots folder in the root of this repository using a filename in the format YYYYMMDD-HHmmss.png.

def plot_data():
    '''Plot the closing prices of FAANG stocks from the latest data file'''
    data_dir = "data"
    plot_dir = "plots"
    os.makedirs(plot_dir, exist_ok=True) #This create a directory if doesn't exist

    # Get the latest file in the data directory
    files = os.listdir(data_dir)
    latest_file = max([os.path.join(data_dir, f) for f in files], key=os.path.getctime)
    # getctime get the creation time of the file
    # source: https://docs.python.org/3/library/os.path.html#os.path.getctime

    # Read the data
    df = pd.read_csv(latest_file, header=[0,1], index_col=0, parse_dates=True)

    # Plot the closing prices
    plt.figure(figsize=(12, 6))
    for ticker in ["META", "AAPL", "AMZN", "NFLX", "GOOG"]:
        plt.plot(df.index, df[('Close', ticker)], label=ticker)

    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.title(f'FAANG Stocks Closing Prices - {dt.datetime.now().strftime("%Y-%m-%d")}')
    plt.legend()
    plt.grid()

    # Save the plot
    plot_filename = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"
    plot_filepath = os.path.join(plot_dir, plot_filename)
    plt.savefig(plot_filepath)
    plt.close()
    return plot_filepath

# call the plot function
plot_file_path = plot_data()
print(f"Plot saved to {plot_file_path}")