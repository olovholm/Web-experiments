# -*- coding: utf-8 -*-
import sys
import urllib2
import HTMLParser
import re
from BeautifulSoup import BeautifulSoup

'''
This script goes through the Norwegian Parliament's list over representatives and compiles a list with name and ID. 
The ID can later be used for aquiring more information such as party and committee.
'''

URL = "http://stortinget.no/no/Representanter-og-komiteer/Representantene/Representantfordeling/"
PATTERN = re.compile(r"Representanter-og-komiteer/Representantene/Representantfordeling/Representant/\?perid=(\w*)\">([a-å]*), ([a-å]*)", re.IGNORECASE)
ID_PATTERN = re.compile(r"perid=>")



try: 
    page = urllib2.urlopen(URL)
except:
    print "Failed to fetch item "+URL
    sys.exit(1)
    
    
try:
    soup = BeautifulSoup(page)
except HTMLParser.HTMLParseError as e:
    print "failed to parse "+ URL
    sys.exit(1)

anchors = soup.findAll('a')


for a in anchors:  
    if re.search(PATTERN,str(a)):
        a = re.search(PATTERN,str(a))
        print "ID:",(a.group(1))
        print "Etternavn:",a.group(2)
        print "Fornavn:",a.group(3),"\n"

        