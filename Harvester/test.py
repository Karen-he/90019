from datetime import datetime
from couchdb import Server

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

# total = len(hashtagdb) + len(hashtag17db)
# print(total)
# re = hashtag17db.view('sentiment&time/pos').update_seq
# print(re)
# print(hashtag17db.view('sentiment&time/pos').total_rows)

# pos17 = hashtag17db.view('sentiment&time/pos')
# for item in pos17:
#     print(item.id)
#     doc = hashtag17db.get(item.id)
#     if 'create_time' in doc.keys():
#         month17 = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y').month
#     else:
#         month17 = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y').month
#     print(month17)

import threading
import time


# def sleeper(i):
#     print("thread %d sleeps for 5 seconds" % i)
#     time.sleep(5)
#     print("thread %d woke up" % i)
#
#
# for i in range(10):
#     t = Thread(target=sleeper, args=(i,))
#     t.start()
#
# for i in range(10):
#     print('in main')


def get_timeline_data(view17, view18, g):
    MAX17 = view17.total_rows
    MAX18 = view18.total_rows
    print(threading.current_thread().name)
    print("start collecting")
    print(g)
    while g <= MAX17:
        for item in view17.rows[g:g+10]:
            print(item.id)
            doc = hashtag17db.get(item.id)
            if 'create_time' in doc.keys():
                month17 = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y').month
            else:
                month17 = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y').month
            month = str(month17).zfill(2) + '17'
            postimeline[month] = postimeline.get(month) + 1
    while g <= MAX18:
        for item in view18.rows[g:g+10]:
            doc = hashtagdb.get(item.id)
            print(item.id)
            if 'create_time' in doc.keys():
                dt = datetime.strptime(doc['create_time'], '%a %b %d %X %z %Y')
            else:
                dt = datetime.strptime(doc['created_at'], '%a %b %d %X %z %Y')
            month17 = dt.month
            # print(dt.year)
            # print(dt.month.__class__)
            if dt.year == 2018:
                month = str(month17).zfill(2) + '18'
            if dt.year == 2017:
                month = str(month17).zfill(2) + '17'
            postimeline[month] = postimeline.get(month) + 1
    print('finish collecting')


def background():
    i = 0
    while True:
        # time.sleep(10)
        for (view17, view18) in [(pos17, pos18), (neg17, neg18), (neu17, neu18)]:
            global v
            v = 0
            print(v)
            print(i)
            t = threading.Thread(target=get_timeline_data(view17, view18, v), name='background')
            t.daemon = True
            # print(threading.current_thread().name)
            t.start()
            v = v + 10
            i = i + 1
            time.sleep(0.1)



# mainthread = Thread(target='__main__')
# mainthread.run()
print(threading.current_thread().name)
i = 0
for (view17, view18) in [(pos17, pos18), (neg17, neg18), (neu17, neu18)]:
    global v
    v = 0
    print(v)
    print(i)
    t = threading.Thread(target=get_timeline_data(view17, view18, v), name='background')
    t.daemon = True
    # print(threading.current_thread().name)
    t.start()
    v = v + 10
    i = i + 1
    time.sleep(0.1)
# backthread = threading.Thread(target=background()).start()
# print(threading.current_thread().name)
# backthread.start()
# backthread.daemon = True


for x in range(10):
    print('main-'+str(x))

