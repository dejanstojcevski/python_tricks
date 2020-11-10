import re
''' 
This module shows basic regular expressions in python with re module.
Explains basic methods and classes used in re matching.
'''

text = 'Does this text match this the pattern?'

# normal re matching
match = re.search(r'\bthis', text)  # returns new instance of class re.Match. re Match is subclass of re.Pattern!
if match:
    s = match.start()
    e = match.end()
    print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
            match.re.pattern,       # from the class re.Match.re we can access all attributes of the class re.Pattern
            match.string,
            s,
            e,
            text[s:e])
    )
else:
    print('Match not forund')

# precompiling regular expression patterns for efficiency
regexp=re.compile(r'\ADoes')        # make new instance of class type re.Pattern
match=regexp.search(text)           # make new instance of class type re.Match
if match:
    s = match.start()
    e = match.end()
    print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
            regexp.pattern,         # we directly call method pattern from the class type re.Pattern
            match.string,
            s,
            e,
            text[s:e])
    )
else:
    print('Match not forund')

# find all occurences of the pattern - re.findall and re.finditer
regexp=re.compile(r'\bthis\b')      # make new instance of class re.Pattern
match=regexp.findall(text)          # makes new LIST of all occurrences of pattern in string
print(match)
match=regexp.finditer(text)         # makes new iterator with all occurrences of the pattern
for item in match: print(item)

# find pattern only at the start of the text - match method of re.Pattern class
regexp=re.compile('this')
match=regexp.match(text)            # makes new iterator
print(match)
regexp=re.compile('Does')
match=regexp.match(text)
print(match)

# find pattern as the whole text - re.Pattern.fullmatch
regexp=re.compile('Does')
match=regexp.fullmatch(text)
print(match)