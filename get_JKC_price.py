
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from datetime import date
import os
import config as config

# URL for ShopRite KETTLE BRAND Jalapeno, Potato Chips, 7.5 Ounce
url = "https://www.shoprite.com/sm/pickup/rsid/3000/product/kettle-brand-jalapeo-potato-chips-75-oz-00084114902047"

s = Service(ChromeDriverManager().install())

# Variole to hold options for Chrome.
options = Options()

# Sets the browser to run in the background.
options.add_argument("--disable-extensions")
options.add_argument('--disable-application-cache')
options.add_argument('--disable-gpu')
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--headless')

# Creates undetected chrome driver with options.
# Sets the process to run in the background.
browser = uc.Chrome(use_subprocess = True,driver_executable_path = s.path)

# Requests information from the URL.
browser.get(url)

# Gets the HTML output in text format (one lone string).
html_output = browser.find_element(By.XPATH, "/html/body").text

# Splits the strings by new line.
html_output = html_output.split("\n")

# Get's today's date.
today = date.today()

# Parses the HTML output looking for strings that have'$' in it.
# Once it finds it, it knows that the price is the 2nd string.
counter = 0
for row in html_output:

    # Checks for $ in the row.
    if '$' in row:

        # The second $ has the price in it.
        if counter == 1:

            # Checks '2 for 5'.
            if 'was' in row:

                # Splits the row and separates the dollar sign from the string.
                price = row.split(' ')
                priceSTR = price[2].split('$')

                # Casts the price into float.
                priceInt = float(priceSTR[1])

                # Since it's 2 for 5, it divides the price in two.
                final_price = str(priceInt/2)
            
            # Regular price.
            else:

                # Separates the dollar sign from price and casts it to float.
                price = row.split('$')
                final_price = float(price[1])
            break
    
        # increments counter to go to the next '$'.
        counter += 1

# Opens the file in the Documents folder and appends new data to it.
with open(os.path.expanduser(config.root_folder + 'Kettle/data.csv'), 'a') as f:
    f.write(today.strftime("%m/%d/%Y") + "," + str(final_price) + "\n")

# Quits the browser.
browser.quit()

# Quits the program.
quit()