from collections import Counter

print('Number of occurences of letter e: {:-5}'.format(Counter('dejan stojcevski')['e']))

# initializing empty counter and populating it with sequence
c=Counter()
c.update('dejan stojcevski dejan')
print('Number of occurences of letter e: {:-5}'.format(c['e']))
c.update({'e':4}) # adding dict to increase number of occurences of letter 'e'
print('Number of occurences of letter e: {:-5}'.format(c['e']))

# Counter class dos not return KeyError if key is not defined! It returns 0!
print('Number of occurences of letter x: {:-5}'.format(c['x']))

# methods of Counter class:
# elements - list all elements known to the class
print(list(c.elements()))
# most_common
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))