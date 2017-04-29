import imapemail, os, datetime
from rwtext import write_text
from getpass import getpass

IMAP = 'imap.gmail.com'
label = 'INBOX'
sender = 'lists@jftna.org.nz'
YEAR = 1991

username = raw_input('gmail: ')
password = getpass('Password: ')

def get_date_of(contents):
    month = contents.rsplit()[0]
    day = contents.rsplit()[1]
    try:
        day = int(day)
        month = datetime.datetime.strptime(month, '%B').month
        return month, day
    except ValueError:
        return None, None

def get_contents(message):
    return message.get_payload()[186:-950]

ec = imapemail.EmailClient(username, password, IMAP)
print 'Downloading emails...'
ec.search_emails_from(sender, label)
ec.reverse_search()
messages = ec.get_email_messages()
print 'Found %s emails...' % ec.emails_found

for message in messages:
    contents = get_contents(message)
    month, day = get_date_of(contents)
    if month and day:
        destination = datetime.date(YEAR, month, day).strftime('%Y-%m-%d') + '.txt'
        write_text(contents, 'downloads/' + destination)

