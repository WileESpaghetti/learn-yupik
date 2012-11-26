#!python
#encoding: utf-8
import sqlite3, grammar.Postbase
dbcon = sqlite3.connect('testdb.db')
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

#print(getPostbases())
#print(getEndings())
print(getStems())

for w in getStems():
	for e in getSuffixes():
		print(grammar.Postbase.applyPostbase(w, e))

print(applyPostbase(applyPostbase('nere', '-nrite'), '+\'(g/t)u:nga'))
print(applyPostbase(applyPostbase(applyPostbase('nere', '@~yug'), '-llru'), '+\'(g/t)uq'))
