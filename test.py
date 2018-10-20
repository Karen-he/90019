# import tweepy
from couchdb import Server
import json
# import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from config import *
# from Locate import *
import sys
# from findHashtag import *


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
            print(id)
            # print(db[doc])
            doc = dict(db[id])
            # json.load()
            print(doc)

            # checkColunm(doc)
            # db.save(doc)

loopDB()
