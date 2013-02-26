#!python
#encoding: utf-8
""" Classes of base endings:
Class I:	single prime vowel
Class II:	double prime vowel
Class III:	ends with an 'e' not preceded by 't'
Class IV:	'te' ending
Class IVa:	fricative + 'te'
Class IVb:	vowel + 'te'
Class IVc:	contains a '°' when listed (eg. "kiircete-°");
		also includes bases expanded from the postbase ":(ng)ite-°" (eg. "nerenrite-°"
Class V:	single or double vowel + 'r' (nouns only)
Class VI:	ends in consonant and not in Class V

*See section 2.3 in Yup'ik Eskimo Grammar, Irene Reed """
import Alphabet

# FIXME need to figure out how to properly explode \' using Word.apostrophePurpose()
# FIXME need to add voiceless nasals to test functions
def explode(word):
	""" split the word into it's letters. this makes working with letters made up
	of more than one character (eg. 'll' or 'ng' a whole lot easier """
	#FIXME should \' be treated as a separate letter or combined with the letter
	# it is telling to geminate (eg. r') or completely omited in the output
	#FIXME needs to throw exception if incorrect character found
	exploded = []

	for i in word:
		# test if a letter is a valid doubled letter or is 'ng'
		if len(exploded) > 0 and Alphabet.isADouble(i) and exploded[-1] == i:
			exploded[-1] = i + i
		elif len(exploded) > 0 and exploded[-1] == 'n' and i == 'g':
			exploded[-1] = 'ng'
		elif len(exploded) > 0 and exploded[-1] == 'ń'  and i == 'g':
			exploded[-1] = 'ńg'
		elif len(exploded) > 0 and exploded[-1] + i == 'ḿ':
			exploded[-1] = 'ḿ'
		elif len(exploded) > 0 and exploded[-1] + i == 'ń':
			exploded[-1] = 'ń'
		elif len(exploded) > 0 and (i == '\xe1' or i == '\xb8' or i == '\xbf' or i == '\xc5' or i == '\x84'):
			if (exploded[-1] == '\xe1' or exploded[-1] == '\xb8' or exploded[-1] == '\xbf' or exploded[-1] == '\xc5' or exploded[-1] == '\x84'):
				exploded[-1] = exploded[-1] + i
			else:
				exploded.append(i)
		else:
			exploded.append(i)
	return exploded


def isClassI(base):
	""" word ends in a single prime vowel """
	exp = explode(base)

	isClass = False
	if len(exp) > 1:
		if Alphabet.isPrimeVowel(exp[-1]) and not Alphabet.isPrimeVowel(exp[-2]):
			isClass = True
	return isClass


def isClassII(base):
	""" word ends in 2 prime vowels """
	exp = explode(base)

	isClass = False
	if len(exp) > 1:
		if Alphabet.isPrimeVowel(exp[-1]) and Alphabet.isPrimeVowel(exp[-2]):
			isClass = True
	return isClass


def isClassIII(base):
	""" words that end in 'e', but do not end in 'te' """
	exp = explode(base)

	isClass = False
	if len(exp) > 1:
		if exp[-1] == 'e' and not exp[-2] == 't':
			isClass = True
	return isClass


def isClassIV(base):
	""" words that end in 'te' """
	exp = explode(base)

	isClass = False
	if len(exp) > 1:
		if exp[-1] == 'e' and exp[-2] == 't':
			isClass = True
	return isClass


def isClassIVa(base):
	""" word ends in a fricitive followed by 'te' """
	exp = explode(base)

	isClass = False
	if len(exp) > 2:
		if isClassIV(base) and Alphabet.isFricative(exp[-3]):
			isClass = True
	return isClass


def isClassIVb(base):
	""" words that end with a vowel followed by 'te' """
	exp = explode(base)

	isClass = False
	if len(exp) > 2:
		if isClassIV(base) and Alphabet.isVowel(exp[-3]):
			isClass = True
	return isClass


def isClassIVc(base):
	""" contains a '°' when listed (eg. 'kiircete-°');
	 also includes bases expanded from the postbase ':(ng)ite-°' (eg. 'nerenrite-°' """
	#TODO incomplete
	isClass = False
	#if isClassIV(base) and isVowel(base[-3]):
	#isClass = True
	#print("Base is a Class IVc word")
	return isClass


def isClassV(base):
	#FIXME does not check if noun
	""" nouns only: ends with 1 or 2 vowels followed by 'r' """
	exp = explode(base)

	#FIXME: does not check if word is a noun or words marked with '*'
	isClass = False
	if len(exp) > 1:
		if exp[-1] == 'r' and Alphabet.isVowel(exp[-2]):
			isClass = True
	return isClass


def isClassVI(base):
	""" all words ending in a consonant and that are not Class V """
	exp = explode(base)

	isClass = False
	if len(exp) > 1:
		if Alphabet.isConsonant(exp[-1]) and not isClassV(base):
			isClass = True
	return isClass

#FIXME should throw error if not in a correct class
def getClass(word):
	""" returns the roman numeral representation of the class """
	classnum = ''
	if isClassI(word):
		classnum = 'I'
	elif isClassII(word):
		classnum = 'II'
	elif isClassIII(word):
		classnum = 'III'
	elif isClassIV(word):
		classnum = 'IV'
		if isClassIVa(word):
			classnum = 'IVa'
		elif isClassIVb(word):
			classnum = 'IVb'
		elif isClassIVc(word):
			classnum = 'IVc'
	elif isClassV(word):
		classnum = 'V'
	elif isClassVI(word):
		classnum = 'VI'
	else:
		print('ERROR: incorrect class!')


def getClassAsInt(word):
	classnum = -1
	if isClassI(word):
		classnum = 1
	elif isClassII(word):
		classnum = 2
	elif isClassIII(word):
		classnum = 3
	elif isClassIV(word):
		classnum = 4
	elif isClassV(word):
		classnum = 5
	elif isClassVI(word):
		classnum = 6
	else:
		#FIXME, when would this get executed, and should it throw an exception?
		print('ERROR: incorrect class!')
	return classnum


def debugClasses(w):
	""" print out which classes a word was detected as being a part of """
	if isClassI(w):
		print("Base is a Class I word")
	if isClassII(w):
		print("Base is a Class II word")
	if isClassIII(w):
		print("Base is a Class III word")
	if isClassIV(w):
		print("Base is a Class IV word")
	if isClassIVa(w):
		print("Base is a Class IVa word")
	if isClassIVb(w):
		print("Base is a Class IVb word")
	if isClassIVc(w):
		print("Base is a Class IVc word")
	if isClassV(w):
		print("Base is a Class V word")
	if isClassVI(w):
		print("Base is a Class VI word")
