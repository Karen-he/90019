import time
from datetime import datetime
import threading
from couchdb import Server
from flask import Flask, render_template
import requests

# print('before create app')
app = Flask(__name__)
# Bootstrap(app)

# couchdb config
server = Server('http://admin:hekeren@127.0.0.1:5984/')
hashtag17db = server['hashtag2017']
hashtagdb = server['hashtag']
search = server['search']
stream = server['stream']
twitter2017 = server['twitter2017']

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


@app.before_first_request
def activate_job():
    # global total
    # total = search.view('_all_docs').total_rows + stream.view('_all_docs').total_rows + twitter2017.view(
    #     '_all_docs').total_rows
    def run_job():
        while True:
            # print('run background task')
            time.sleep(5)
            get_timeline_data()
    thread = threading.Thread(target=run_job)
    thread.start()


#background function
def background():
    while True:
        time.sleep(5)
        get_timeline_data()


def get_timeline_data():
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
        # if dt.year == 2018:
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
        # if dt.year == 2018:
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
        # if dt.year == 2018:
        month = str(month17).zfill(2) + '18'
        # if dt.year == 2017:
        #     month = str(month17).zfill(2) + '17'
        neutimeline[month] = neutimeline.get(month) + 1

    print('finish collecting')


# print('before background function')

@app.route("/")
@app.route("/home")
def home():
    summary = {}
    total = len(hashtagdb) + len(hashtag17db)
    pos = pos17.total_rows + pos18.total_rows
    neg = neg17.total_rows + neg18.total_rows
    neu = neu17.total_rows + neu18.total_rows
    summary['total'] = total
    summary['pos'] = pos
    summary['neg'] = neg
    summary['neu'] = neu
    # total = search.view('_all_docs').total_rows+stream.view('_all_docs').total_rows+twitter2017.view('_all_docs').total_rows
    total = 1892972 + 101191 + 4106112
    return render_template('home.html', summary=summary, total=total)


@app.route("/summary")
def summary():
    summary = {}
    total = len(hashtagdb) + len(hashtag17db)
    pos = pos17.total_rows + pos18.total_rows
    neg = neg17.total_rows + neg18.total_rows
    neu = neu17.total_rows + neu18.total_rows
    # summary['total'] = total
    summary['pos'] = pos
    summary['neg'] = neg
    summary['neu'] = neu
    return render_template('summary.html', title='summary', summary=summary)


@app.route("/timeline")
def timeline():
    timeline = {'neg': negtimeline, 'pos': postimeline, 'neu': neutimeline}
    return render_template('timeline.html', title='Timeline', timeline=timeline)


def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            # print('In start loop')
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    # print('Server started, quiting start_loop')
                    not_started = False
                # print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    # print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()


start_runner()


# run py file in debug mode
if __name__ == '__main__':
    start_runner()
    # print('in main before run')
    app.run(debug=True)
