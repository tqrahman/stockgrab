# Enter helper functions that will provide the necessary query to extract the data
# added changes will be added in time.
# Imports
import datetime
import time
import calendar
import requests
from bs4 import BeautifulSoup 

def convert_to_unix_time(completeDate):
    '''
    Converts human-readable date to unix time

    Parameters:
    -----------
    date: human-readable date
- - - -- - 
    Return:
    --------
    A datetime in unix format
    '''

    time.mktime(datetime.datetime.strptime(completeDate, "%m/%d/%y").timetuple())


    pass

def get_query(tick,start_date,end_date,interval):
    '''
    Creates the query given a tick symbol, start_date, end_date, and interval

    Parameters:
    -----------
    tick: the tick symbol of the stock
    start_date: the start date of the data requested
    end_date: the end date of the data requested
    interval: the frequency of the requested data

    Return:
    --------
    A string that will be used to scrape the site
    '''

    url = f"https://finance.yahoo.com/quote/{tick}/history?period1=print{start_date}&period2={end_date}&interval={interval}&filter=history&frequency=1d&includeAdjustedClose=true"
    url

    pass

def get_data(query):
    '''
    Scrapes the site and returns the data collected.

    Parameters:
    -----------
    query: a string that represents the site to scrap from

    Return:
    -------
    A csv file with the data requested by the user
    '''
userAgent = ""
headers = {"User-Agent": userAgent}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content)

historicalPricesTable = soup.find("table", attrs={"data-test": "historical-prices"})

allStockData = []
#find all the column names, find "thead", then find all "th"
stockRow = []
for header in historicalPricesTable.thead.find_all("th"):
    stockRow.append(header.text)
allStockData.append(stockRow)

#find all the data, find "tbody", then find all "tr", for each row find all "td"
for row in historicalPricesTable.tbody.find_all("tr"):
    stockRow = []
    for data in row.find_all("td"):
        stockRow.append(data.text)
    allStockData.append(stockRow)

#grab the column names, then the data

#first obtain the element containing all the data in the table
#"table", data-test="historical-prices"
historicalPricesTable = soup.find("table", attrs={"data-test": "historical-prices"})

#find all the column names, find "thead", then find all "th"
for header in historicalPricesTable.thead.find_all("th"):
    print(header.text, end="  ")

#find all the data, find "tbody", then find all "tr", for each row find all "td"
for row in historicalPricesTable.tbody.find_all("tr"):
    print()
    for data in row.find_all("td"):
        print(data.text, end="  ")

import csv

with open("Query.csv", "w") as f:
    stockWriter = csv.writer(f)
    stockWriter.writerows(allStockData)
