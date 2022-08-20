from django.shortcuts import render
from .forms import StockForm

# Create your views here.
def home_page(request):
    stock_form = StockForm()
    return render(request, 'home/index.html', context={'stock_form':stock_form})