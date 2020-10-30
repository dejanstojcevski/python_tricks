l=()
for last_line in open(r'C:\Users\Admin001\Desktop\Python\sample1.csv'):pass
for line in open(r'C:\Users\Admin001\Desktop\Python\sample.csv'): l += line,
x=l.index(last_line)+1 if last_line in l else 0
for item in l[x:]: print(item,end='')
