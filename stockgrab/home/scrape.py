# Enter helper functions that will provide the necessary query to extract the data

# Imports

def convert_to_unix_time():
    '''
    Converts human-readable date to unix time

    Parameters:
    -----------
    date: human-readable date

    Return:
    --------
    A datetime in unix format
    '''
    pass

def get_query():
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
    pass

def get_data():
    '''
    Scrapes the site and returns the data collected.

    Parameters:
    -----------
    query: a string that represents the site to scrap from

    Return:
    -------
    A csv file with the data requested by the user
    '''
    pass