from django.shortcuts import render
from .forms import StockForm

# Create your views here.
def home_page(request):
    
    # Did the user submit information
    if request.method=='POST':
        
        #TO DO: Scrape Yahoo Finace to extract the necessary data
        pass
    stock_form = StockForm()
    return render(request, 'home/index.html', context={'stock_form':stock_form})