# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 01:18:08 2016

@author: rahul
"""

import re

match = re.search("iig", "piiig")
match.group()

# . (dot) any char
# \w word char
# \d digit
# \s whitespace \S non-whitespace


def Find(pat, text):
    match = re.search(pat, text)
    if match: print match.group()
    else: print 'not found'
        
Find("gh", "poghti")
Find('...ty', 'potty')

Find('..gs' , 'he wasg runnigss')


## raw string  'r' passes out the string character string without being worry about the backslashes
Find(r'c\.l', 'c.lled piig sgsgn lkgo' )


## matching word character " \w "
Find(r':\w\w\w', 'blah :cat cat cat dog')   # :cat result
Find(r':\d\d\d',"blah :123srg")

Find(r':\d\s\d',"blah :1 23srg")
 
Find(r'\d\s+\d\s+\d',"blah :1 2        3srg")

Find(r':\w+' , 'blah :kitten 1 2        3srg')

Find(r':.+' , 'blah :kitten 1 2        3srg')

#to terminate at first white space character
Find(r':\S+', 'blah :kitten$jnfif vn24')

# allowing the set of characters inside the square brackets so as to work with dot char before & after @
Find(r'[\w.]+@[\w.]+', 'blah fg.y@gmail.com @ vn24')

## square bracket is essential if you are looking for some list of char together

Find(r'[\w.]+@[\w.]+', 'blah fg.y@gmail.com @ vn24')

#first has to be the word .... + here changes to *(star)
Find(r'\w[\w.]*@[\w.]+', 'blah .fg.y@gmail.com @ vn24')

m = re.search(r'([\w.]+)@([\w.]+)', 'blah fg.y@gmail.com @ vn24')

m.group()
m.group(1)

re.findall(r'[\w.]+@[\w.]+', 'blah fg.y@gmail.com ,ty@vn24')
re.findall(r'([\w.]+)@([\w.]+)', 'blah fg.y@gmail.com ,ty@vn24')

dir(re)






import re
def removePunctuation(text):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.

    Note:
        Only spaces, letters, and numbers should be retained.  Other characters should should be
        eliminated (e.g. it's becomes its).  Leading and trailing spaces should be removed after
        punctuation is removed.

    Args:
        text (str): A string.

    Returns:
        str: The cleaned up string.
    """
    
    m = re.sub(r'[^a-z0-9\s]','',text.lower().strip())
    return m
    
    
    
print removePunctuation('Hi, you!')
print removePunctuation(' No under_score!')
print removePunctuation(' *      Remove punctuation then spaces  * ')











