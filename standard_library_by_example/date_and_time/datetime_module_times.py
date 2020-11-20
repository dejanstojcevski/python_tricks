# datetime module stores information about dates and times in module classes
# it differs from time module which works with floats for representing seconds since epoch

import datetime

# times are represented with datetime.time class
t = datetime.time(1, 2, 3,89)
print(t)
print('hour :', t.hour)
print('minute :', t.minute)
print('second :', t.second)
print('microsecond:', t.microsecond)
print('tzinfo :', t.tzinfo)

t = datetime.time(minute=43,hour=12,second=56,microsecond=32) # kwarg parameters
print(t)

# min, max,resolution are datetime.time class variable attributes
print('Earliest :', datetime.time.min)
print('Latest :', datetime.time.max)
print('Resolution:', datetime.time.resolution)