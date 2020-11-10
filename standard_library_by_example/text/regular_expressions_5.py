import re
'''
This module shows how to substitute strings with regular expressions
'''

bold = re.compile(r'\*{2}(.*?)\*{2}')
text = r'Make this **bold**. This **too**.'
print('Text:', text)
print('Bold:', bold.sub(r'<b>\1</b>', text)) # use sub method from re.Match class to substitute

# use named groups instead of \1
bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')
text = 'Make this **bold**. This **too**.'
print('Text:', text)
print('Bold:', bold.sub(r'<b>\g<bold_text></b>', text)) # here we are using \g to insert named group name

# substitute only first occurence
bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')
text = 'Make this **bold**. This **too**.'
print('Text:', text)
print('Bold:', bold.sub(r'<b>\g<bold_text></b>', text, count=1)) # count is for how many occurencies will be substituted