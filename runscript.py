# runscript.py
# You can add this script to your scheduled jobs if you don't have
# the JFT reading texts in your database yet. Adjust to JFT email
# subscription time received stamp accordingly.
#
# By Rye Salvador - 6 September 2015

import imapemail
from funtext import save_to_textfile
import argparse, os

# Change the following with your login information.
username = 'noreply@example.com'
password = 'foobar'
IMAP = 'imap.gmail.com'
label = 'INBOX'
sender = 'lists@jftna.org.nz'
download_path = 'downloads'

script_path = os.path.dirname(os.path.abspath(__file__))

def save_jft(message):
    """Save JFT reading into textfile using email Subject as filename."""
    contents = message.get_payload()[186:-950] # Splice message body.
    destination = script_path + '/' + download_path + '/' + str(message['Subject']) + '.txt'
    save_to_textfile(contents, destination)

def main():
    """Main function. Takes one optional argument.

       Type `$ python runscript.py -h' for help."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='save all jft emails', action='store_true')
    args = parser.parse_args()

    ec = imapemail.EmailClient(username, password, IMAP)
    ec.search_emails_from(sender, label)
    ec.reverse_search()

    if args.all:
        messages = ec.get_email_messages()
        print 'Downloading %s emails...' % ec.emails_found
        for message in messages:
            save_jft(message)
    else:
        message = ec.get_email_message(1)
        save_jft(message)

if __name__ == '__main__':
    main()
