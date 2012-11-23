#!python
#encoding: utf-8
vowels = ['a', 'e', 'i', 'u']
primeVowels = ['a', 'i', 'u']

fricatives = ['v', 'l', 's', 'y', 'g', 'r', 'ug', 'ur', 'vv', 'll', 'ss', 'gg', 'rr', 'w', 'urr']

def explode(word):
	""" split the word into it's letters. this makes working with letters made up
	of more than one character (eg. 'll' or 'ng' a whole lot easier """
	#FIXME should \' be treated as a separate letter or combined with the letter
	# it is telling to geminate (eg. r') or completely omited in the output
	pass

def getSyllables(word)
	""" return a list of the syllables that make up word """
	pass

def syllableMatches(syl, form):
	""" eg. syllableMatches('rte', '[V]VCe')
	capital 'V' or 'C' match vowels and consonants respectivly
	letters in []'s shows optional letters. """
	pass

def isSyllable(syl):
	""" tests if syl is a valid Yup'ik syllable """
	#FIXME add documentation of valid syllabes
	pass

def syllableCount(word):
	"""get the number of syllables in word"""
	pass

# letter types: c is a letter as represented in the explode() function and doesn;t
# actually have to be a single character. (eg. 'll' or 'ng')
def isVowel(c):
	""" is c a vowel """
	isV = False
	for v in vowels:
		if c == v:
			isV = True
			break
	return isV

def isPrimeVowel(c):
	""" is c a prime vowel? (basically every vowel except for 'e') """
	isPrime = False
	for v in primeVowels:
		if c == v:
			isPrime = True
			break
	return isPrime

def isVelar(c):
	""" is c a velar """
	pass

def isFricative(c)
	""" is c a fricative """
	isF = False
	for f in fricatives:
		if c == f:
			isF = True
			break
	return isF

def isConsonant(c):
	""" is c a consonant """
	pass

def apostrophePurpose(word):
	"""is the apostrophe being used for gemination, separate 'n' and 'g', etc."""
	pass

def isGeminationMarker(word):
	"""is the apostrophe in the word used for gemination purposes"""
	pass

def getRythmicLength(syllables, n):
	"""test the nth syllable for rythmic stress. index starts at 0"""
	pass

def isGeminated(word, c):
	"""test to see if the charcter at pos c is geminated"""
	pass

def isVoiced(word, c)
	"""test position c to see if it is voiced"""
