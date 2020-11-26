# shutil module help us in copying / moving files/directories
# also has several other tools

import shutil,os

source = os.listdir("/tmp/")
destination = "/tmp/newfolder/"
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files, destination) # copy file to dest directory. permissions of the file are preserved
        shutil.copy2(files,destination) # copy file to dest directory. permissions + access and modification times are preserved

shutil.copyfile('/path/to/file', '/path/to/other/phile') # copy file to file (possibly renaming the file)

############
# recursively move a file or directory (src) to another location (dst).
# if the destination is a directory or a symlink to a directory, then src is moved inside that directory.
# the destination directory must not already exist.
# this would move files ending with .txt to the destination path

source = os.listdir("/tmp/")
destination = "/tmp/newfolder/"
for files in source:
    if files.endswith(".txt"):
        shutil.move(files, destination) # move file to dir

####################
# recursively copy the entire directory tree rooted at src to dest.
# dest must not already exist.
# errors are reported to standard output

SOURCE = "samples"
BACKUP = "samples-bak"
shutil.copytree(SOURCE, BACKUP)

####################
# recursively delete a directory tree.
# This removes the directory 'three' and anything beneath it in the filesystem.

shutil.rmtree('one/two/three')