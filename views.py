# Create your views here.
import datetime, calendar
from django.shortcuts import render
from jftapp.models import Page
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

ITEMS_PER_PAGE = 12

def paginate(request, query_set, context={}):
    paginator = Paginator(query_set, ITEMS_PER_PAGE)
    try:
        page_number = int(request.GET['page'])
    except (KeyError, ValueError):
        page_number = 1
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404
    entries = page.object_list
    context.update({
        'pages': entries,
        'show_paginator': paginator.num_pages > 1,
        'has_prev': page.has_previous(),
        'has_next': page.has_next(),
        'page': page_number,
        'num_pages': paginator.num_pages,
        'next_page': page_number + 1,
        'prev_page': page_number - 1
        })
    return context

def search(request, template_name, context={}):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            pages = Page.objects.filter(contents__icontains = q)
            context = {'orig_pages': pages, 'query': q}
            return render(request, 'jftapp/search_results.html', paginate(request, pages, context))
        context['error'] = error
    return render(request, template_name, context)

def home(request):
    today = datetime.date.today()
    page = Page.objects.get(date__month=today.month, date__day=today.day)
    return search(request, 'jftapp/home.html', {'page': page})

def index(request):
    pages = Page.objects.all()
    return search(request, 'jftapp/index.html', paginate(request, pages))

def about(request):
    return search(request, 'jftapp/about.html')

def by_month(request, month):
    month = datetime.datetime.strptime(month, '%b').month
    month_name = calendar.month_name[month]
    pages = Page.objects.filter(date__month=month)
    context = {'month_name': month_name}
    return search(request, 'jftapp/by_month.html', paginate(request, pages, context))

def by_date(request, month, day):
    month = datetime.datetime.strptime(month.capitalize(), '%b').month
    day = datetime.datetime.strptime(day, '%d').day
    page = Page.objects.get(date__month=month, date__day=day)
    return search(request, 'jftapp/by_date.html', {'page': page})

