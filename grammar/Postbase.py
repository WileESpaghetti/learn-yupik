#!python
#encoding: utf-8
import Base, string

#postbase must be in full dictionary form. eg. +'(g/t)uq
#FIXME: can multple ()'s occure in postbases?
def parenLetter(word, postbase):
	letter = ''
	classnum = Base.getClassAsInt(word)
	#print(classnum)
	#print(postbase)
	parenOpen = string.find(postbase, '(') + 1
	#print(parenOpen)
	parenClose = string.find(postbase, ')')
	#print(parenClose)
	options = postbase[parenOpen : parenClose]
	#print(string.split(options, '/'))
	for c in options:
		if c == 'g' and classnum == 2:
			letter = 'g'
		elif c == 'ng' and classnum <= 4:
			letter = 'ng'
		elif c == 's' and classnum <= 4:
			letter = 's'
		elif c == 't' and (classnum == 4 or classnum == 5):
			letter = 't'
		elif c == 'u' and classnum >= 3:
			letter = 'c'
	print(letter)
	return letter
	
	

#parenLetter("+\'(g/t)uq")
