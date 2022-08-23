# Enter helper functions that will provide the necessary query to extract the data
# added changes will be added in time.
# Imports
import datetime
import time
import json
# import calendar
import requests
from bs4 import BeautifulSoup 
from pandas import DataFrame

def convert_to_unix_time(completeDate):
    '''
    Converts human-readable date to unix time

    Parameters:
    -----------
    date: human-readable date

    Return:
    --------
    A datetime in unix format
    '''

    return time.mktime(datetime.datetime.strptime(completeDate, "%m/%d/%y").timetuple())


def get_query(tick, start_date, end_date, interval):
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
    return url


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

    # Create the request
    response = requests.get(query, headers={"user-agent": ""})
    json_stock_data = json.loads(response.text)

    # Extract the data from the json object
    timestamps = json_stock_data["chart"]["result"][0]["timestamp"]
    open = json_stock_data["chart"]["result"][0]["indicators"]["quote"][0]["open"]
    high = json_stock_data["chart"]["result"][0]["indicators"]["quote"][0]["high"]
    low = json_stock_data["chart"]["result"][0]["indicators"]["quote"][0]["low"]
    close = json_stock_data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
    adjustedClose = json_stock_data["chart"]["result"][0]["indicators"]["adjclose"][0]["adjclose"]
    volume = json_stock_data["chart"]["result"][0]["indicators"]["quote"][0]["volume"]

    return [timestamps, open, high, low, close, adjustedClose, volume]

def convert_to_dataframe(list_data):
    '''
    Converts data into a pandas dataframe
    
    '''
    data = DataFrame(list_data).T
    data.columns = ['timestamps', 'open', 'close', 'high', 'low', 'adjustedClose', 'volume']
    return data