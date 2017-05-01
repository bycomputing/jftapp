# Create your views here.
import datetime, calendar
from django.shortcuts import render
from jftapp.models import Page

def search(request, template_name, context={}):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            pages = Page.objects.filter(contents__icontains = q)
            return render(request, 'jftapp/search_results.html', {'pages': pages, 'query': q})
    context['error'] = error
    return render(request, template_name, context)

def home(request):
    today = datetime.date.today()
    page = Page.objects.get(date__month=today.month, date__day=today.day)
    return search(request, 'jftapp/home.html', {'page': page})

def index(request):
    pages = Page.objects.all()
    return search(request, 'jftapp/index.html', {'pages': pages})

def about(request):
    return search(request, 'jftapp/about.html')

def by_month(request, month):
    month = datetime.datetime.strptime(month, '%b').month
    month_name = calendar.month_name[month]
    pages = Page.objects.filter(date__month=month)
    return search(request, 'jftapp/by_month.html', {'pages': pages, 'month_name': month_name})

def by_date(request, month, day):
    month = datetime.datetime.strptime(month.capitalize(), '%b').month
    day = datetime.datetime.strptime(day, '%d').day
    page = Page.objects.get(date__month=month, date__day=day)
    return search(request, 'jftapp/by_date.html', {'page': page})

