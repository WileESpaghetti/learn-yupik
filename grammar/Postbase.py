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

import Base, Vowel, string, Word

postbaseSymbols = ('+', '-', '~', '÷', ':', '\'', '@', '- -', '%', '(', ')')

def explodePostbase(postbase):
	"""split a postbase into it's different parts"""
	pass

#postbase must be in full dictionary form. eg. +'(g/t)uq
#FIXME: can multple ()'s occure in postbases?
def getParenOptions(postbase):
	""" converts the ()'s in the postbase to a tuple """
	#FIXME: make this return a tuple
	options = []
	parenOpen = string.find(postbase, '(') + 1
	parenClose = string.find(postbase, ')')
	options = string.split(postbase[parenOpen : parenClose], '/')

	return options

def parenLetter(word, postbase):
	""" returns the letter that should be picked from inside of the ()'s in postbase notation """
	letter = ''
	classnum = Base.getClassAsInt(word)

	for c in getParenOptions(postbase):
		if c == 'g' and classnum == 2:
			letter = 'g'
		elif c == 'ng' and classnum <= 4:
			letter = 'ng'
		elif c == 's' and classnum <= 4:
			letter = 's'
		elif c == 't' and classnum >= 5:
			letter = 't'
		elif c == 'u' and classnum >= 3:
			letter = 'c'

	return letter

def getVelarDropPostbases(postbase):
	""" returns the postbase with the velar and with the velar dropped """
	#FIXME ^ this docstring is really terrible and unclear
	#FIXME might make sense to return a dictionary {'wDrop': '', 'woDrop': ''}
	velarDropPostbase = ''
	colon = string.find(postbase, ":")
	velarStart = postbase[:colon]
	velarEnd = postbase[colon + 1:]
	velarPostbase = velarStart + velarEnd

	if velarEnd[:2] == 'ng':
		velarDropPostbase = velarStart + velarEnd[2:]
	else:
		velarDropPostbase = velarStart + velarEnd[1:]

	return [velarPostbase, velarDropPostbase]

def stripEZStuff(word, postbase):
	"""remove the parts of postbase from word that doesn't need any special calculation"""
	parenOpen = string.find(postbase, '(')
	parenClose = string.find(postbase, ')') + 1

	postStart = postbase[:parenOpen]
	postEnd = postbase[parenClose:]

	# need to do this instead of using rstrip() because of issues like rstrip("tuquuq", "uq") -> "t"
	# instead of "tuqu"
	newend = string.rfind(word, postEnd)
	word = word[:newend]

	return word

def isParensStripped(word, postbase):
	""" find out whether or not a letter in parenthesis needs to be removed """
	#options = getParenOptions(postbase)
	stripParen = False
	pl = parenLetter(word[:-1], postbase)
	last = word[-1]
	if word[-1] == pl and not pl == '':
		stripParen = True

	return stripParen

def stripParenLetter(word, postbase):
	""" detect which letter needs to be selected from inside of ()'s and remove it """
	#FIXME it doesn't actually look like this does anything or is used?
	removeParen = isParensStripped(word, postbase)
	if removeParen:
		pass

def stripPostbase(word, postbase):
	""" removes a postbase from a word. see wiki for info reguarding postbase syntax """
	print("Removing postbase:\t%s" % postbase)

	word = stripEZStuff(word, postbase)

	# detect which letters in parenthesis we need to remove if any
	removeParen = isParensStripped(word, postbase)
	if removeParen:
		word = word[:-1]

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

def getPostbaseOptions(postbase):
	"""translate the list of symbols in a postbase into flag veriables to be used when applying postbases.
	return as a dictionary"""
	pass

