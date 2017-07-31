import time
import datetime

myDate = "2017-07-30 22:30:0,000"
timestamp = time.mktime(datetime.datetime.strptime(myDate, "%Y-%m-%d %H:%M:%S,%f").timetuple())
print timestamp
