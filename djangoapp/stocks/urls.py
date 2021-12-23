from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    
    path('<str:tid>',views.ticker,name='ticker'),

    path('',views.index,name='index'),
    path('/contact', views.contact, name='contact'), 
    
    
]