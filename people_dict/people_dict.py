import shelve

# read all records from the database
def readdb():
    db = shelve.open('people-shelve')
    for key in db:
        print(key, '=>\n ', db[key])
    db.close()

# read single record from the database
def readrec(rec):
    db = shelve.open('people-shelve')
    print(rec, '=>\n ', db[rec])
    db.close()

# add record to the database
def addrec(rec):
    db = shelve.open('people-shelve')
    db[rec['name'].split()[0].lower()]=rec
    db.close()

# delete record from database
def delrec(rec):
    db = shelve.open('people-shelve')
    del db[rec]
    db.close()


dejan   = { 'name': 'Dejan Stojcevski', 'age': 46, 'pay': 90000, 'job': 'dev' }
bob     = { 'name': 'Bob Smith',        'age': 42, 'pay': 30000, 'job': 'dev' }
sue     = { 'name': 'Sue Jones',        'age': 45, 'pay': 40000, 'job': 'hdw' }
tom     = { 'name': 'Tom Smith',        'age': 50, 'pay': 0,     'job':  None }

for x in (dejan,bob,sue,tom): addrec(x)
readrec('dejan')
