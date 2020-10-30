i=0
for last_line in open('test.py'): i+=1
print(i,':',last_line,sep='')

# another way but not as efficient
(*a,last_line)=open('test.py')
print(len(a)+1,':',last_line,sep='')

# same as previous
file=list(open('test.py'))
print(len(file),':',file[-1],sep='')