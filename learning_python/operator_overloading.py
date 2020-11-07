# Intercepting slices and indexes with __getitem__ method overloading
class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index): # Called for index or slice
        print('index' if isinstance(index,int) else 'slice: ', index)
        return self.data[index]

#inst=Indexer()
#print(inst[1:3])

# Intercepting iteration protocol with __getitem__ method overloading
# This is older way. Today interation protocol is based on __iter__ and __next__
class StepperIndex:
    def __init__(self):
        self.data='dejan'
    def __getitem__(self, i):
        return self.data[i]

#step=StepperIndex()
#for i in step: print(i)

# Iteration protocol (__iter__ method) - single pass iteration
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self): # Get iterator object on iter
        return self
    def __next__(self): # Return a square on each iteration
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

#sq=Squares(3,9)
#sq_iter=sq.__iter__()
#for i in sq_iter: print(i) # supports normal iteration
#if 16 in Squares(3,9).__iter__(): print('yes') # supports all other iteration contexts

# Iteration protocol - multiple pass iterators
class Squares_multi:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return Squares_multi_iter(self.value,self.stop)
class Squares_multi_iter:
    def __init__(self,value,stop):
        self.value=value
        self.stop=stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
#sq=Squares_multi(2,5)
#for i in sq: print(i)
#for i in sq: print('vtoro',i)

# And now for the big finale: multiple scan iterator withough new class
# We will use generator function in __iter__ method here !!!
class Squares_best:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        for i in range(self.value, self.stop + 1):
            yield i ** 2

sq=Squares_best(2,5)
for i in sq: print(i)
for i in sq: print(i) # no need for new iterator !!!