
import re
import requests
import json
from requests_oauthlib import OAuth1Session
import datetime
import dateutil.parser
import sys

try:
  query = sys.argv[1]
except:
  query = 'data'

twitter_url = 'https://stream.twitter.com/1.1/statuses/filter.json?language=en&track=' + query

host         = '45.55.207.56'
url          = 'http://' + str(host) + ':61051/SASESP/windows/Twitter/CQ1/Data_Input/state?value=injected'
headers      = {'Content-Type': 'application/xml'}

key          = ""
secret       = ""
token        = ""
token_secret = ""

twitter = OAuth1Session(key, client_secret=secret,
                        resource_owner_key=token,
                        resource_owner_secret=token_secret)

r = twitter.get(
    twitter_url,
    stream=True
)

print '\n\nTwitter Response Code:  ' + str(r) + '\n\n'

for line in r.iter_lines():
    try:
        requests.put(url, data=str('''
            <events>
                <event>
                    <opcode>i</opcode>
                    <ID key='true'>'''  + json.loads(line)["id_str"]                        + '''</ID>
                    <Author>'''         + json.loads(line)["user"]["screen_name"]           + '''</Author>
                    <Tweets>'''         + json.loads(line)["text"]                          + '''</Tweets>
                    <Followers>'''      + str(json.loads(line)["user"]["followers_count"])  + '''</Followers>
                    <Timestamp>'''      + str(dateutil.parser.parse(re.sub('\+.+','',json.loads(line)["created_at"]))) + '''</Timestamp>
                </event>
            </events>'''), headers=headers)
        #print json.loads(line)["created_at"]
        #print json.loads(line)["user"]["followers_count"]
    except:
        pass


