# search options to regular expressions
import re

# ignore case
text = 'This is some text -- with punctuation.'

pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE) # this is option for ignoring letter case
print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Case-sensitive:')
for match in with_case.findall(text):
    print(' {!r}'.format(match))
print('Case-insensitive:')
for match in without_case.findall(text):
    print(' {!r}'.format(match))

# multiline mode
text = '''This is some text -- with punctuation.
A second line.'''

pattern = r'(^\w+)|(\w+\S*$)'

single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE) # multiline mode

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Single Line :')
for match in single_line.findall(text): print(' {!r}'.format(match))
print('Multline :')
for match in multiline.findall(text):   print(' {!r}'.format(match))
print('_'*80)

# dor matches new lines as well mode
print('_'*80)
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL) # dot matches new lines as well
print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('No newlines :')
for match in no_newlines.findall(text):print(' {!r}'.format(match))
print('Dotall :')
for match in dotall.findall(text):print(' {!r}'.format(match))
print('_'*80)

# enabling verbose mode in re patterns with VERBOSE flag
print('_'*80)
address = re.compile(
    '''
    [\w\d.+-]+ # Username
    @
    ([\w\d.]+\.)+ # Domain name
    (com|org|edu) 
    ''', re.VERBOSE )

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo'
]
for candidate in candidates:
    match = address.search(candidate)
    print('{:<40} {}'.format(candidate, 'Matches' if match else 'No match'),
)
print('_' * 80)

# regular expression note: all above flags can be aded to the re pattern as well with (?i) notation
# i=x (verbose), s (dot all), m (multiline), i (ignore case)