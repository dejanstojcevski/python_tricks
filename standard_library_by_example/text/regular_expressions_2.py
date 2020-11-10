# groups in regular expressions
import re

text = 'This is some text -- with punctuation.'

patterns = [
    (r'^(\w+)',             'word at start of string'),
    (r'(\w+)\S*$',          'word at end, with optional punctuation'),
    (r'(\bt\w+)\W+(\w+)',   'word starting with t, another word'),
    (r'(\w+t)\b',           'word ending with t')
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc),end='')
    print('Found group:', match.groups(),end='') # returns the groups (in a tuple) as defined in pattern
    print(' First groupped item is: ',match.groups()[0])
    print()

# using named groups in patterns
patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b'
]
for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print(match.groupdict(),end='') # returns dict with group name (key) and match (value) for that group
    print()