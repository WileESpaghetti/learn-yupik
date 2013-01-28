#!python
#encoding: utf-8
#columns
labials = ['p', 'v', 'vv', 'n', 'ń']
apicals = ['t', 'l', 'll', 'n', 'ń', 'c', 's', 'y', 'ss']
frontVelars = ['k', 'g', 'gg', 'ng', 'ńg', 'q', 'r', 'rr']
labializedFrontVelars = ['ug', 'w']
labializedbackVelars = ['ur', 'urr']

# rows

#consonants = list(set(stops + fricatives +  nasals))

#vowel columns
frontVowels = ['i']
midVowels = ['e', 'a']
backVowels = ['u']

#rows
highVowels = ['i', 'e', 'u']
lowVowels = ['a']

primeVowels = ['a', 'i', 'u']

vowels = highVowels + lowVowels


# acegiklmnpqrstuvwy

vowels = ['a', 'e', 'i', 'u']
consonants = ['p', 't', 'c',]






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
