# imapemail.py (ver. 1.0)
# A simple wrapper class for email and imaplib.
#
# By Rye Salvador - 1 September 2015
# Not compatible with Python 3

import email
import imaplib

class EmailClient(object):
    items = []
    emails_found = 0
    def __init__(self, username, password, imap):
        """Authenticates an IMAP object. Logs the user in."""
        self.mailbox = imaplib.IMAP4_SSL(imap)
        self.mailbox.login(username, password)

    def search_emails_from(self, sender, label):
        """Selects where in the mailbox to look for
           and search emails from whom."""
        self.mailbox.select(label.upper())
        self.response, data = self.mailbox.search(None, '(FROM %s)' % sender)
        self.items = data[0].split()
        self.emails_found = len(self.items)

    def get_email_message(self, index):
        """Return a message object. Reference by index."""
        for item in self.items[index - 1:index]:
            message = self.retrieve_message_in(item)
            return message

    def get_email_messages(self, start=None, stop=None):
        """Return a list of message objects. If no parameters were given
           then it returns all message objects in the items list.

           It might take some time if the list is big."""
        messages = []
        if start==None and stop==None:
            for item in self.items:
                messages.append(self.retrieve_message_in(item))
            return messages
        elif start==None or stop==None:
            return
        for item in self.items[start - 1:stop]:
            messages.append(self.retrieve_message_in(item))
        return messages

    def reverse_search(self):
        """Reverse email items from first email to most recent,
           to to most recent to first."""
        self.items.reverse()

    def retrieve_message_in(self, item):
        """Receives an item object from traversing thru the items list.
           Return a message object."""
        response_part, email_id = self.mailbox.fetch(item, "(RFC822)")
        for id in email_id:
            if isinstance(id, tuple):
                return email.message_from_string(id[1])
