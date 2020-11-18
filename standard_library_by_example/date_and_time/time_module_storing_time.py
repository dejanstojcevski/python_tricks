# time module works with times in two distinct ways:
# 1. it stores time in seconds from the epoch
# 2. it stores time in time.struct_time object (class) - this is the only class in time module
# there are several methods to convert between two store types
# advantage of struct_time is accessing the various parts of time (hour, minute, ..) by key

import time

# making/populating struct_time object
# converting from seconds to struct_time
strtime=time.gmtime(time.time())
print(strtime)
strtime=time.localtime(time.time())
print(strtime)
# constructing struct_time from sequence (__init__ method of time.struct_time class)
strtime=time.struct_time((2020,3,15,14,23,45,0,0,0))
print(strtime)
# converting from string to time.struct_time type
strtime=time.strptime('2020-03-12 14:34:00','%Y-%m-%d %H:%M:%S')
print(strtime)

# converting from struct_time to seconds
print(time.mktime(strtime))
# converting from struct_time to string (or pretty printing the struct_time instance value)
print(time.strftime('%Y-%m-%d',strtime))
# converting from struct_time to string in time.ctime() format
print(time.asctime(strtime))
