# -*- coding: utf-8 -*-

import sys
import time
import cPickle
import twitter
from twitter__login import login
from twitter__util import makeTwitterRequest

friends_limit = 10000
SCREEN_NAME = sys.argv[1]
t = login()

def getFriendIds(screen_name=None, user_id=None, friends_limit=10000 ):
    assert screen_name is not None or user_id is not None
    
    ids = []
    cursor = -1

    while cursor != 0:
        params = dict(cursor=cursor)
        if screen_name is not None:
            params['screen_name'] = screen_name
        else: 
            params['user_id'] = user_id
            
        response = makeTwitterRequest(t, t.friends.ids, **params)
        
        ids.extend(response['ids'])
        cursor = response['next_cursor']
        print >> sys.stderr, \
            "Fetched %i ids for %s" % (len(ids), screen_name or user_id)
        if len(ids) >= friends_limit:
            break
    return ids
        
if __name__ == '__main__':
    ids = getFriendIds(sys.argv[1], friends_limit=10000)
    
    print ids

        
        
'''
    if wait_period > 3600: 
        print "Too many retrieves. Saving partial data to disk and exiting"
        f = file('%s.friend_ids' % str(cursor), 'wb')
        cPickle.dump(ids,f)
        f.close()
        exit()
        
    try: 
        response = t.friends.ids(screen_name=SCREEN_NAME, cursor=cursor)
        ids.extend(response['ids'])
        wait_period = 2
    except twitter.api.TwitterHTTPError, e:
        if e.e.code == 401:
            print 'Encountered an 401 Error (Not Authroized)'
            print 'User %s is protecting their tweets' % (SCREEN_NAME, )
        elif e.e.code in (502, 503):
            print 'Encountered %i Error. Trying again in %i seconds'% (e.e.code, wait_period)
            time.sleep(wait_period)
            wait_period *= 1.5
            continue
        elif t.account.rate_limit_status()['remain_hits'] == 0:
            status = t.account.rate_limit_status()
            now = time.time()
            when_rate_limit_resets = status['reset_time_in_seconds']
            sleep_time = when_rate_limit_resets - now
            print 'Rate limit reached. Trying again in %i seconds' % (sleep_time, )
            time.sleep(sleep_time)
            continue
    cursor = response['next_cursor']
    print 'Fetched %i ids for %s' % (len(ids), SCREEN_NAME)
    if len(ids) >= friends_limit:
        break
        
print ids

'''
            
            
            