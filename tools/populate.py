import django, os, datetime
django.setup()
from jftapp.models import Page

YEAR = 1991
textfiles = os.listdir('jftapp/downloads')

for tf in textfiles:
    with open('jftapp/downloads/' + tf) as f:
        contents = f.read()
        day = contents.rsplit()[1]
        month = contents.rsplit()[0]
        heading = contents.splitlines()[2]
    try:        
        day = int(day)
        month = datetime.datetime.strptime(month, '%B').month
        Page.objects.create(heading=heading,
                            date=datetime.date(YEAR, month, day),
                            contents=contents)
    except ValueError:
        print('Corrupt textfile')
        continue

