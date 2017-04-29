# Create your views here.
import datetime, calendar
from django.shortcuts import render
from jftapp.models import Page

def home(request):
    today = datetime.date.today()
    page = Page.objects.get(date__month=today.month, date__day=today.day)
    return render(request, 'jftapp/home.html', {'page': page})

def index(request):
    pages = Page.objects.all()
    return render(request, 'jftapp/index.html', {'pages': pages})

def about(request):
    return render(request, 'jftapp/about.html')

def by_month(request, month):
    month = datetime.datetime.strptime(month, '%b').month
    month_name = calendar.month_name[month]
    pages = Page.objects.filter(date__month=month)
    return render(request, 'jftapp/by_month.html', {'pages': pages, 'month_name': month_name})

def by_date(request, month, day):
    month = datetime.datetime.strptime(month.capitalize(), '%b').month
    day = datetime.datetime.strptime(day, '%d').day
    page = Page.objects.get(date__month=month, date__day=day)
    return render(request, 'jftapp/by_date.html', {'page': page})

