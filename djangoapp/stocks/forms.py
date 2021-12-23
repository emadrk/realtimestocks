from django import forms


class TickerForm(forms.Form):
    ticker = forms.CharField(label="Write Ticker",max_length=10)



