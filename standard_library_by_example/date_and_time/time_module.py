import time
import random

# time.time() uses system clock. this clock can be manually changed by user and thus time.time() will be changed
print('Current time since the epoch in seconds representation: ', time.time())
print('Current time since the epoch in string representation : ', time.ctime())
print('Time after 15 seconds from now string representation  : ', time.ctime(time.time()+15))

print()
# time.monotonic() uses increment of seconds always onwards. it does not depend on system clock
# start time of monotonic clock is not defined so it is only useful for measuring time differences
start = time.monotonic()
time.sleep(random.random())
end = time.monotonic()
print('start : {:>9.2f}'.format(start))
print('end   : {:>9.2f}'.format(end))
print('span  : {:>9.2f}'.format(end - start))

print()
# time.process_time() is process time measuring clock
# like the time.monotonic() it only progresses forward
# time.process_time() unlike monotonic has defined start time - the epoch
# it always starts when the python process starts
# the processor clock is not ticking if the python program is not doing anything!!!
template = '{} - {:0.2f} - {:0.2f}'
print(template.format(time.ctime(), time.time(), time.process_time()))
for i in range(3, 0, -1):
    print('Sleeping', i)
    time.sleep(i)
    print(template.format(time.ctime(), time.time(), time.process_time()))

print()
# time.perf_counter() is high resolution monotonic clock
# it is used for measuring performance
# start time is not defined so it is used for measuring time differences not absolute times
def is_prime(number):
   for i in range(2, number):
      if number % i == 0:
         return False
         return True

start_time = time.perf_counter()
map(is_prime,range(100))
end_time = time.perf_counter()
print(end_time - start_time)