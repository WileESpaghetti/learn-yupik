#!python
#encoding: utf-8
import Base

vowels = ['a', 'e', 'i', 'u']
primeVowels = ['a', 'i', 'u']

fricatives = ['v', 'l', 's', 'y', 'g', 'r', 'ug', 'ur', 'vv', 'll', 'ss', 'gg', 'rr', 'w', 'urr']
alphabet = ['\'', 'a', 'c', 'e', 'g', 'gg', 'i', 'k', 'l', 'll', 'm', 'n', 'ng', 'p', 'q', 'r', 'rr', 's', 'ss', 't', 'u', 'v', 'vv', 'w', 'y']

#letters that can be doubled
# FIXME this might be done by specific character classes instead - fricatives pnly?
doubled = ['g', 'l', 'r', 's', 'v']

def syllableMatches(syl, form):
	""" eg. syllableMatches('rte', '[V]VCe')
	capital 'V' or 'C' match vowels and consonants respectivly
	letters in []'s shows optional letters. checks from the end of the word"""
	# FIXME this is not necessarily done on a syllable by syllable basis. sometimes it
	# can overlap boundaries
	sylMatches = False

	# better handling of 'ng' and other double letters
	syl = Base.explode(syl)
	form = Base.explode(form)

	syl = syl[::-1]
	form = form[::-1]

	inBrackets = False
	j = 0
	for i in range(len(form)):
		if inBrackets:
			# FIXME not sure if there is really anything to do but ignore
			if form[i] == '[':
				inBrackets = False
				j += 1
		else:
			if form[i] == 'V' and isVowel(syl[j]):
				sylMatches = True
				j += 1
			elif form[i] == 'C' and not isVowel(syl[j]):
				sylMatches = True
				j += 1
			elif form[i] == syl[j]:
				#FIXME this may have some false positives
				sylMatches = True
				j += 1
			elif form[i] == ']':
				# we are reversed, so close brackets = open brackets
				inBrackets = True
			else:
				sylMatches = False
				break
	return sylMatches

def lSyllableMatches(syl, form):
	""" eg. syllableMatches('rte', '[V]VCe')
	capital 'V' or 'C' match vowels and consonants respectivly
	letters in []'s shows optional letters. checks from the start of the word"""
	# FIXME this is not necessarily done on a syllable by syllable basis. sometimes it
	# can overlap boundaries
	sylMatches = False

	# better handling of 'ng' and other double letters
	syl = Base.explode(syl)
	form = Base.explode(form)

	inBrackets = False
	j = 0
	for i in range(len(form)):
		if inBrackets:
			# FIXME not sure if there is really anything to do but ignore
			if form[i] == '[':
				inBrackets = False
				j += 1
		else:
			if form[i] == 'V' and isVowel(syl[j]):
				sylMatches = True
				j += 1
			elif form[i] == 'C' and not isVowel(syl[j]):
				sylMatches = True
				j += 1
			elif form[i] == syl[j]:
				#FIXME this may have some false positives
				sylMatches = True
				j += 1
			elif form[i] == ']':
				# we are reversed, so close brackets = open brackets
				inBrackets = True
			else:
				sylMatches = False
				break
	return sylMatches

def getSyllables(word):
	""" return a list of the syllables that make up word """
	syllables = []
	syl = []
	exp = Base.explode(word)

	for i in range(len(exp)):
		c = exp[i]
		syl.append(c)
		if i < len(exp) - 1:
			if not isVowel(c) and not isVowel(exp[i+1]):
				syllables.append(syl)
				syl = []
	syllables.append(syl)

	syl = []
	syl2 = []
	for s in syllables:
		for i in range(len(s)):
			if not isVowel(s[i]) and (i > 0 and i < len(s) - 1):
				if isVowel(s[i-1]) and isVowel(s[i+1]):
					syl2.append(syl)
					syl = []
			syl.append(s[i])
		syl2.append(syl)
		syl = []
	return syl2

def isSyllable(syl):
	""" tests if syl is a valid Yup'ik syllable """
	#FIXME add documentation of valid syllabes
	pass

def syllableCount(word):
	"""get the number of syllables in word"""
	return len(getSyllables(Base.explode(word)))

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

def isFricative(c):
	""" is c a fricative """
	isF = False
	for f in fricatives:
		if c == f:
			isF = True
			break
	return isF

def isConsonant(c):
	""" is c a consonant """
	return not isVowel(c)

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

def isVoiced(word, c):
	"""test position c to see if it is voiced"""
	pass


#print(explode('alinguq'))
#getSyllables(explode('alinguq'))
#print(explode('tuquuq'))
#getSyllables(explode('tuquuq'))
#print(explode('arnaq'))
#getSyllables(explode('arnaq'))
#print(explode('arnaq'))
#getSyllables(explode('angyalingaicugnarquq'))
#print(getSyllables(explode('elit')))
#print(syllableMatches('nrite', '[V]CVte'))
