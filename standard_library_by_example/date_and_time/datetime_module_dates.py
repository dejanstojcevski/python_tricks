# datetime module stores information about dates and times in module classes
# it differs from time module which works with floats for representing seconds since epoch

import datetime
import time
import textwrap

# dates are represented with datetime.date class
# creating date instance:
dt=datetime.date(2008,12,15)                # creating using the date class constructor with arguments year,month,day
dt=datetime.date.today()                    # creating with the class method today() in the date class
dt=datetime.date.fromtimestamp(time.time()) # creating from the seconds since the epoch
dt=datetime.date.fromisoformat('2020-03-23')# creating from ISO formatted string 'YYYY-MM-DD'
print(dt)

# now that we have a date as a instance of date class,
# we can invoke several instance methods on the instance
print(dt.timetuple())                       # converting datetime.date instance into struct_time instance
print(
    textwrap.dedent(
    '''
    Min date: {}
    Max date: {}
    Res date: {}
    '''.format(dt.min, dt.max, dt.resolution)
    )
)
print(dt.replace(year=2018,month=4))        # replacing year or month or day in date instance making new object - date instances are imutable!

# formatting output
print(dt.isoformat())
print(dt.ctime())
print(dt.strftime('%d-%m-%Y'))
print(dt.toordinal())                       # days passed since epoch