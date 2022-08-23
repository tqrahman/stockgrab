# Imports
from django import forms

class StockForm(forms.Form):

    # Creating a list of possible interval choices
    interval_choices = [
        ('1d', 'Daily'),
        ('1wk', 'Weekly'),
        ('1mo', 'Monthly')
    ]

    tick = forms.CharField(label='Tick Symbol', required=True)
    start_date = forms.DateField(label='Start Date', required=False)
    end_date = forms.DateField(label='End Date', required=False)
    interval = forms.CharField(label='Frequency', required=False, widget=forms.Select(choices=interval_choices))