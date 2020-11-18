import bisect # inserts elements in list as the list is maintained sorted

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

l = []

for i in values:
    position = bisect.bisect(l, i) # returns the position of the elements in the list
    bisect.insort(l, i)            # actually inserts the element into the list
    print('{:>3} {:>3}'.format(i, position), l)