# use the datetime.datetime class to store dates and times combined in one instance
import datetime
import time

# creating datetime instances
dt=datetime.datetime(2019,5,23,23,45,34,0) # with class constructor
dt=datetime.datetime.strptime('2020-3-23 10:54:34','%Y-%m-%d %H:%M:%S') # from string
dt=datetime.datetime.now() # with class method
dt=datetime.datetime.utcnow() # with class method
dt=datetime.datetime.today() # with class method
dt=datetime.datetime.fromtimestamp(time.time()) # with class method

# once we have a datetime as an instance, we can use instance methods for various purposes
# fetching various attributes from the instance
FIELDS = [
    'year', 'month', 'day',
    'hour', 'minute', 'second',
    'microsecond'
]
for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(dt, attr)))

# printing the value of the datetime.datetime instance with different formats
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
print(dt.timestamp()) # from datetime object to timestamp

# comparing values
if dt>datetime.datetime.strptime('2003-3-23 10:54:34','%Y-%m-%d %H:%M:%S'): print(True)

# doing aritmetic with datetime.timedelta class
print(dt-datetime.timedelta(days=1,hours=4,minutes=23))
print(datetime.datetime.today()-datetime.datetime.strptime('2020-03-23','%Y-%m-%d')) # result from the - operation is timedelta object