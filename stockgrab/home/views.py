# Imports

import gzip
from http.client import HTTPResponse
from io import BytesIO
from django.shortcuts import render
import csv
from django.utils.encoding import smart_str

from .forms import StockForm
from .scrape import convert_to_dataframe, convert_to_unix_time, get_query, get_data

def home_page(request):
    '''

    '''    
    # Checking to see if user submitted information
    if request.method=='POST':
        
        # Extracting the tick symbol from input
        tick = request.POST['tick']

        # Extracting the start_date from input
        start_date = request.POST['start_date']
        start_unix = convert_to_unix_time(start_date)

        # Extracting the end_date from input
        end_date = request.POST['end_date']
        end_unix = convert_to_unix_time(end_date)

        # Extracting the interval from input
        interval = request.POST['interval']
        
        # Creating user input
        user_input = f"Grabbed the Stock! \n Here is the data for {tick} from {start_date}-{end_date} every {interval}"
        
        # Get URL given the user inputs 
        url = get_query(tick, start_unix, end_unix, interval) 

        # Get the data
        list_data = get_data(url)
        
        # Convert list of data into a pandas Dataframe
        df = convert_to_dataframe(list_data) 
        # print(df.head())

        # Download the data
        # b = BytesIO()
        # with gzip.open(b, 'wb') as f:
        #     f.write(df.to_csv().encode())
        # response = HTTPResponse(b.getvalue(), content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="stockgrab_data.csv"'

        # response = HTTPResponse(open("uploads/something.txt", 'rb').read())
        # response['Content-Type'] = 'text/plain'
        # response['Content-Disposition'] = 'attachment; filename=DownloadedText.txt'

        return render(request, 'home/results.html', context={'user_input':user_input})
    
    stock_form = StockForm()

    return render(request, 'home/index.html', context={'stock_form':stock_form})