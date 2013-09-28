import urllib2, base64, json

# NOTE: Put your consumer key & secret here
CONSUMER_KEY = b'AtDvumv2XT7iAbzsPEInQ'
CONSUMER_SECRET = b'z5atyQUwygHxSuSlBGTUMgflzudWzYBkSalPLx5FF4U'

#
# Step 1: Encode consumer key and secret
#

base64_consumer_key_secret = base64.b64encode(
    urllib2.quote(CONSUMER_KEY) + b':' + urllib2.quote(CONSUMER_SECRET))

#
# Step 2: Obtain a bearer token
#

# note: the following line won't verify server certificate; to do so you'll have to
#       use python3 and specify cafile & capauth
request = urllib2.Request("https://api.twitter.com/oauth2/token")
request.add_header('Authorization', b'Basic ' + base64_consumer_key_secret)
request.add_header("Content-Type", b'application/x-www-form-urlencoded;charset=UTF-8')
request.add_data(b'grant_type=client_credentials')

resp = urllib2.urlopen(request)
data = json.load(resp)
if data['token_type'] != 'bearer':
    throw("Bad token_type: " + data['token_type'])
access_token = data['access_token']

print("access_token: " + access_token)
print('')

#
# Step 3: Authenticate API requests with the bearer token
#

request = urllib2.Request(
        'https://api.twitter.com/1.1/statuses/user_timeline.json?count=3&screen_name=twitterapi'
    )
request.add_header('Authorization', b'Bearer ' + access_token)

resp = urllib2.urlopen(request)
data = json.load(resp)

print("Result:")
print(json.dumps(data, indent=4, separators=(',', ': ')))