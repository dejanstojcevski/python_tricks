import collections

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])
d.remove('c')
print('remove(c):', d)

# populating deque
d.extend('xyz')
d.append('q')
print('Extended and appended deque: {}'.format(d))
d.extendleft('nm')
d.appendleft('r')
print('Extended and appended deque from left side: {}'.format(d))

# removing elements from either side of the queue
d.popleft()
d.pop()
print('Removed first and last elements from the queue: {}'.format(d))

# rotating elements of the queue
d.rotate(5)
print('rotated queue {}:'.format(d))
d.rotate(-5)
print('rotated queue left side {}:'.format(d))

# constraining dequeue size
# this is efficient method of finding last n lines of file since we are using iterator as a file descriptor
# and deque of limited size
d=collections.deque(maxlen=3) # maximum 3 elements in this queue
for line in open(r'C:\Users\Admin001\Desktop\Python\sample1.csv'): d.append(line.strip())
print(*d,sep='\n')