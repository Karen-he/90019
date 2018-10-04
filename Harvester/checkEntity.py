import tweepy
from couchdb import Server
import json
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import *
from Locate import *
import sys
from findHashtag import *


DB_Name = ['stream', 'search']
db_id = sys.argv[1]

# connet to couchdb
server = Server('http://admin:hekeren@127.0.0.1:5984/')
try:
    db = server[DB_Name[db_id]]
except:
    db = server.create(DB_Name[db_id])

# instance of do sentiment analysis
analyzer = SentimentIntensityAnalyzer()


# # time_label added
# def time_label(tweet_time):
#     time_parse = tweet_time.split(' ')[3]
#     time_tag = time_parse[:2]
#     return time_tag


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            nid = tweet["id_str"]

            if nid in db:
                print('--------already saved----------------')
                return True
            else:
                ntext = tweet['text']
                ncoordinates = tweet['coordinates']
                nuser = tweet['user']
                ntime = tweet['created_at']
                nplace = tweet['place']
                nentities = tweet['entities']
                sentiment = analyzer.polarity_scores(ntext)
                # swearing = lable_swearing(ntext)
                # generate new tweeter
                # topic = give_label(ntext)
                # time_tag = time_label(ntime)
                suburb = give_suburb(ncoordinates)
                hashtag = hasHashtag(ntext)
                triggerHashtag = searchHashtag(tags)
                ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                        'coordinates': ncoordinates, 'create_time': ntime,
                        'place': nplace, 'entities': nentities,
                        'addressed': False, 'suburb': suburb, 'sentiment': sentiment, 'hasHashtag': hashtag, 'triggerHashtag': triggerHashtag}
                db.save(ndoc)
                print(nid)
                print('-------------------------------------')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))

        return True

    def on_error(self, status):
        print(status)
        """ Handle any error throws from stream API """
        if status == 420:
            self.on_timeout()

    def on_timeout(self):
        """ Handle time out when API reach its limit """
        print("API Reach its limit, sleep for 10 minutes")
        time.sleep(60 * 16)
        return


# print config information
print('Auth_id: ' + str(auth_id))
print('GEOCODE: ' + str(GEOBOX))
print('database: ' + DB_Name)

# auth twitter account
consumer_key = AUTH[auth_id]['consumer_key']
consumer_secret = AUTH[auth_id]['consumer_secret']
access_token = AUTH[auth_id]['access_token']
access_token_secret = AUTH[auth_id]['access_token_secret']
# Creation of the actual interface, using authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def start_stream():
    while True:
        try:
            #start stream app
            myStreamListener = MyStreamListener()
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
            myStream.filter(locations=GEOBOX, languages=["en"])
        except:
            continue

start_stream()


def checkColunm(doc):
    nid = doc['id_str']
    for i in ['hasHashtag', 'triggerHashtag']:
        if len(doc[i]) == 0:
            ntext = doc['text']
            ncoordinates = doc['coordinates']
            nuser = doc['user']
            ntime = doc['created_at']
            nplace = doc['place']
            nentities = doc['entities']
            sentiment = analyzer.polarity_scores(ntext)
            # swearing = lable_swearing(ntext)
            # topic = give_label(ntext)
            # time_tag = time_label(ntime)
            suburb = give_suburb(ncoordinates)
            hashtag = hasHashtag(ntext)
            triggerHashtag = searchHashtag(tags)
            # generate new tweeter
            ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                    'coordinates': ncoordinates, 'create_time': ntime,
                    'place': nplace, 'entities': nentities,
                    'addressed': False, 'sentiment': sentiment, 'suburb': suburb, 'hasHashtag': hashtag,
                    'triggerHashtag': triggerHashtag}
            db.save(ndoc)
            print(nid)
            print('********************************************')