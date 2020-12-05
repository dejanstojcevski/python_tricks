from itertools import count     # count is a infinite version of builtin range function

enumerate = lambda x, start=0: zip(count(start),x)  # overloading enumerate function with count(start,step) - there is no end parameter like in range!
print(list(enumerate('dejanstojcevski',3)))
print(list(zip(count(3),'dejanstojcevski')))        # same as previous
print(list(zip(count(5,2),'dejanstojcevski')))      # with step as additional parameter for count

from itertools import cycle     # cycle repeats some iterable indefinetly

m3= (i == 0 for i in cycle(range(3)))
m5= (i == 0 for i in cycle(range(5)))
multipliers = zip(range(100), m3, m5)                # finding common multipliers of 3 and 5
print(list(x for (x,*rest) in multipliers if all(rest)))

from itertools import accumulate # serially apply function on iterable. default function is sum

print(list(accumulate('dejan')))
print(list(accumulate([1,2,3,4,5,6,7,8],lambda x,y: y-x)))