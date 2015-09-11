# jftsearch.py
# Functions used by views.py to retrieve JFT readings.
#
# By Rye Salvador - 5 September 2015

import os
from os.path import expanduser
from datetime import datetime
from models import JFTReading
from funtext import read_textfile
from runscript import download_path

script_path = os.path.dirname(os.path.abspath(__file__))
search_path = script_path + '/' + download_path

def month_convert_to_words(month):
    """Return the alphabetical equivalent of the given chronological value
       of a Gregorian calendar based month."""
    monthDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    return monthDict[month]

def search_textfiles_for_jftreading(month, date):
    """Return the textfile path and filename."""
    files = os.listdir(search_path)
    month_files = []
    # print 'Searching downloaded textfiles...'
    for f in files:
        if month in f:
            month_files.append(f)
    for f in month_files:
        if date in f:
            return search_path + '/' + f
    # print '%s %s textfile not found.' % (month, date)
    return None

def jftreading_in_database(tagname):
    """Return True if JFT reading object found from the database
       else it return False."""
    try:
        jftreading = JFTReading.objects.get(tagname=tagname)
    except JFTReading.DoesNotExist:
        # print 'Record not found in database; fall back to searching downloaded textfiles.'
        return False
    else:
        return True

def get_jftreading_contents(date_given):
    """Return JFT reading contents."""
    date_today = datetime.now()
    weekday, day, month, year = date_given.strftime('%A %d %B %y').split()
    tagname = '[Jft] Just for Today Reading - %s %s' % (month, day)

    # Check JFT in the database. 
    if jftreading_in_database(tagname):
        jftreading = JFTReading.objects.get(tagname=tagname)
        contents = jftreading.contents
        return contents

    # We run the download script in case scheduled task failed.
    if search_textfiles_for_jftreading(month, day) == None:
        if date_given.month == date_today.month and date_given.day == date_today.day:
            os.system('python %s/runscript.py' % script_path)

    # Check JFT in the textfiles.
    filename = search_textfiles_for_jftreading(month, day)
    if filename != None:
        contents = read_textfile(filename)
        JFTReading.objects.create(tagname=tagname, contents=contents)
        return contents
