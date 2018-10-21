from couchdb import Server

server = Server('http://admin:hekeren@127.0.0.1:5984/')
search = server['search']
stream = server['stream']
hashtag = server['hashtag']

for id in search:
    doc = dict(search[id])
    id = doc['_id']
    if id in hashtag:
        print('--------already saved----------------')
    else:
        try:
            print(doc['_id'])
            hashtag = doc['hasHashtag']
            triggerHashtag = doc['triggerHashtag']
            if hashtag != 'none' or triggerHashtag != 'none':
                nodc = doc
                hashtag.save(nodc)
                print('********************************************')
        except Exception as e:
                print(e)
                continue

for id in stream:
    doc = dict(search[id])
    id = doc['_id']
    if id in hashtag:
        print('--------already saved----------------')
    else:
        try:
            print(doc['_id'])
            hashtag = doc['hasHashtag']
            triggerHashtag = doc['triggerHashtag']
            if hashtag != 'none' or triggerHashtag != 'none':
                nodc = doc
                hashtag.save(nodc)
                print('********************************************')
        except Exception as e:
                print(e)
                continue
