# splitting with regular expressions
import re

text = '''Paragraph one
on two lines.

Paragraph two.

Paragraph three.'''

for num, para in enumerate(re.split(r'\n{2,}', text)): # re.split returns list with elements
    print(num, repr(para))