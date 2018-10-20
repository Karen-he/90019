import CouchDB
import sys
import os

if __name__ == '__main__':
    try:
        server = CouchDB.Server('http://localhost:5984/')
    except Exception, e:
        sys.exit(1)

    DbName = "test"

    try:
        DB = server[DbName]
    except Exception, e:
        sys.exit(1)

    changeRS = DB.changes(feed='continuous', heartbeat='50000', include_docs=True)
    counter = 0
    for each in changeRS:
        counter += 1
    if (counter > 2000):
        len(DB.view('TestDesignDoc/testView1'))
    print
    "update view"
    counter = 0