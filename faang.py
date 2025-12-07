# this program create a function called get_data
# that downloads all hourly data for FAANG stocks for the past 5 days
# and saves each stock's data to a separate CSV file using a filename with the format YYYYMMDD-HHmmss.csv.
# and create the data folder if it does not exist.

# Dates and times
import datetime as dt 

# Yahoo Finance data
from arrow import now
import yfinance as yf

# Dates and times
import datetime as dt 

# Yahoo Finance data
import yfinance as yf

# Create a Function 'get_data()'
def get_data():
    df = yf.download(
            ["META", "AAPL", "AMZN", "NFLX", "GOOG"],
            period="5d",
            interval="1h"
        )

        # To get the current date and time
    now = dt.datetime.now()
        # Format date and time.
    #now.strftime("%Y%m%d-%H%M%S")

    # File name.
    filename = "./data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv"

    # Save CSV
    df.to_csv(filename)
    print ("Data saved to", filename)