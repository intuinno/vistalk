from twython import Twython
from twython import TwythonStreamer

APP_KEY='AtDvumv2XT7iAbzsPEInQ'
APP_SECRET = 'z5atyQUwygHxSuSlBGTUMgflzudWzYBkSalPLx5FF4U'

OAUTH_TOKEN='38975687-rBGM5Wj23VNdYz8n8Gg8zMqgOBKfZ4uHaZ5uCH8MD'
OAUTH_TOKEN_SECRET='qpPMWwzMgWt2kYocyLM6nI3NUEcyWK2FHw8MlT8j90'

# twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# twitter.verify_credentials()

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

stream = MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='twitter')
