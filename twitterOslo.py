# -*- coding: utf-8 -*-

import twitter
import json
import cPickle
import re
import networkx as nx

'''
This codes follows from the examples in ptwobrussell's Mining the Social Web, published by O'Reilly. 
This code is created by combining two different examples. Temporarily saving through cPickle is comment out.
By running this script and running "circo -Tpng -Ooslo_search_results oslo_search_results.dot" a png image with a network consisting of 
retweets where the term Oslo is used is created. The book is really good so you should buy a copy. 
'''
g = nx.DiGraph()
OUT = "oslo_search_results.dot"


twitter_search = twitter.Twitter(domain="search.twitter.com")
search_results = []
for page in range(1, 6):
    search_results  .append(twitter_search.search(q="oslo", rpp=100, page=page))
    
print json.dumps(search_results, sort_keys=True, indent=1)

tweets = [r['text']
    for result in search_results
        for r in result['results'] ]
        
words = []
for t in tweets:
    words += [ w for w in t.split()]
    
print "total words: " + str(len(words))
print "total unique words" + str(len(set(words)))
'''
f = open("OsloData.pickle", "wb")
cPickle.dump(words, f)
f.close()
'''

#Please remove comments above to import data to OsloData.pickle
#Code below reads data from file and conducts data analysis
'''
words = cPickle.load(open("OsloData.pickle"))
print "Data structure loaded"
print json.dumps(words, sort_keys=True, indent=4)
'''
all_tweets = [tweet 
    for page in search_results
        for tweet in page["results"]  ]
        

def get_rt_sources(tweet):
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)")
    return [ source.strip()
                for tuple in rt_patterns.findall(tweet)
                    for source in tuple
                        if source not in ("RT", "via") ]
                        
for tweet in all_tweets: 
    rt_sources = get_rt_sources(tweet["text"])
    if not rt_sources: continue
    for rt_source in rt_sources:
        g.add_edge(rt_source, tweet["from_user"], {"tweet_id" : tweet["id"]})
        
print "Number of nodes: "+str(g.number_of_nodes())
print "Number of edges: "+str(g.number_of_edges())
print "Number of connected components: "+ str(len(nx.connected_components(g.to_undirected())))

    
try: 
    nx.drawing.write_dot(g, OUT)
except ImportError, e:
    print e


