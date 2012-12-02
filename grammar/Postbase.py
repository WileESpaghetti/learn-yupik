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
	""" split the word into it's letters. this makes working with letters made up
	of more than one character (eg. 'll' or 'ng' a whole lot easier """
	#FIXME should \' be treated as a separate letter or combined with the letter
	# it is telling to geminate (eg. r') or completely omited in the output
	#FIXME needs to throw exception if incorrect character found
	exploded = []
	
	tmp = ''
	inParens = False
	for i in range(len(postbase)):
		if inParens:
			tmp += postbase[i]
			if postbase[i] == ')':
				exploded.append(tmp)
				tmp = ''
				inParens = False
		else:
			if postbase[i] == '(':
				inParens = True
				tmp += '('
			else:
				dl = False
				for l in Word.doubled:
					if postbase[i] == l:
						dl = True

				# test if a letter is a valid doubled letter or is 'ng'
				if i > 0 and dl and exploded[-1] == postbase[i]:
					exploded[-1] = postbase[i] + postbase[i]
				elif i > 0 and exploded[-1] == 'n' and postbase[i] == 'g':
					exploded[-1] = 'ng'
				else:
					exploded.append(postbase[i])

	# combine velar with the drop velar (:) symbol
	# FIXME this logic is probably better up in the code above, but it was easier to put it here
	for i in range(len(exploded)):
		if i > 0 and exploded[i-1] == ':':
			exploded[i-1] += exploded[i]
			exploded.pop(i)
	
	return exploded

#print(explodePostbase("+'(g/t)uq"))
print(explodePostbase("+'(g/t)u:nga"))

def validatePostbase(postbase):
	"""checks to make sure postbase is properly formed"""
	valid = False
	return valid

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

	velarPostbase = postbase[:colon] + postbase[colon + 1:]

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
	#TODO would be cool if you could pass a list of postbases in here and have it do the "right thing"
	exp = Base.explode(word)
	keepStrongCfinal = False
	# @ symbol?
	dropVCfinal = False
	attachIrregular = False

	#keep the final consonant
	plus = string.find(postbase, '+')
	if plus > -1:
		postbase = postbase[:plus] + postbase[plus+1:]

	# FIXME need to check against words that contain '-' as a part of the word
	# FIXME this might cause trouble with enclitics
	# remove the last consonant
	minus = string.find(postbase, '-')
	if minus > -1:
		postbase = postbase[:minus] + postbase[minus+1:]
		if not Word.isVowel(exp[-1]):
			exp.pop(-1)

	# remove final 'e'
	tilde = string.find(postbase, '~')
	if tilde > -1:
		postbase = postbase[:tilde] + postbase[tilde+1:]
		if exp[-1] == 'e':
			exp.pop(-1)

	# choose between letters in parenthesis
	paren = string.find(postbase, '(')
	if  paren > -1:
		pl = parenLetter(word, postbase)
		#FIXME, what if multiple parens
		parenOpen = string.find(postbase, '(')
		parenClose = string.find(postbase, ')') + 1

		postbase = postbase[:parenOpen] + pl + postbase[parenClose:]

	# add gemination if needed
	#FIXME not tested on words that contain 2 \' ...does such a word exist?
	apos = string.find(postbase, '\'')
	if apos > -1:
		postbase = postbase[:apos] + postbase[apos+1:]
		
		# FIXME this may indicate that there's something that needs tweaked about the syllablematches
		# function. A short base is defined as [C]VCe, currently this only tests the end of the word.
		# this should match VCe and CVCe only
		shortA = len(exp) == 3 and Word.syllableMatches(exp, 'VCe')
		shortB = len(exp) == 4 and Word.syllableMatches(exp, 'CVCe')
		if shortA or shortB:
			exp.pop(-1)
			if Word.syllableCount(exp) == 1:
				exp.append('\'')
		elif exp[-1] == 'e':
			exp.pop(-1)

	# velar dropping suffixes
	colon = string.find(postbase, ':')
	if colon > -1:
		testsuf = exp[-1] + postbase
		testExp = Base.explode(testsuf)
		colon = testExp.index(':')
		velar = testExp[colon+1]
		testExp = testExp[:colon] + testExp[colon+1:]

		if Word.syllableMatches(testExp, 'CV' + velar + 'V'): #FIXME might crash if word isn't long enough
			testExp = Base.explode(postbase)
			colon = testExp.index(':')
			testExp.pop(colon)
			testExp.pop(colon)
		else:
			testExp = Base.explode(postbase)
			colon = testExp.index(':')
			testExp.pop(colon)

		postbase = ''.join(testExp)


	if postbase[0] == '÷':
		keepStrongCfinal = True

	if string.find(postbase, ':') > -1:
		dropVelar = True

	if postbase[0] == '- -':
		dropVCfinal = True

	if postbase[0] == '%':
		attachIrregular = True

	word = ''.join(exp)
	word = word + postbase

	#cleanup for words that wind up not needing the \' for gemination because they are followed by 2 vowels
	#FIXME not tested on words that contain 2 \' ...does such a word exist
	exp = Base.explode(word)
	try:
		gemmarker = exp.index('\'')
	except ValueError:
		gemmarker = -1
	if gemmarker > -1 and len(exp) >= gemmarker + 3:
		syl = exp[gemmarker+1:gemmarker+3]
		if Word.syllableMatches(syl, 'VV'):
			exp.pop(gemmarker)

	word = ''.join(exp)

	return word

