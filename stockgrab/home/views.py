# Imports

import csv
from django.http import HttpResponse
# from http.client import HTTPResponse
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

        # Download data

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="stockgrab_data.csv"'
        
        # writer = csv.writer(response, csv.excel)
        # response.write(u'\ufeff'.encode('utf8'))

        # # 'timestamps', 'open', 'close', 'high', 'low', 'adjustedClose', 'volume'
        # writer.writerow([
        #     smart_str(u"timestamps"),
        #     smart_str(u"open"),
        #     smart_str(u"close"),
        #     smart_str(u"high"),
        #     smart_str(u"low"),
        #     smart_str(u"adjustedClose"),
        #     smart_str(u"volume"),
	    # ])
        # #get data from database or from text file....
        # # events = event_services.get_events_by_year(year) #dummy function to fetch data
        # for row in df:
        #     writer.writerow([
        #         smart_str(row.timestamps),
        #         smart_str(row.open),
        #         smart_str(row.close),
        #         smart_str(row.high),
        #         smart_str(row.low),
        #         smart_str(row.adjustedClose),
        #         smart_str(row.volume),
        #     ])

        df.to_csv(
            path_or_buf=response,
            sep=';',
            index=False
        )

        # return render(request, 'home/results.html', context={
        #     'user_input':user_input,
        #     'file':response
        # })
        return response
    
    stock_form = StockForm()

    return render(request, 'home/index.html', context={'stock_form':stock_form})