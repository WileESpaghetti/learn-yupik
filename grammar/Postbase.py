#!python
#encoding: utf-8

# grammar rules for postbase syntax
# +	keeps final consonant of base
# -	drops final consonent
# ~	drops final 'e'
# ÷	keeps strong final consonents
# :	drops voiced velar consonents if between single vowels where first vowel is prime
# '	causes gemination of final consonent if base in the form of (C)VCe-
# @	???
# - -	base drops final conconant + vowel preceeding it. (only for shortened forms of consonent dropping postbases beginning with 'li'
# %	attaches irregularly (certain non-productive postbases only)
# ()	one of the letters (separated by '/') is selected based on certain rules

# grammar rules for selecting letters in '()'
# g	Class II	ends with one or two prime vowels
# ng	Class I - IV	ends with a vowel
# s	Class I - IV	ends with a vowel
# t 	Class V - VI	ends in a consonant
# u	Class III - VI	ends in 'e' or a consonant

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

def getVelarDropPostbases(postbase):
	colon = string.find(postbase, ":")
	velarStart = postbase[:colon]
	velarEnd = postbase[colon + 1:]
	velarPostbase = velarStart + velarEnd
	velarDropPostbase = ''

	if velarEnd[:2] == 'ng':
		velarDropPostbase = velarStart + velarEnd[2:]
	else:
		velarDropPostbase = velarStart + velarEnd[1:]

	return [velarPostbase, velarDropPostbase]

def stripPostbase(word, postbase):
	print("Removing postbase:\t%s" % postbase)
	postbaseBuilder = ''

	#strip everything that doesn't need calculated
	parenOpen = string.find(postbase, '(')
	parenClose = string.find(postbase, ')') + 1

	postStart = postbase[:parenOpen]
	postEnd = postbase[parenClose:]

	# need to do this instead of using rstrip() because of issues like rstrip("tuquuq", "uq") -> "t"
	# instead of "tuqu"
	newend = string.rfind(word, postEnd)
	word = word[:newend]

	# detect which letters in parenthesis we need to remove if any
	options = getParenOptions(postbase)
	removeParen = False
	for c in options:
		# special case so that 'ng' isn't removed by accident
		if c == 'g' and word[-2] == 'n':
			c = ''

		basetmp = word.rstrip(c)
		basetmpclassnum = Base.getClassAsInt(basetmp)
		pl = parenLetter(basetmp, postbase)
		if pl == c and word[-1] == c:
			if c == 't' and Vowel.isVowel(basetmp[-1]):
				# 't' can't be added from '()' if it occurs next to a vowel
				# so it can be ignored
				pass
			else:
				removeParen = True
				word = basetmp

	if word[-1] == "\'":
		word = word[:-1] + 'e'
	elif not removeParen and Base.getClassAsInt(word) >= 5:
		# for postbases with 't' in parenthesis: 't' only gets added if word ends in consonant
		# if we removed a 't' then the word must be class V or VI. If we didn't need to remove
		# a 't' then then the word must end in a vowel. If the word claims to be V or VI but we
		# didn't need to remove anything then the word should be a class III or IV instead.
		word = word + 'e'

	print("Base Form:\t\t%s" % word)
	print('')

