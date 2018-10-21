from couchdb import Server

server = Server('http://admin:hekeren@127.0.0.1:5984/')
search = server['search']
stream = server['stream']
hashtagdb = server['hashtag']

# print('search')
for id in search:
    # print('search')
    doc = dict(search[id])
    id = doc['_id']
    if id in hashtagdb:
        print('--------already saved----------------')
    else:
        try:
            print(doc['_id'])
            hashtag = doc['hasHashtag']
            triggerHashtag = doc['triggerHashtag']
            if hashtag != 'none' or triggerHashtag != 'none':
                nodc = doc
                hashtagdb.save(nodc)
                print('********************************************')
        except Exception as e:
                print(e)
                continue
# print('stream')
for id in stream:
    # print('stream')
    doc = dict(search[id])
    id = doc['_id']
    if id in hashtagdb:
        print('--------already saved----------------')
    else:
        try:
            print(doc['_id'])
            hashtag = doc['hasHashtag']
            triggerHashtag = doc['triggerHashtag']
            if hashtag != 'none' or triggerHashtag != 'none':
                nodc = doc
                hashtagdb.save(nodc)
                print('********************************************')
        except Exception as e:
                print(e)
                continue
