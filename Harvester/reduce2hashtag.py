from couchdb import Server
# import json

server = Server('http://admin:hekeren@127.0.0.1:5984/')
# search = server['search']
# stream = server['stream']
t17 = server['twitter2017']
hashtagdb = server['hashtag2017']

i = 0
print('twitter2017')
for id in t17:
    # print('search')
    doc = dict(t17.get(id))
    id = doc['_id']
    if id in hashtagdb:
        print('--------already saved----------------')
    else:
        try:
            # print(doc['_id'])
            ndoc = doc
            ndoc.pop('_rev')
            hashtag = doc['hasHashtag']
            triggerHashtag = doc['triggerHashtag']
            if hashtag != 'none' or triggerHashtag != 'none':
                # ndoc = doc
                # hashtagdb.copy(id,i)
                hashtagdb.save(ndoc)
                # hashtagdb[id]=nodc
                i=i+1
                print(doc['_id'])
                print(i)
                print('********************************************')
        except Exception as e:
                print(e)
                continue

# print('stream')
# for id in stream:
#     # print('stream')
#     doc = dict(stream.get(id))
#     id = doc['_id']
#     if id in hashtagdb:
#         print('--------already saved----------------')
#     else:
#         try:
#             # print(doc['_id'])
#             ndoc = doc
#             ndoc.pop('_rev')
#             hashtag = doc['hasHashtag']
#             triggerHashtag = doc['triggerHashtag']
#             if hashtag != 'none' or triggerHashtag != 'none':
#                 # nodc = doc
#                 # hashtagdb.copy(id, i)
#                 hashtagdb.save(ndoc)
#                 # hashtagdb[id] = nodc
#                 i = i + 1
#                 print(doc['_id'])
#                 print(i)
#                 print('********************************************')
#         except Exception as e:
#                 print(e)
#                 continue
