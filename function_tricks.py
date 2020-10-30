# Function calling
# d={'end':'','sep':'*'*100+'\n'}
# print(*open(r'C:\Users\Admin001\Desktop\Python\sample1.csv'),**d)

# Transfering all lines of file in tuple - minimum coding
def to_tuple(*lines): yield lines
t = to_tuple(*open(r'C:\Users\Admin001\Desktop\Python\sample1.csv'))
print(*map(str.strip, *t), sep='\n')

# Same as before but with lambda
# lines=open(r'C:\Users\Admin001\Desktop\Python\sample1.csv')
# t=lambda *lines: lines