def applyPostbase(word, postbase):
	""" add a postbase to a word """
	keepCfinal = False
	dropCfinal = False
	dropEfinal = False
	keepStrongCfinal = False
	dropVelar = False
	gemination = False
	# @ symbol?
	dropVCfinal = False
	attachIrregular = False
	containsParens = False

	if postbase[0] == '+':
		keepCfinal = True

	if postbase[0] == '-':
		dropCfinal = True

	if string.find(postbase, '~') > -1:
		dropEfinal = True

	if postbase[0] == '÷':
		keepStrongCfinal = True

	if string.find(postbase, ':') > -1:
		dropVelar = True

	if string.find(postbase, '\'') > -1:
		gemination = True

	if postbase[0] == '- -':
		dropVCfinal = True

	if postbase[0] == '%':
		attachIrregular = True

	if string.find(postbase, '(') > -1:
		containsParens = True

	if keepCfinal:
		#FIXME what if '+' not the first char in postbase?
		postbase = postbase[1:]

	if containsParens:
		pl = parenLetter(word, postbase)
		
		#FIXME, what if multiple parens
		parenOpen = string.find(postbase, '(')
		parenClose = string.find(postbase, ')') + 1

		postbase = postbase[:parenOpen] + pl + postbase[parenClose:]

	if gemination:
		isV = False
		if word[-3:-1] == 'ng':
			isV = Vowel.isVowel(word[-4])
		else:
			isV = Vowel.isVowel(word[-3])
		isVCE = word[-1] == 'e' and isV and not Vowel.isVowel(word[-2]) # FIXME aurre currently gets computed incorrect. along with some +(g/t):nga words.
		if word[-1] == 'e':
			word = word[:-1]
			if isVCE and Word.syllableCount(word) == 1:
				# FIXME only add the ' to one syllable words? need grammar rule specifics
				word = word + '\''

	# strip gemination marker
	#FIXME: this feels like it should go somewhere else
	apos = string.find(postbase, '\'')
	if apos > -1:
		postbase = postbase[:apos] + postbase[apos+1:]
		if string.find(postbase, '\\') > -1:
		#FIXME there's a mysterious '\' when selecting words from db. endings probably not escaped properly in db
			slash = string.find(postbase, '\\')
			postbase = postbase[:slash] + postbase[slash+1:]

	if dropCfinal:
		#FIXME what if '-' not the first char in postbase?
		postbase = postbase[1:]
		if not Word.isVowel(word[-1]):
			word = word[:-1]

	if dropEfinal:
		tilde = string.find(postbase, '~')
		postbase = postbase[:tilde] + postbase[tilde+1:]
		if word[-1] == 'e':
			word = word[:-1]

	
	if dropVelar:
		testsuf = word[-1] + postbase
		colon = string.find(testsuf, ":")
		velar = ''
		lvowel = False
		rvowel = False
		
		lvowel = Vowel.isVowel(testsuf[colon-1]) and not Vowel.isVowel(testsuf[colon-2])

		if testsuf[colon+1] == 'n' and testsuf[colon+2] == 'g':
			rvowel = Vowel.isVowel(testsuf[colon+3])
		else:
			rvowel = Vowel.isVowel(testsuf[colon+2])

		colon = string.find(postbase, ":")
		if lvowel and rvowel:
			if postbase[colon+1] == 'n' and postbase[colon+2] == 'g':
				postbase = postbase[:colon] + postbase[colon+3:]
			else:
				postbase = postbase[:colon] + postbase[colon+2:]
		else:
			postbase = postbase[:colon] + postbase[colon+1:]

	word = word + postbase

	#cleanup for words that wind up not needing the \' for gemination because they are followed by 2 vowels
	#FIXME not tested on words that contain 2 \' ...does such a word exist?
	gemmarker = string.find(word, "\'")
	if len(word) >= gemmarker + 2:
		# ^ prevents crashing when word enough character to have 2 vowels following the \'
		if Vowel.isVowel(word[gemmarker+1]) and Vowel.isVowel(word[gemmarker+2]):
			word = word[:gemmarker] + word[gemmarker+1:]
	return word

