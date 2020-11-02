'''
try:
    1/0
except Exception as X:
    print('Following exception occured: ',X)
    a=X # python 3 does not retain exception beyond except clause so we must save exception in var for outside use
print(a)
'''
# assert command is for catching constraints not errors!!!
def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2
print(f(4))