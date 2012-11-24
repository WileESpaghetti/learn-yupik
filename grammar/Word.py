#!python
#encoding: utf-8
vowels = ['a', 'e', 'i', 'u']
primeVowels = ['a', 'i', 'u']

fricatives = ['v', 'l', 's', 'y', 'g', 'r', 'ug', 'ur', 'vv', 'll', 'ss', 'gg', 'rr', 'w', 'urr']
alphabet = ['\'', 'a', 'c', 'e', 'g', 'gg', 'i', 'k', 'l', 'll', 'm', 'n', 'ng', 'p', 'q', 'r', 'rr', 's', 'ss', 't', 'u', 'v', 'vv', 'w', 'y']

def explode(word):
	""" split the word into it's letters. this makes working with letters made up
	of more than one character (eg. 'll' or 'ng' a whole lot easier """
	#FIXME should \' be treated as a separate letter or combined with the letter
	# it is telling to geminate (eg. r') or completely omited in the output
	exploded = []

	x = range(len(word))
	for i in x:
		c = word[i]
		if i < len(word) - 1:
			#FIXME this might pick up letters like 'uu'. this causes tuquuq to be split incorrectly
			doubleLetters = c == 'g' or c == 'l' or c == 'n' or c == 'r' or c == 's' or c == 'v'
			if (doubleLetters  and c == word[i+1]) or (c == 'n' and word[i+1] == 'g'):
				exploded.append(c + word[i+1])
				x.pop(2)		
			else:
				exploded.append(c)
		else:
			exploded.append(c)

	return exploded

def syllableMatches(syl, form):
	""" eg. syllableMatches('rte', '[V]VCe')
	capital 'V' or 'C' match vowels and consonants respectivly
	letters in []'s shows optional letters. """
	for i in form:
		if i == V:
			pass

def getSyllables(word):
	""" return a list of the syllables that make up word """
	syllables = []
	syl = []
	for i in range(len(word)):
		c = word[i]
		syl.append(c)
		if i < len(word) - 1:
			if not isVowel(c) and not isVowel(word[i+1]):
				syllables.append(syl)
				syl = []
		#print(syl)
	syllables.append(syl)
	#print(syllables)
	#print("\n\n")
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
	print(syl2)
	print("\n\n")

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

def isVoiced(word, c):
	"""test position c to see if it is voiced"""


#print(explode('alinguq'))
#getSyllables(explode('alinguq'))
#print(explode('tuquuq'))
#getSyllables(explode('tuquuq'))
#print(explode('arnaq'))
#getSyllables(explode('arnaq'))
#print(explode('arnaq'))
#getSyllables(explode('angyalingaicugnarquq'))
