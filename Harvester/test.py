from datetime import datetime

dt = 'Thu Oct 04 13:03:01 +0000 2018'
dtobj = datetime.strptime(dt, '%a %b %d %X %z %Y')
print(dtobj.year)
print(dtobj.month)
