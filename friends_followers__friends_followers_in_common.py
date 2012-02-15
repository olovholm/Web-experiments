# -*- coding: utf-8 -*-

import sys
import redis
import json

from twitter__util import getRedisIdByScreenName
from twitter__util import pp

r = redis.Redis()

def friendsFollowersInCommon(screen_names):
    print "method gets called with args: ", json.dumps(screen_names)
    r.sinterstore('temp$friends_in_common', 
    [getRedisIdByScreenName(screen_name, 'friends_ids')
        for screen_name in screen_names]
    )
    
    r.sinterstore("temp$followers_in_common", 
    [getRedisIdByScreenName(screen_name, 'follower_ids')
        for screen_name in screen_names]
    )
    
    print 'Friends in common for %s: %s' % (', '.join(screen_names),
    pp(r.scard('temp$friends_in_common')))
    
    print 'Followers in common for %s: %s' % (', '.join(screen_names), 
    pp(r.scard('temp$followers_in_common')))
    
    r.delete('temp$friends_in_common')
    r.delete('temp$followers_in_common')
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print >> sys.stderr, "Please suppy at least two screen names. "
        sys.exit(1)
    
    friendsFollowersInCommon(sys.argv[1:]) 