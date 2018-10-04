import re
hashtags = []
with open('Harvester/hashtags.txt') as inputfile:
    for i in inputfile:
        hashtags.append(i.replace('\n', ''))
        print(i.replace('\n', ''))
print(hashtags)

tweet = 'metoo'
wordlist = tweet.split(' ')
# count = 0
hash = []
for word in wordlist:
    word = word.lower()
    word = re.sub('[^0-9a-zA-Z]+', '', word)
    if word in hashtags:
        # count = count + 1
        hash.append(word)
if len(hash) > 0:
    print(hash)
else:
    print('none')
