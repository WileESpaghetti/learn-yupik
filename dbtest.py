#!python
#encoding: utf-8
import sqlite3, grammar.Postbase
dbcon = sqlite3.connect('yupik_dictionary.db')
dbcon.text_factory = str
c = dbcon.cursor()

def getSuffixes():
    pb = []
    for row in c.execute('SELECT * FROM words where word_type=2 or word_type=3;'):
            pb.append(row[1])
    return pb

def getPostbases():
    pb = []
    for row in c.execute('SELECT * FROM words where word_type=2;'):
            pb.append(row[1])
    return pb

def getEndings():
    pb = []
    for row in c.execute('SELECT * FROM words where word_type=3;'):
            pb.append(row[1])
    return pb

def getStems():
    pb = []
    for row in c.execute('SELECT * FROM words where word_type=1;'):
            pb.append(row[1])
    return pb

def getBases():
    pb = []
    for row in c.execute('SELECT * FROM words where word_type=1 or word_type=5;'):
            pb.append(row[1])
    return pb

def getEnclitics():
    pb = []
    for row in c.execute('SELECT * FROM words where word_type=4;'):
            pb.append(row[1])
    return pb

for w in getStems():
    for e in getSuffixes():
        print(grammar.Postbase.applyPostbase(w, e))
    print("")

print(grammar.Postbase.applyPostbase(grammar.Postbase.applyPostbase('nere', '-nrite'), '+\'(g/t)u:nga'))
print(grammar.Postbase.applyPostbase(grammar.Postbase.applyPostbase(grammar.Postbase.applyPostbase('nere', '@~yug'), '-llru'), '+\'(g/t)uq'))
