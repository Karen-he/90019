import re
import json

hashtags = []
with open('hashtags.txt') as inputfile:
    for i in inputfile:
        hashtags.append(i.replace('\n', ''))
        # print(i)
print(hashtags)

def hasHashtag(tweet):
    wordlist = tweet.split(' ')
    # count = 0
    hash = []
    for word in wordlist:
        word = word.lower()
        word = re.sub('[^0-9a-zA-Z]+', '', word)
        if word in hashtags:
            # count = count + 1
            hash.append(word)
    # print(hash)
    if len(hash) > 0:
        return hash
    else:
        return 'none'

def searchHashtag(tags):
    hash = []
    originalTags = []
    for tag in tags:
        hashtag = tag['text']
        hashtag = hashtag.lower()
        hashtag = re.sub('[^0-9a-zA-Z]+', '', hashtag)
        originalTags.append(hashtag)
        # print(hashtag)
        if hashtag in hashtags:
            hash.append(hashtag)
    # print(hash)
    # print(originalTags)
    output = json.dumps({'trigger': hash, 'original': originalTags})
    print(output)
    if len(hash) > 0:
        return output
    else:
        return 'none'
