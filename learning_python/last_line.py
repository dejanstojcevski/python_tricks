i=0
for last_line in open('two_files.py'): i+=1
print(i,':',last_line,sep='')

# another way but not as efficient
(*a,last_line)=open('two_files.py')
print(len(a)+1,':',last_line,sep='')

# same as previous
file=list(open('two_files.py'))
print(len(file),':',file[-1],sep='')

# efficiently get last n lines from a file!
import collections
d=collections.deque(maxlen=3) # maximum 3 elements in this queue
for line in open(r'C:\Users\Admin001\Desktop\Python\sample1.csv'): d.append(line.strip())
print(*d,sep='\n')