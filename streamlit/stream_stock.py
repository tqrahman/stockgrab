# Imports
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as stream

import scrape

# SSL
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


#####################
### STREAMLIT APP ###
#####################

stream.write(
    """
    # STOCKGRAB 📈
    ### Grab Your Stock Data Here!

    """
)

interval_choices = {
    'Daily':'1d',
    'Weekly':'1wk',
    'Monthly':'1mo' 
}

tick, start_date, end_date, interval = stream.columns(4)

with tick:
    selected_tick = stream.text_input(
        'TICK SYMBOL',
        'AAPL' 
    )

with start_date:
    selected_start_date = stream.date_input(
        'START DATE',
        datetime.date(2022, 1, 1)
    )

with end_date:
    selected_end_date = stream.date_input(
        'END DATE',
        datetime.date.today()
    )

with interval:
    selected_interval = stream.selectbox(
        'INTERVAL',
        interval_choices.keys(),
        0
    )

# Converting date to unix time
selected_start_date = int(scrape.convert_to_unix_time(selected_start_date))
selected_end_date = int(scrape.convert_to_unix_time(selected_end_date))
selected_interval = interval_choices[selected_interval]

@stream.cache
def get_data():
    query = scrape.get_query(selected_tick, selected_start_date, selected_end_date, selected_interval)
    data = scrape.get_data(query)
    df = scrape.convert_to_dataframe(data)
    df['Date'] = pd.to_datetime(df['Date'].astype('int'), unit='s').dt.date
    df['Volume'] = df['Volume'].astype('int')
    return df

@stream.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

df = get_data()

stream.table(df.head())

###################
### EXPORT DATA ###
###################

csv = convert_df(df)
stream.download_button(
    "Export the Data", 
    csv,
    f"{selected_tick}_stock_data_{selected_start_date}-{selected_end_date}.csv",
    "text/csv",
    key='download-csv'
)

#################
### PLOT DATA ###
#################

fig, ax = plt.subplots()
ax.plot(df['Date'], df['AdjustedClose'])
ax.grid()
ax.set_title(f"{selected_tick} Adjusted Close Price")
ax.set_xlabel("Date")
ax.tick_params(axis='x', labelrotation = 45)
ax.set_ylabel("Adjusted Close")

stream.pyplot(fig)


