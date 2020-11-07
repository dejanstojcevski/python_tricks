"""
def first_function() : print('this is a first function')
def second_function(): print('this is a second function')
def default_function():print('this is a default function')

branch = {
    '1':'first_function()',
    '2':'second_function()'
         }

choice=input('Input choice: ')
a=branch.get(choice,'default_function()')
eval(a)
"""
# Another way (with 'default' choice)

key=input('Input capitalize or lowerize: ')
print(
    {'capitalize': (lambda x : x.upper()),
     'lowerize':   (lambda x : x.lower())
    }.get(key,lambda x: x)('dEjAn')
)