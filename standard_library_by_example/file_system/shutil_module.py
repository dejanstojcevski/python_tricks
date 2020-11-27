# shutil module help us in copying / moving files/directories
# also has several other tools

import shutil,tarfile,os

######## File system space
print('='*40,' File System Space ','='*40)
total_b, used_b, free_b = shutil.disk_usage('.')
gib = 2 ** 30  # GiB == gibibyte
gb = 10 ** 9   # GB  == gigabyte
print('Total: {:6.2f} GB  {:6.2f} GiB'.format(total_b / gb, total_b / gib))
print('Used : {:6.2f} GB  {:6.2f} GiB'.format(used_b / gb, used_b / gib))
print('Free : {:6.2f} GB  {:6.2f} GiB'.format(free_b / gb, free_b / gib))
'''
######## Managing Archives
print('='*40,' Archives ','='*40)
for format, description in shutil.get_archive_formats():
    print('{:<5}: {}'.format(format, description))

print('Creating archive:')
shutil.make_archive('file_system','gztar',root_dir='..',base_dir='file_system')
print('Archve contents:')
with tarfile.open('file_system.tar.gz', 'r') as t:
    for n in t.getnames():
        print(n)

# which archive types shutil can manage to open
print('shutil managed archive formats:')
for format, exts, description in shutil.get_unpack_formats():
    print('{:<5}: {}, names ending in {}'.format(format, description, exts))

# extracting archive
os.mkdir('extracted_archive')
shutil.unpack_archive('file_system.tar.gz','extracted_archive')
'''
######### Copy/Move files
shutil.copyfile('shutil_module.py','shutil_module2.py')     # copy file to file
os.unlink('shutil_module2.py')
shutil.copy('shutil_module.py','newdir')                    # copy file to file or directory (if second argument is a dir) along with file permissions
shutil.copy2('shutil_modue.py','newdir')                    # copy file to file or dir along with file attributes (ctime, mtime, atime)
shutil.move('shutil_module.py','shutil_module2.py')         # moving file (renaming)
