s = 'ABCDBCA'

translation = s.maketrans({ord('A'): 'a', ord('B'): ord('b')})  # single argument as dict
print(s.translate(translation))

translation = s.maketrans('A','a') # two arguments - must be of equal size!
print(s.translate(translation))

print(s.translate({ord('A'):ord('a')})) # direct translation with dict as argument. dict values must be ord numbers!