#!python
#encoding: utf-8
import Base
import Alphabet
import Syllables

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
				if Alphabet.isVowel(exp[i - 1]):
					if Alphabet.isVowel(exp[i + 1]):
						purpose = APOS_PREVENT_GEMMINATION
						break
					elif exp[i + 1] == 'r':
						purpose = APOS_DISRUPT_STRESS
						break
				else:
					if Alphabet.isVowel(exp[i + 1]):
						purpose = APOS_GEMINATION_MARKER
						break
					elif exp[i - 1] == 'n' and exp[i + 1] == 'g':
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
		if c > 0 and (Alphabet.isVoicelessFricative(exp[c - 1]) or Alphabet.isStop(exp[c - 1])):
			voiced = False
		elif c < len(exp) - 1 and Alphabet.isStop(exp[c + 1]):
			voiced = False
	elif Alphabet.isVoicedNasal(l) and c > 0 and (
		Alphabet.isVoicelessFricative(exp[c - 1]) or Alphabet.isStop(exp[c - 1])):
		voiced = False

	return voiced


def getVoicingPattern(word):
	vp = []
	exp = Base.explode(word)
	for i in range(len(exp)):
		vp.append(isVoiced(word, i))

	return vp


def getRhythmicVowelLengthPattern(word):
	"""returns a list of booleans representing which syllables have rhythmic length """
	rhythmicLength = []
	syl = Syllables.getSyllables(word)
	cvCount = 0

	for s in syl:
		if Syllables.syllableMatches(s, 'CV'):
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
	syl = Syllables.getSyllables(word)
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
		if i > 0 and i < len(exp) - 2:
			if Alphabet.isVowel(exp[i - 1]) and Alphabet.isConsonant(exp[i]) and Alphabet.isVowel(
					exp[i + 1]) and Alphabet.isVowel(exp[i + 2]):
				gempat.append(True)
			else:
				gempat.append(False)
		elif i > 0 and exp[i - 1] == 'e' and hasRhythmicLength(word, i - 1):
			gempat.append(True)
		else:
			gempat.append(False)
	return gempat


def getStressPattern(word):
	stressPat = []
	syl = Syllables.getSyllables(word)
	rhy = getRhythmicVowelLengthPattern(word)
	ruleOne = False
	numStressed = 0

	for i in range(len(syl)):
		if ruleOne:
			numStressed += 1
		# first syllable is closed
		if i < len(syl) - 1:
			if i == 0 and Syllables.syllableMatches(syl[i], 'C'):
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# syllable is closed and previous syllable is unstress/open
			elif i > 0 and Syllables.syllableMatches(syl[i], 'C') and not stressPat[-1] and Syllables.syllableMatches(syl[i - 1], 'V'):
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# syllable contains VV
			elif Syllables.syllableMatches(syl[i], '[C]VV[C]'):
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# syllable is rhythmically lengthened
			elif rhy[i]:
				stressPat.append(True)
				ruleOne = True
				numStressed = 0
			# after finding one of the above rules, every even number syllable gets stress
			elif ruleOne and numStressed > 0 and numStressed % 2 == 0 and Syllables.syllableMatches(syl[i], 'C'):
				stressPat.append(True)
			#syllable preceeding one containing VV
			#FIXME group of OR statements below is a workaround because '[]' format doesn't work correctly in syllableMatches()
			elif i < len(syl) - 1 and (
					Syllables.syllableMatches(syl[i + 1], 'CVV') or Syllables.syllableMatches(syl[i + 1], 'VVC') or Syllables.syllableMatches(
					syl[i + 1], 'VV')):
				stressPat.append(True)
			else:
				stressPat.append(False)
		else:
			stressPat.append(False)
	return stressPat

# FIXME might be usefule to have a get[*]Text() function that also returns HTML

def getSyllableText(word):
	syl = ''
	for i in Syllables.getSyllables(word):
		syl = syl + '\t' + ''.join(i) + '\t/'
		# remove trailing '/'
	syl = syl[1:-2]
	return syl

def getStressText(word):
	stress = ''
	syls = Syllables.getSyllables(word)
	spat = getStressPattern(word)

	for i in range(len(syls)):
		if spat[i]:
			syls[i] = ''.join(syls[i]).upper()
		stress = stress + '\t' + ''.join(syls[i]) + '\t/'
	# remove trailing '/'
	stress = stress[1:-2]
	return stress


def getRhythmicVowelLengthText(word):
	rhy = ''
	syls = Syllables.getSyllables(word)
	rlen = getRhythmicVowelLengthPattern(word)

	for i in range(len(syls)):
		if rlen[i]:
			syls[i] = ''.join(syls[i]) + '\t'
		rhy = rhy + '\t' + ''.join(syls[i]) + '\t/'
	# remove trailing '/'
	rhy = rhy[1:-2]
	return rhy

def getVoicingText(word):
	voi = ''
	exp = Base.explode(word)
	vpat = getVoicingPattern(word)

	for i in range(len(exp)):
		voi = voi + exp[i] + ': '
		if vpat[i]:
			voi += '+ , '
		else:
			voi += '- , '
	# remove trailing ','
	voi = voi[:-2]
	return voi
