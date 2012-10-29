#!python
#encoding: utf-8
import Base, Vowel, string

#postbase must be in full dictionary form. eg. +'(g/t)uq
#FIXME: can multple ()'s occure in postbases?
def getParenOptions(postbase):
	options = []
	parenOpen = string.find(postbase, '(') + 1
	parenClose = string.find(postbase, ')')
	options = string.split(postbase[parenOpen : parenClose], '/')
	return options
	

def parenLetter(word, postbase):
	letter = ''
	classnum = Base.getClassAsInt(word)
	for c in getParenOptions(postbase):
		if c == 'g' and classnum == 2:
			letter = 'g'
		elif c == 'ng' and classnum <= 4:
			letter = 'ng'
		elif c == 's' and classnum <= 4:
			letter = 's'
		elif c == 't' and (classnum == 5 or classnum == 6):
			letter = 't'
		elif c == 'u' and classnum >= 3:
			letter = 'c'
	return letter

def stripPostbase(word, postbase):
	print("Removing postbase:\t%s" % postbase)

	#strip everything that doesn't need calculated
	parenOpen = string.find(postbase, '(')
	parenClose = string.find(postbase, ')') + 1

	postStart = postbase[:parenOpen]
	postEnd = postbase[parenClose:]

	word = string.rstrip(word, postEnd)
	print("Removing {0}:\t\t{1}".format(postEnd, word))

	# detect which letters in parenthesis we need to remove if any
	options = getParenOptions(postbase)
	removeParen = False
	for c in options:
		# special case so that 'ng' isn't removed by accident
		if c == 'g' and word[-2] == 'n':
			c = ''

		basetmp = word.rstrip(c)
		if (not c == '' and parenLetter(basetmp, postbase)) == c:
			print("need to remove %s" % c)
			word = basetmp
            if word[-1] == c:
			    removeParen = True
		#print("Removing {0}:\t\t{1}".format(c, word))

	if word[-1] == "\'":
		word = word[:-1] + 'e'
	elif  removeParen == False and not Vowel.isVowel(word[-1]):
		word = word + 'e'

	#if not Vowel.isVowel(word[-1]):
		#word = word + 'e'
	print("final form:\t\t%s" % word)
	print('')
	

#parenLetter("+\'(g/t)uq")
#print(getParenOptions("+\'(g/t)uq"))
