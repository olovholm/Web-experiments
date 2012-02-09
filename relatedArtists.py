# -*- coding: utf-8 -*-

import sys
import urllib2
from xml.dom.minidom import parseString
import networkx as nx 
import os


LINK_PREAMBLE = "http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=%s&api_key=b25b959554ed76058ac220b7b2e0a026" % sys.argv[1]
MAX_DEPTH = int(sys.argv[2])

OUT = "music_graph.dot"
depth = 0 
g = nx.DiGraph()
next_queue = [LINK_PREAMBLE]


while depth < MAX_DEPTH:
    print "We're going higher"
    depth += 1
    (queue, next_queue) = (next_queue, [])
    
    for item in queue:
        print "size of queue: "+ str(len(queue))
        data = ''
        print "will open "+item
        try:
            page = urllib2.urlopen(item)
        except (urllib2.URLError, ValueError):
            print 'Could not fetch: '+item
            continue
            
        data = page.read()
        page.close()
        dom = parseString(data)
        data = ''
        curr_artist = dom.getElementsByTagName('similarartists')[0].getAttribute('artist')
        artists = dom.getElementsByTagName('artist')
        if not g.has_node(curr_artist):
            g.add_node(curr_artist)
            print "node was added: "+item
        print curr_artist
        
        for artist in artists:
            name = artist.getElementsByTagName('name')[0].firstChild.data
            url = artist.getElementsByTagName('url')[0].firstChild.data
            g.add_edge(curr_artist, name)
            try:
                new_url = "http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=%s&api_key=b25b959554ed76058ac220b7b2e0a026" % urllib2.quote(name)
                next_queue.append(new_url)
            except (KeyError) as e:
                i = 0 
                #Uncomment to solve the coding error
                #print e 
                #print "at name: " +name

            #dom = parseString(artist)
          #  name = dom.getElementsByTagName('name')[0]
          #  print "new element: "+name
            
try:
    nx.drawing.write_dot(g, OUT)
except ImportError, e:
    print "Could not write"
        
        

