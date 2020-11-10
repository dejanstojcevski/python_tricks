##############################################################################
# formating/interpolation with % operator
# %[(keyname)][flags][width][.precision]typecode
variables = {'ime':'dejan','prezime':'stojcevski','god':46,'salary':467.3256}
print(
'''
Ime:        %(ime)-10s 
Prezime:    %(prezime)-10s
Godini:     %(god)-10d
Plata:      %(salary)010.2f EUR
''' % variables
)

##############################################################################
# formatting/interpolation with str.format method
# this method is basically a function and accepts all kinds of arguments: positional, keyword
# {fieldname component !conversionflag :formatspec}
# formatspec: [[fill]align][sign][#][0][width][,][.precision][typecode]

print (
'''
Ime:        {0}
Prezime:    {prezime}
Godini:     {god}
Plata:      {salary}
'''.format('dejan', prezime='stojcevski', god=46, salary=467.3256) # formating by position and keyword at same time
)

# another examples of format method
import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))

somelist='SPAM'
print('first={0[0]}, third={0[2]}'.format(somelist))

print( '{0.platform:<10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')) )
print( '{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159) )
print('My {kind:<8} runs {platform:>8}'.format(**dict(platform=sys.platform, kind='laptop')))

# format function new to the python 2.6 and 3.0
# serves to format single item
# has all the formatting syntax of the str.format method
print(format(1.2345, '<10.2f'),':')

#################################################################################
# formating/interpolation with string.Template
# class string.Template uses two methods for string formatting/interpolation:
# substitute, safe_substitute
from string import Template
t=Template('''
Ime:        $ime
Prezime:    ${prezime}
Godini:     $god
Plata:      $salary
''')
print(t.substitute(**variables))

#################################################################################
# since Python 3.6 we have new tool for variable interpolation in strings: f-strings
name='Dejan Stojcevski'; age=46
print(f'Hello {name.lower()}')
print(f'{name} is {age+2} years old')
def to_lowercase(input): return input.lower()
print( f"{to_lowercase('Dejan Stojcevski')} is funny.") # function return value interpolation into string
n=123;print(f'{n:=+8}') # f-strings accept all the str.format method syntax rules