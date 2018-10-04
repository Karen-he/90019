import re
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
