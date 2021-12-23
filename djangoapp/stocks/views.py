from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .tiingo import get_meta_data, get_price_data





def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)

    else:
        form = TickerForm()

   
    return render(request,'index.html',{'form': form})


def ticker(request, tid):
    context = {}
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_price_data(tid)
    return render(request,'ticker.html',context)

def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        stocks=request.POST['stocks']
        print(name,email,phone,stocks)
        obj=contact(name=name,email=email,phone=phone,stocks=stocks)
        obj.save()
    return render(request,'contact.html')    

def success(request):
    context = {}
    return render(request,'success.html',context)    





