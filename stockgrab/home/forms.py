# Imports
from django import forms

class StockForm(forms.Form):
    tick = forms.CharField(required=True)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    interval = forms.CharField(required=False)