# -*- coding: utf-8 -*-
import urllib2
import re
import HTMLParser


URL_PREFIX = "http://www.stortinget.no/no/Representanter-og-komiteer/Representantene/Representantfordeling/Representant/?perid="
f = open("stortingsrepr.txt","r")
fo = open("stortingsrepr_BD.txt","w")

PATTERN = re.compile(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}")


for line in f:
    (etternavn, fornavn, ident) = line.split(';')
    ident = ident.rstrip()
    
    try: 
        print "Opening site for", etternavn, fornavn
        page = urllib2.urlopen(URL_PREFIX+ident)
    except:
        print "Failed to fetch item "+URL
        sys.exit(1)
        
    for line in page:
        if re.search(PATTERN, line) and "Født" in line:
            birthdate = re.findall(PATTERN, line)[0]

    
    fo.write("%s;%s;%s;%s\n" % (etternavn, fornavn, ident, birthdate))
    
fo.close()