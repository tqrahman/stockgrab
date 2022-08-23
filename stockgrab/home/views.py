# Imports
from django.shortcuts import render
from .forms import StockForm

def home_page(request):
    '''

    '''    
    # Checking to see if user submitted information
    if request.method=='POST':
        
        # Extracting the tick symbol from input
        tick = request.POST['tick']

        # Extracting the start_date from input
        start_date = request.POST['start_date']
        
        # Extracting the end_date from input
        end_date = request.POST['end_date']
        
        # Extracting the interval from input
        interval = request.POST['interval']
        
        # Sanity check
        user_input = f"I need stock {tick} from {start_date} - {end_date} every {interval}"
        # print(f"I need stock {tick} from {start_date} - {end_date} every {interval}")

        return render(request, 'home/results.html', context={'user_input':user_input})
    
    stock_form = StockForm()
    
    return render(request, 'home/index.html', context={'stock_form':stock_form})