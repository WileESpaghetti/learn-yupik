#!python
#encoding: utf-8
#columns

#consonants = list(set(stops + fricatives +  nasals))

# acegiklmnpqrstuvwy

consonants = ['p', 't', 'c',]
alphabet = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']
doubled = ['g', 'l', 'r', 's', 'v']

def isADouble(c):
	isD = False
	for d in doubled:
		if c == d:
			isD = True
			break
	return isD

# refactored
stops = ['p', 't', 'c', 'k', 'q']

def isStop(c):
	""" is c a stop """
	isS = False
	for s in stops:
		if c == s:
			isS = True
			break
	return isS

# 'w' is voiceless counterpart of 'ug'
# FIXME need to add the voiced arched 'u' digraphs 'ug', 'ur' and voiceless 'urr'
voicedFricatives = 		['v', 'l', 's', 'g', 'r', 'y']
voicelessFricatives = 	['vv', 'll', 'ss', 'gg', 'rr', 'w']
fricatives = 			voicedFricatives + voicelessFricatives

def isFricative(c):
	""" is c a fricative """
	isF = False
	for f in fricatives:
		if c == f:
			isF = True
			break
	return isF

def isVoicedFricative(c):
	""" is c a fricative """
	isF = False
	for f in voicedFricatives:
		if c == f:
			isF = True
			break
	return isF

# TODO: do we want to account for automatic devoicing?
def isVoicelessFricative(c):
	""" is c a fricative """
	isF = False
	for f in voicelessFricatives:
		if c == f:
			isF = True
			break
	return isF


voicedNasals = ['m', 'n', 'ng']
voicelessNasals = ['ḿ', 'ń', 'ńg']
nasals = voicedNasals + voicelessNasals

def isNasal(c):
	""" is c a nasal """
	isN = False
	for n in nasals:
		if c == n:
			isN = True
			break
	return isN

def isVoicedNasal(c):
	""" is c a nasal """
	isN = False
	for n in voicedNasals:
		if c == n:
			isN = True
			break
	return isN

def isVoicelessNasal(c):
	""" is c a nasal """
	isN = False
	#print('c is ' + c)
	for n in voicelessNasals:
		if c == n:
			isN = True
			break
	return isN

primeVowels = ['a','i','u']
vowels = ['a', 'e', 'i', 'u']

def isVowel(c):
	""" is c a vowel """
	isV = False
	for v in vowels:
		if c == v:
			isV = True
			break
	return isV

def isPrimeVowel(c):
	isPrime = False
	for v in primeVowels:
		if c == v:
			isPrime = True
			break
	return isPrime

# WARNING: this function should always be used instead of "not isVowel()". This is because
# apostrophes are only considered a letter when used as the gemmination marker. "not isVowel()"
# will cause some false positives if an apostrophe is being used for a different purpose.
# FIXME: need to refactor code that uses the "not isVowel()" pattern
# FIXME: does not correctly test \'
def isConsonant(c):
	""" is c a consonant """
	isC = False
	consonants = []
	consonants.extend(stops)
	consonants.extend(nasals)
	consonants.extend(fricatives)

	for i in consonants:
		if i == c:
			isC = True
			break
		elif c == '\'':
			#FIXME, need to refactor this part
			# this is left in to keep some things from breaking
			# \' should only be considered a consonany if used for gemmination
			isC = True
			break

	return isC
