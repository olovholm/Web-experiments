# -*- coding: utf-8 -*-

import sys
import urllib2
import HTMLParser
import BeautifulSoup as BeautifulSoup
import HTMLParser
import networkx as nx


def printUsage():
    print " ** USAGE **"
    print "Usage:\tXNFCrawler url depthOfCrawl"
    print "Example:\tXNFCrawler http://www.lovholm.net 2"
    print "Description:\tThis program iterates through URL and harness semantic markup for relationships to make up a social graph"
    print "Note:\t\tdepthOfCrawl should be convertable to an int and is optional"
# Try http://ajaxian.com
try:
    ROOT_URL = sys.argv[1]
except IndexError as e:
    print e
    printUsage()
    
if len(sys.argv) > 2:
    MAX_DEPTH = int(sys.argv[2])
else:
    MAX_DEPTH = 1

XNF_TAGS = set([
    'colleague', 
    'sweethart', 
    'parent',
    'co-resident',
    'co-worker',
    'muse',
    'neighbor',
    'sibling',
    'kin',
    'child',
    'date',
    'spouse',
    'me',
    'acqaintance',
    'met',
    'crush',
    'contact',
    'friend',
])

OUT = "graph.dot"
depth = 0

g = nx.DiGraph()
next_queue = [ROOT_URL]

while depth < MAX_DEPTH:
    depth += 1
    (queue, next_queue) = (next_queue, [])
    
    for item in queue:
        print "will try to open "+item
        try:
            page = urllib2.urlopen(item)
        except urllib2.URLError:
            print 'Failed to fetch ' + item
            continue
        
        try: 
            soup = BeautifulSoup(page)
        except HTMLParser.HTMLParseError as e:
            print 'Failed to parse ' + item
            print e
            continue
        
        anchorTags = soup.findAll('a')
        
        if not g.has_node(item):
            g.add_node(item)
            print "node was added: "+item
        
        
        print "Number of anchor_tags stumbled upon: "+str(len(anchorTags))+ "for item: "+item


