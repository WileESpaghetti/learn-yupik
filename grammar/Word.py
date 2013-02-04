#!python
#encoding: utf-8
import Base, Alphabet

#letters that can be doubled
# FIXME this might be done by specific character classes instead - fricatives pnly?


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
			if i<=j:
				if inBrackets:
					# FIXME not sure if there is really anything to do but ignore
					if form[i] == '[':
						inBrackets = False
						j += 1
				else:
					if form[i] == 'V' and Alphabet.isVowel(syl[j]):
						sylMatches = True
						j += 1
					elif form[i] == 'C' and not Alphabet.isVowel(syl[j]):
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
				elif form[i] == 'C' and not Alphabet.isVowel(syl[j]):
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
			if not Alphabet.isVowel(c) and not Alphabet.isVowel(exp[i+1]):
				syllables.append(syl)
				syl = []
	syllables.append(syl)

	syl = []
	syl2 = []
	for s in syllables:
		for i in range(len(s)):
			if not Alphabet.isVowel(s[i]) and (i > 0 and i < len(s) - 1):
				if Alphabet.isVowel(s[i-1]) and Alphabet.isVowel(s[i+1]):
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


def isVelar(c):
	""" is c a velar """
	pass


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
				if Alphabet.isVowel(exp[i-1]):
					if Alphabet.isVowel(exp[i+1]):
						purpose = APOS_PREVENT_GEMMINATION
						break
					elif exp[i+1] == 'r':
						purpose = APOS_DISRUPT_STRESS
						break
				else:
					if Alphabet.isVowel(exp[i+1]):
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
	elif Alphabet.isVoicelessFricative(l):
		voiced = False
	elif Alphabet.isVoicelessNasal(l):
		voiced = False
	elif Alphabet.isVoicedFricative(l):
		if c > 0 and (Alphabet.isVoicelessFricative(exp[c-1]) or Alphabet.isStop(exp[c-1])):
			voiced = False
		elif c < len(exp) - 1 and Alphabet.isStop(exp[c+1]):
			voiced = False
	elif Alphabet.isVoicedNasal(l) and c > 0 and (Alphabet.isVoicelessFricative(exp[c-1]) or Alphabet.isStop(exp[c-1])):
		voiced = False

	return voiced


def getRhythmicVowelLengthPattern(word):
	"""returns a list of booleans representing which syllables have rhythmic length """
	rhythmicLength = []
	syl = getSyllables(word)
	cvCount = 0

	for s in syl:
		if syllableMatches(s, 'CV'):
			cvCount += 1
			if cvCount % 2 == 0:
				#FIXME should not be true if cvCount = 0 because of the cvCount +=1 line, but need to test just to make sure. 0 should return false
				rhythmicLength.append(True)
			else:
				rhythmicLength.append(False)
		else:
			cvCount = 0
			rhythmicLength.append(False)

	# probably not best this way, but last syllable doesn't receive rhythmic Length ever.
	rhythmicLength[-1] = False

	return rhythmicLength

def hasRhythmicLength(word, index):
	""" does the sylIndex-th syllable have rhythmic vowel length """
	exp = Base.explode(word)
	syl = getSyllables(word)
	rl = getRhythmicVowelLengthPattern(word)
	rlexp = []
	for s in range(len(syl)):
		for r in range(len(syl[s])):
			rlexp.append(rl[s])
	return rlexp[index]

def getAutoGemminationPattern(word):
	gempat = []
	exp = Base.explode(word)
	rl = getRhythmicVowelLengthPattern(word)
	for i in range(len(exp)):
		if i > 0 and i < len(exp)-2:
			if Alphabet.isVowel(exp[i-1]) and Alphabet.isConsonant(exp[i]) and Alphabet.isVowel(exp[i+1]) and Alphabet.isVowel(exp[i+2]):
				gempat.append(True)
			else:
				gempat.append(False)
		elif i > 0 and exp[i-1] == 'e' and hasRhythmicLength(word,i-1):
			gempat.append(True)
		else:
			gempat.append(False)
	return gempat

def getStressPattern(word):
	stressPat = []
	syl = getSyllables(word)
	rhy = getRhythmicVowelLengthPattern(word)
	ruleOne = False
	numStressed = 0

	for i in range(len(syl)):
		if ruleOne:
			numStressed += 1
		# first syllable is closed
		if i < len(syl) -1 :
			if i == 0 and syllableMatches(syl[i], 'C'):
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# syllable is closed and previous syllable is unstress/open
			elif i > 0 and syllableMatches(syl[i],'C') and not stressPat[-1] and syllableMatches(syl[i-1],'V'):
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# syllable contains VV
			elif syllableMatches(syl[i],'[C]VV[C]'):
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# syllable is rhythmically lengthened
			elif rhy[i]:
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# after finding one of the above rules, every even number syllable gets stress
			elif ruleOne and numStressed > 0 and numStressed%2 == 0 and syllableMatches(syl[i],'C'):
				stressPat.append(True)
			#syllable preceeding one containing VV
			#FIXME group of OR statements below is a workaround because '[]' format doesn't work correctly in syllableMatches()
			elif i < len(syl) - 1 and (syllableMatches(syl[i+1],'CVV') or syllableMatches(syl[i+1],'VVC') or syllableMatches(syl[i+1],'VV')):
				stressPat.append(True)
			else:
				stressPat.append(False)
		else:
			stressPat.append(False)
	return stressPat

