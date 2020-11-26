import glob
import os
import fnmatch

for items in glob.glob('..\..\learning_python\*'):
    print(os.path.basename(items))

# change working directory two levels up
os.chdir(os.path.join(os.getcwd(),'..\..'))

# find files of certain pattern from the top level dir all the way down
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(os.path.join(os.getcwd(),root), basename)
                yield filename

for filename in find_files('.', '*module*'):
    print('Found Python module:', filename)

# fnmatch module is a base for a glob module
# fnmatch module have functions that work on single filename
for name in os.listdir():
    print('Filename: {:<25} {}'.format(name, fnmatch.fnmatch(name, '*lear*')))

# searching for specific files from a list of files
print(fnmatch.filter(os.listdir('learning_python'),'*.py')) # using filter function in fnmatch module

# use fnmatchcase function for case sensitive matching
pattern = '*PYTHON*'
print('Pattern :', pattern)
print()
files = os.listdir('.')
for name in files:
    print('Filename: {:<30} {}'.format(name, fnmatch.fnmatchcase(name, pattern)))

# glob.iglob returns iterator which can be used to iterate over files one by one
print('=' * 40 ,' glob Iterator ','=' * 40)
it=glob.iglob('learning_python/*')
for file in it:
    # do whatever you want with the files one by one
    print(os.path.abspath(file))