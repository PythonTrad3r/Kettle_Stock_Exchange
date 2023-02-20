import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import mplcursors
import math
import config as config


#######################################
#######################################
# Shows the ticker, date, and price when the user hovers over chart data.
def hover_show_details(allDates, allPrices, i) -> str:

    # Holds the ticker Symbol.
    ticker = "JKC"

    # Gets Holds the date of the current i position from all dates.
    # Rounds the i down as it is a decimal and casts it to string.
    date = str(allDates[math.floor(i)])

    # Gets and Holds the price of the current i position from all prices.
    # Rounds the i down as it is a decimal and casts it to string.
    price = '$' + str(allPrices[math.floor(i)])

    # Returns one big string holding the hover over text.
    return ticker + "\n" + date + "\n" + price


# Reads data from the file and enters it into a dataframe.
df = pd.read_csv(os.path.expanduser(config.root_folder + 'data.csv'))

# Creates figure object.
fig = plt.subplot2grid((2,4), (0, 0), rowspan = 100, colspan = 100)

# Title of chart.
plt.title("ShopRite Stock Exchange : JKC")

# Sets the data for the x and y axis.
plt.plot(df['date'], df['price'], label="JKC")

# Sets the x label.
plt.xlabel("Date")

# Sets the y label.
plt.ylabel("Price")

# Shows a lengend with the tickers.
plt.legend()

# Sets the size of the chart.
plt.gcf().set_size_inches(12,6)

# Sets the distance between x values. Only shows every other 2.
plt.xticks(np.arange(0, df['date'].size +1, 2))

# Gets the last quote as a pandas value.
lastQuotePD = df[-1:]

# Gets just the price value.
lastQuote = int(lastQuotePD['price'].values)

# Zooms in to show the latest price on the chart for the x axis.
fig.set_xlim([30, df['date'].size])

# Zooms in to show the latest price on the chart for the x axis.
# Has a $5 buffer for the top. 
fig.set_ylim([False, lastQuote + 5])

# Holds a list of all the dates.
# Used for mouse hover.
allDates = df['date']

# Holds a list of all the prices.
# Used for mouse hover.
allPrices = df['price']

# When the mouse hovers over the line.
# It shows the ticket, the date, and the price.
mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(hover_show_details(allDates, allPrices, sel.index)))

# Shows the chart.
plt.show()


