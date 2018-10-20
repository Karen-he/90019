from couchdb import Server
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import *
from Locate import *
from findHashtag import *
import json
import ijson

DB_Name = ['twitter']
server = Server('http://admin:hekeren@127.0.0.1:5984/')
db = server['twitter']

# instance of do sentiment analysis
analyzer = SentimentIntensityAnalyzer()

twitterFile = open('/mnt/tmp/twitter.json')

rows = ijson.items(twitterFile, 'rows.item')

# with open('/mnt/tmp/twitter.json') as twitterFile:
#     twitterJson = json.load(twitterFile)
#     rows = twitterJson['rows']
for row in rows:
    doc = dict(row['doc'])
    print(doc['_id'])
    ndoc = doc
    text = doc['text']
    coordinates = doc['coordinates']
    sentiment = analyzer.polarity_scores(text)
    suburb = give_suburb(coordinates)
    hashtag = hasHashtag(text)
    tags = doc['entities']['hashtags']
    triggerHashtag = searchHashtag(tags)
    ndoc['hasHashtag'] = hashtag
    ndoc['triggerHashtag'] = triggerHashtag
    ndoc['sentiment'] = sentiment
    ndoc['suburb'] = suburb
    db.save(ndoc)
    print('********************************************')




