import os,time

# first group of functions in this module just parses strings which represent paths in the file system
# they are based on os module attributes: os.sep, os.extsep, os.pardir, os.curdir
# these functions does not have interaction with the operating system but depends solely on the os attributes mentioned above

PATHS = ['/one/two/three','/one/two/three/','/','.','']
for path in PATHS:
    print('{!r:<17} : {}'.format(path, os.path.split(path)))    # split() function splits paths and return tuple of dir and file
    print('{!r:<17} : {}'.format(path, os.path.basename(path))) # returns just the file name
    print('{!r:<17} : {}'.format(path, os.path.dirname(path)))  # returns just the directory name

print('=' * 80)

paths = ['/one/two/three/four','/one/two/threefold','/one/two/three/']
for path in paths:
    print('PATH:', path)
print()
print('COMMONPATH:', os.path.commonpath(paths))                 # returns common path of the paths in sequence
print()

print('=' * 40,' Joining Strings in a Path ' , '=' * 40)
PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]
for parts in PATHS:
    print('{!r:<29} : {}'.format(parts, os.path.join(*parts)))   # build a path from a series of strings

os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
for items in os.listdir('learning_python'):
    print(os.path.join(os.path.abspath('.'),'learning_python',items)) # os.path.abspath gets variable stored in os.curdir

# second group of functions actually has interface towards operating system and fetches file access/modification/... times and
# tests for existence and type

print('=' * 40,' Get File Attributes ' , '=' * 40)
print('File :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Creation time:', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
print('=' * 80)

os.chdir('standard_library_by_example/file_system')
print('=' * 40,' Test for existence and type ' , '=' * 40)
for file in os.listdir():
    print('File        : {!r}'.format(file))
    print('Absolute    :',os.path.isabs(file))
    print('Is File?    :',os.path.isfile(file))
    print('Is Dir?     :',os.path.isdir(file))
    print('Is Link?    :',os.path.islink(file))
    print('Mountpoint? :',os.path.ismount(file))
    print('Exists?     :',os.path.exists(file))
    print('Link Exists?:',os.path.lexists(file))