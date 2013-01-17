#!python
#encoding: utf-8
import Base, Alphabet

vowels = ['a', 'e', 'i', 'u']
primeVowels = ['a', 'i', 'u']

consonants = ['\'','c','gg','g','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','vv','v','w','y']

fricatives = ['v', 'l', 's', 'y', 'g', 'r', 'ug', 'ur', 'vv', 'll', 'ss', 'gg', 'rr', 'w', 'urr']
stops = ['p','t','c','k','q']
nasals = ['m','n','ng']
alphabet = ['\'', 'a', 'c', 'e', 'g', 'gg', 'i', 'k', 'l', 'll', 'm', 'n', 'ng', 'p', 'q', 'r', 'rr', 's', 'ss', 't', 'u', 'v', 'vv', 'w', 'y']

#letters that can be doubled
# FIXME this might be done by specific character classes instead - fricatives pnly?
doubled = ['g', 'l', 'r', 's', 'v']

#FIXME needs to throw exception if '[]' passed in. need to also write test for this case
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

	if len(syl) > 0:
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

#FIXME needs to throw exception if '[]' passed in. need to also write test for this case
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

	if len(syl) > 0:
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

# FIXME need to verify how apostrophes are split depending on their function
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

# TODO write functions for is open syllable, simple syllable, etc.
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

def isVoicedFricative(c):
	""" is c a fricative """
	isF = False
	for f in Alphabet.voicedFricatives:
		if c == f:
			isF = True
			break
	return isF

def isVoicelessFricative(c):
	""" is c a fricative """
	isF = False
	for f in Alphabet.voicelessFricatives:
		if c == f:
			isF = True
			break
	return isF

def isStop(c):
	""" is c a stop """
	isS = False
	for s in stops:
		if c == s:
			isS = True
			break
	return isS

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
	for n in Alphabet.voicedNasals:
		if c == n:
			isN = True
			break
	return isN

def isVoicelessNasal(c):
	""" is c a nasal """
	isN = False
	#print('c is ' + c)
	for n in Alphabet.voicelessNasals:
		#print ('n is ' + n)
		#print('c is ' + c)
		if c == n:
			isN = True
			break
	#print(isN)
	return isN

def isConsonant(c):
	""" is c a consonant """
	return not isVowel(c)

# uses for apostrophe's
# 0. mark gemination - taq'uq (C'V)
# 1. separate n and g - tan'gurraq
# 2. separated stop and voices fricative or nasal - it'gaq
# 3. prevent automatic gemination - atu'urkaq
# 4. indicate departer from usual stress pattern -  qvartu'rtuq
# 5. indicate end of a word was dropped - qaill' instead of qaillun (how)
# FIXME what about multiple \' in a word?

APOS_GEMINATION_MARKER = 0
APOS_NG_SEPARATOR = 1
APOS_PREVENT_DEVOICING = 2
APOS_PREVENT_GEMMINATION = 3
APOS_DISRUPT_STRESS = 4
APOS_SHORT_WORD = 5

def apostrophePurpose(word):
	"""is the apostrophe being used for gemination, separate 'n' and 'g', etc."""
	exp = Base.explode(word)
	purpose = -1
	for i in range(len(exp)):
		if i > 0 and exp[i] == '\'':
			if i < len(exp) - 1:
				if isVowel(exp[i-1]):
					if isVowel(exp[i+1]):
						purpose = APOS_PREVENT_GEMMINATION
						break
					elif exp[i+1] == 'r':
						purpose = APOS_DISRUPT_STRESS
						break
				else:
					if isVowel(exp[i+1]):
						purpose = APOS_GEMINATION_MARKER
						break
					elif exp[i-1] == 'n' and exp[i+1] == 'g':
						purpose = APOS_NG_SEPARATOR
						break
					else:
						# FIXME need to test if a catch-all is appropriate. technically the only
						# other valid use of a \' is whenever auto-devoicing occurs. (stop + nasal || fric)
						#FIXME need to do research on autodevoicing to make sure this ^^ is acurate
						# FIXME will need to write a test to make sure cases without auto devoicing are not matched
						purpose = APOS_PREVENT_DEVOICING
						break
			else:
				purpose = APOS_SHORT_WORD
	return purpose

def isAutoDevoiced(word, index):
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
	# FIXME does not properly handle if char other than a stop or fricative is found at 'c'
	voiced = True
	exp = Base.explode(word)
	l = exp[c]
	if c == 0 and l == 's':
		voiced = False
	elif c == len(exp) - 1 and l == 'r':
		voiced = False
	elif isVoicelessFricative(l):
		voiced = False
	elif isVoicelessNasal(l):
		voiced = False
	elif isVoicedFricative(l):
		if c > 0 and (isVoicelessFricative(exp[c-1]) or isStop(exp[c-1])):
			voiced = False
		elif c < len(exp) - 1 and isStop(exp[c+1]):
			voiced = False
	elif isVoicedNasal(l) and c > 0 and (isVoicelessFricative(exp[c-1]) or isStop(exp[c-1])):
		voiced = False

	return voiced


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
