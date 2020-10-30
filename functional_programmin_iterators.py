# Example of an efficient shell like pipe with
# iterators/generators

# f=filter(lambda x: bool('Telephone' in x),open(r'C:\Users\Admin001\Desktop\Python\sample.csv'))
# g=(x.replace('"','') for x in f)   # with generator we are constructing new iterator over existing iterator f
# for x in g: print(x,end='')        # only one line in memory at every single time
# print(len(list(g)))                # list(g) is just a result subset of an opened file

# Another example
# Efficiently replace " with empty string and
# discard empty lines
#g = (x.replace('"', '') for x in open(r'C:\Users\Admin001\Desktop\Python\sample1.csv'))
#for line in filter(lambda x: bool(x.strip()), g): print(line,end='')

# Another example of shell pipe like command
# this time using functional tools
m=map(lambda x: x.strip().replace('"',''), filter(lambda x: 'Telephone' in x, open(r'C:\Users\Admin001\Desktop\Python\sample.csv')))
m2=map(lambda x: x.replace(',','|'),m)
print(*m2,sep='\n',end='')