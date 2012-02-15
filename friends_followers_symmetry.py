# -*- coding: utf-8 -*-

import sys
import locale
import time
import functools
import twitter
import redis 
from twitter__login import login
from twitter__util import _getFriendsOrFollowersUsingFunc
from twitter__util import getRedisIdByScreenName

SCREEN_NAME = sys.argv[1]
MAXINT = sys.maxint

locale.setlocale(locale.LC_ALL, '')
t = login()
r = redis.Redis()

getFriends = functools.partial(_getFriendsOrFollowersUsingFunc, t.friends.ids, 'friend_ids', t, r)
getFollowers = functools.partial(_getFriendsOrFollowersUsingFunc, t.followers.ids, 'follower_ids', t, r)

screen_name = SCREEN_NAME

print >> sys.stderr, 'Getting friends for %s... ' % (screen_name, )
getFriends(screen_name, limit=MAXINT)
print >> sys.stderr, 'Getting followers for %s...' % (screen_name, )
getFollowers(screen_name, limit=MAXINT)

# Number of Friends and Followers
n_friends = r.scard(getRedisIdByScreenName(screen_name, 'friend_ids'))
n_followers = r.scard(getRedisIdByScreenName(screen_name, 'follower_ids'))

#
n_friends_diff_followers = r.sdiffstore('temp', [getRedisIdByScreenName(screen_name, 'friend_ids'), 
getRedisIdByScreenName(screen_name, 'follower_ids')])

r.delete('temp')

n_followers_diff_friends = r.sdiffstore('temp', [getRedisIdByScreenName(screen_name, 'follower_ids'), 
getRedisIdByScreenName(screen_name, 'friend_ids')])

r.delete('temp')

n_friends_inter_followers = r.sinterstore('temp', 
[getRedisIdByScreenName(screen_name, 'follower_ids'), 
getRedisIdByScreenName(screen_name, 'friend_ids')])

r.delete('temp')

print locale.format('%d', n_friends, True);


print '%s is following %s' % (screen_name, locale.format('%d', n_friends, True))
print '%s is being followed by %s' % (screen_name, locale.format('%d', n_followers, True))
print '%s of %s are not following %s back' % (locale.format('%d', n_friends_diff_followers, True), locale.format('%d', n_friends, True), screen_name)
print '%s of %s are not being followed back by %s' % (locale.format('%d', n_followers_diff_friends, True), locale.format('%d', n_followers, True), screen_name)
print '%s has %s mutual friends ' % (screen_name, locale.format("%d", n_friends_inter_followers, True))