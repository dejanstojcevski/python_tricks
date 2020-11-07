import shelve

# read all records from the database
def readdb():
    db = shelve.open('people-shelve')
    for key in db:
        print(key, '=> ', db[key])
    db.close()

# read single record from the database
def readrec(rec):
    db = shelve.open('people-shelve')
    print(rec, '=>\n ', db[rec])
    db.close()

# add record to the database
def addrec(rec):
    db = shelve.open('people-shelve')
    db[rec.tel]=rec
    db.close()

# delete record from database
def delrec(rec):
    db = shelve.open('people-shelve')
    del db[rec]
    db.close()

# we will add instancess of the class into shelve database
class Person():
    def __init__(self,tel,name,addr):
        self.tel=tel
        self.name=name
        self.addr=addr
    def __repr__(self):
        return('Ime: %s; Telefon: %s; Adresa: %s' % (self.name,self.tel,self.addr))
    def change_name(self,newname):
        self.name=newname

dejan=Person('075400639','Dejan Stojcevski','bul. Vidoe smilevski - Bato No 44/16')
boban=Person('075300123','Boban Stojcevski','bul. Metodija Mitevski No 13 4/4')
addrec(dejan)
addrec(boban)
readdb()
