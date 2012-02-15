# -*- coding: utf-8 -*-

import twitter
import json

screen_name = "olovholm"
t = twitter.Twitter(domain="api.twitter.com",api_version="1")
response = t.users.show(screen_name=screen_name)
response2 = t.friends.ids(screen_name=screen_name)
response3 = t.followers.ids(screen_name=screen_name)
print json.dumps(response, sort_keys=True, indent=4)
print json.dumps(response2, sort_keys=True, indent=4)
print json.dumps(response3, sort_keys=True, indent=4)