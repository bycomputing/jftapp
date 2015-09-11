# Create your views here.
from django.shortcuts import render
from datetime import datetime, timedelta
from jftsearch import get_jftreading_contents

def todays_reading(request, h=6, m=30):
    date = datetime.now() - timedelta(hours=h, minutes=m) # Adjust offset as needed
    return just_for_today(request, date)

def page_date(request, month=None, day=None):
    date = datetime.strptime(month.title() + '-' + day, '%b-%d')
    return just_for_today(request, date)

def just_for_today(request, date, template_name='jftapp/jftreading.html'):
    contents = get_jftreading_contents(date)
    return render(request, template_name, {'jft_contents': contents})
