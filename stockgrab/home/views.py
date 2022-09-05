# Imports
from pickle import GLOBAL
from django.shortcuts import render
from .forms import StockForm
from .scrape import *
from .forms import *
from bs4 import BeautifulSoup
import json
import requests
from datetime import date




def home_page(request):
    '''

    '''    
    # Checking to see if user submitted information
    if request.method=='POST':
        

        # Extracting the tick symbol from input
        
        tick = request.POST['tick']
        #tick_read = requests.get(tick,headers={"User-Agent": ""} )

        # Extracting the start_date from input
        start_date = request.POST['start_date']
        start_date =convert_to_unix_time(start_date)
        # start_date_read = requests.get(start_date,headers={"User-Agent": ""} )
        

        # Extracting the end_date from input
        end_date = request.POST['end_date']
        end_date = convert_to_unix_time(end_date)
        # end_date_read = requests.get(end_date,headers={"User-Agent": ""})

        # Extracting the interval from input
        interval = request.POST['interval']
        # interval_read = requests.get(interval,headers={"User-Agent": ""} )


        
        # Sanity check
        #user_input = f"I need stock {tick} from {start_date} - {end_date} every {interval}"
        url = get_query(tick,start_date,end_date,interval) 
        #jsonStockData = json.loads(obtain.text)
        #print(f"I need stock {tick} from {start_date} - {end_date} every {interval}")

        #print(url)

        list_data = get_data(url)
        df_convert = convert_to_dataframe(list_data) 
        print(df_convert.head())

        return render(request, 'home/results.html', context={'user_input':user_input})
    
    stock_form = StockForm()

    return render(request, 'home/index.html', context={'stock_form':stock_form})