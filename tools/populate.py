import django, datetime, sys, os
from optparse import OptionParser

def main():
    sys.path.append(os.path.pardir)
    sys.path.append(os.path.join(os.path.pardir, os.path.pardir))
    usage = "usage: %prog -s yoursite.settings | --settings=yoursite.settings"
    parser = OptionParser(usage)
    parser.add_option('-s', '--settings', dest='settings', metavar='SETTINGS',
                      help="The Django settings module to use")
    (options, args) = parser.parse_args()
    if not options.settings:
        parser.error("You must specify a settings module")

    os.environ['DJANGO_SETTINGS_MODULE'] = options.settings
    django.setup()
    from jftapp.models import Page

    YEAR = 1991
    textfiles = os.listdir('downloads')

    for tf in textfiles:
        with open('downloads/' + tf) as f:
            contents = f.read()
            day = contents.rsplit()[1]
            month = contents.rsplit()[0]
            heading = contents.splitlines()[2]
        try:        
            day = int(day)
            month = datetime.datetime.strptime(month, '%B').month
            p = Page.objects.create(heading=heading,
                            date=datetime.date(YEAR, month, day),
                            contents=contents)
            print('Creating entry:\n{}\nPage ID: {}\ndone...'.format(p, p.id))
        except ValueError:
            print('Corrupt textfile')
            continue

if __name__ == '__main__':
    main()
