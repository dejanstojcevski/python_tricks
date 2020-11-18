import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b) # new ChainMap instance

print('Individual Values:')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))

# What happens if we delete a['c']?
del a['c']
print('Individual Values:')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
# ChainMap searches for the values in the dirs listed in constructor left to right