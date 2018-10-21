from couchdb import Server
import json

server = Server('http://admin:hekeren@127.0.0.1:5984/')
search = server['search']
stream = server['stream']
hashtagdb = server['hashtag']

i = 0
print('search')
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
                # hashtagdb.save(nodc)
                hashtagdb[i]=nodc
                i=i+1
                print(i)
                print('********************************************')
        except Exception as e:
                print(e)
                continue
print('stream')
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
                # hashtagdb.save(nodc)
                hashtagdb[i] = nodc
                i = i + 1
                print(i)
                print('********************************************')
        except Exception as e:
                print(e)
                continue
