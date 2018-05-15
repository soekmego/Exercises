# Webscraper for stockmarkets
# Can be altered to fit differnt needs.

# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# Specify the URL
quote_page = "https://www.bloomberg.com/quote/SPX:IND"

# Query th website and return the html to the variable 'page'
page = urlopen(quote_page)

# Parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Query the id/class of element and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

# Get the text/content of element
name = name_box.text.strip()

# Get the value corresponding to the text
price_box = soup.find('div', attrs={'class': 'price'})
price = price_box.text

# Get the current time
time = datetime.now()

# Print out to console
# print (name, " ", price, " ", time)

# Print output into a csv file, append results instead of overwriting
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, time])
