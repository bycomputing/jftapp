# funtext.py
# Routine functions on reading and saving textfiles
# to help make code more readable.
#
# By Rye Salvador - 5 September 2015

import os

def read_text(source):
    """Return contents of source file.

       Source is the absolute path and the filename to be read.
       Contents must be of type string."""
    try:
        f = open(source, 'r')
    except IOError:
        print 'Error: Can\'t find file or read data or path does not exist.'
    else:
        contents = f.read()
        f.close()
        return contents 

def write_text(contents, destination):
    """Save contents to destination file.

       Contents must be of type string.
       Destination is the absolute path and the filename to be saved.

       Notes: It will not overwrite existing files
              with the same filename as the destination."""
    if not os.path.exists(destination):
        try:
            with open(destination, 'w') as f:
                f.write(contents)
        except IOError:
            print 'Error: Can\'t find file or read data or path does not exist.'
        else:
            print 'Saving to textfile %s done. :>' % destination
    else:
        print 'File already exists. Nothing to be done.'
