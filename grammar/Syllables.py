import Base, Alphabet

__author__ = 'Lehman'

#FIXME needs to throw exception if '[]' passed in. need to also write test for this case
def syllableMatches(syl, form):
	""" eg. syllableMatches('rte', '[V]VCe')
	capital 'V' or 'C' match vowels and consonants respectively
	letters in []'s shows optional letters. checks from the end of the word"""
	# FIXME this is not necessarily done on a syllable by syllable basis. sometimes it
	# can overlap boundaries
	sylMatches = False

	# better handling of 'ng' and other double letters
	syl = Base.explode(syl)
	form = Base.explode(form)

	syl = syl[::-1]
	form = form[::-1]

	#FIXME need to write test about if form longer than syl has correct behavior
	#FIXME optional '[]' letters should not increment i
	inBrackets = False
	j = 0

	if len(syl) > 0 and len(syl) >= len(form):
		for i in range(len(form)):
			if i <= j:
				if inBrackets:
					# FIXME not sure if there is really anything to do but ignore
					if form[i] == '[':
						inBrackets = False
						j += 1
				else:
					if form[i] == 'V' and Alphabet.isVowel(syl[j]):
						sylMatches = True
						j += 1
					elif form[i] == 'C' and Alphabet.isConsonant(syl[j]):
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
			else:
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
				if form[i] == 'V' and Alphabet.isVowel(syl[j]):
					sylMatches = True
					j += 1
				elif form[i] == 'C' and Alphabet.isConsonant(syl[j]):
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
			if Alphabet.isConsonant(c) and Alphabet.isConsonant(exp[i + 1]):
				syllables.append(syl)
				syl = []
	syllables.append(syl)

	syl = []
	syl2 = []
	for s in syllables:
		for i in range(len(s)):
			if Alphabet.isConsonant(s[i]) and (i > 0 and i < len(s) - 1):
				if Alphabet.isVowel(s[i - 1]) and Alphabet.isVowel(s[i + 1]):
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
