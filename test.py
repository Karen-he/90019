from datetime import datetime
from couchdb import Server
import time

# dt = 'Thu Oct 04 13:03:01 +0000 2018'
# dtobj = datetime.strptime(dt, '%a %b %d %X %z %Y')
# print(dtobj.year==2018)
# print(dtobj.month)

#couchdb config
server = Server('http://admin:hekeren@127.0.0.1:5984/')
hashtag17db = server['hashtag2017']
hashtagdb = server['hashtag']

# get view results
pos17 = hashtag17db.view('sentiment&time/pos')
neg17 = hashtag17db.view('sentiment&time/neg')
neu17 = hashtag17db.view('sentiment&time/neu')
pos18 = hashtagdb.view('sentiment/positive')
neg18 = hashtagdb.view('sentiment/neg')
neu18 = hashtagdb.view('sentiment/neu')

postimeline = {'1017': 0, '1117': 0, '1217': 0, '0118': 0, '0218': 0, '0318': 0, '0418': 0, '0518': 0, '0618': 0,
               '0718': 0, '0818': 0, '0918': 0, '1018': 0, '1118': 0, '1218': 0}
negtimeline = {'1017': 0, '1117': 0, '1217': 0, '0118': 0, '0218': 0, '0318': 0, '0418': 0, '0518': 0, '0618': 0,
               '0718': 0, '0818': 0, '0918': 0, '1018': 0, '1118': 0, '1218': 0}
neutimeline = {'1017': 0, '1117': 0, '1217': 0, '0118': 0, '0218': 0, '0318': 0, '0418': 0, '0518': 0, '0618': 0,
               '0718': 0, '0818': 0, '0918': 0, '1018': 0, '1118': 0, '1218': 0}

start = time.time()
print("start collecting")
for item in pos17:
    doc = hashtag17db.get(item.id)
    if 'create_time' in doc.keys():
        month17 = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y').month
    else:
        month17 = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y').month
    month = str(month17).zfill(2) + '17'
    postimeline[month] = postimeline.get(month) + 1
for item in pos18:
    doc = hashtagdb.get(item.id)
    # print(item.id)
    if 'create_time' in doc.keys():
        dt = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y')
    else:
        dt = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y')
    month17 = dt.month
    # print(dt.year)
    # print(dt.month.__class__)
    if dt.year == 2018:
        month = str(month17).zfill(2) + '18'
    # if dt.year == 2017:
    #     month = str(month17).zfill(2) + '17'
    postimeline[month] = postimeline.get(month) + 1

for item in neg17:
    doc = hashtag17db.get(item.id)
    if 'create_time' in doc.keys():
        month17 = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y').month
    else:
        month17 = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y').month
    month = str(month17).zfill(2) + '17'
    negtimeline[month] = negtimeline.get(month) + 1
for item in neg18:
    doc = hashtagdb.get(item.id)
    if 'create_time' in doc.keys():
        dt = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y')
    else:
        dt = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y')
    if dt.year == 2018:
        month = str(month17).zfill(2) + '18'
    # if dt.year == 2017:
    #     month = str(month17).zfill(2) + '17'
    negtimeline[month] = negtimeline.get(month) + 1

for item in neu17:
    doc = hashtag17db.get(item.id)
    if 'create_time' in doc.keys():
        month17 = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y').month
    else:
        month17 = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y').month
    month = str(month17).zfill(2) + '17'
    neutimeline[month] = neutimeline.get(month) + 1
for item in neu18:
    doc = hashtagdb.get(item.id)
    if 'create_time' in doc.keys():
        dt = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y')
    else:
        dt = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y')
    if dt.year == 2018:
        month = str(month17).zfill(2) + '18'
    # if dt.year == 2017:
    #     month = str(month17).zfill(2) + '17'
    neutimeline[month] = neutimeline.get(month) + 1

print('finish collecting')
print(time.time()-start)