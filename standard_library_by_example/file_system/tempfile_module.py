# tempfile module holds functions which operate on temp files/directories securely
import tempfile, pathlib

with tempfile.TemporaryFile() as temp:      # context manager automatically deletes temp file on file close
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))
    temp.write(b'dejan stojcevski')         # writing to file in binary format
    temp.write(b'another line')
    temp.seek(0)
    print(temp.readlines())                 # reading from file

with tempfile.TemporaryFile('w+t') as temp: # opening temp file in text mode instead of binary mode (which is default)
    print('dejan stojcevski',file=temp)
    temp.seek(0)
    print(temp.readlines())

# Creating temporary directories instead of files
with tempfile.TemporaryDirectory() as directory_name:
    the_dir = pathlib.Path(directory_name)
    print(the_dir)
    a_file = the_dir / 'a_file.txt'
    a_file.write_text('This file is deleted.')
    print(a_file.read_text())
