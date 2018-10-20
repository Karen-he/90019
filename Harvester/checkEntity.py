# import tweepy
from couchdb import Server
# import json
# import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import *
from Locate import *
import sys
from findHashtag import *


# DB_Name = ['stream', 'search']
DB_Name = ['test']
# db_id = sys.argv[1]

# connet to couchdb
server = Server('http://admin:hekeren@127.0.0.1:5984/')

# instance of do sentiment analysis
analyzer = SentimentIntensityAnalyzer()

def loopDB():
    for i in DB_Name:
        db = server[i]
        for id in db:
            doc = dict(db[id])
            # doc = dict(doc)
            checkColunm(doc)
            db.save(doc)


def checkColunm(doc):
    # nid = doc['id_str']
    # doc = dict(doc)
    for i in ['hasHashtag', 'triggerHashtag', 'sentiment', 'suburb']:
        if i not in doc.keys() or (doc[i] == 0):
            text = doc['text']
            coordinates = doc['coordinates']
            # nuser = doc['user']
            # ntime = doc['created_at']
            # nplace = doc['place']
            # nentities = doc['entities']
            sentiment = analyzer.polarity_scores(text)
            suburb = give_suburb(coordinates)
            hashtag = hasHashtag(text)
            tags = doc['entities']['hashtags']
            triggerHashtag = searchHashtag(tags)
            doc['hasHashtag'] = hashtag
            doc['triggerHashtag'] = triggerHashtag
            doc['sentiment'] = sentiment
            doc['suburb'] = suburb
            # # generate new tweeter
            # ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
            #         'coordinates': ncoordinates, 'create_time': ntime,
            #         'place': nplace, 'entities': nentities,
            #         'addressed': False, 'sentiment': sentiment, 'suburb': suburb, 'hasHashtag': hashtag,
            #         'triggerHashtag': triggerHashtag}

            # db.save(doc)
            print(doc['id'])
            print('********************************************')
            break
loopDB()