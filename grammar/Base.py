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
import Alphabet, Word

# FIXME need to figure out how to properly explode \' using Word.apostrophePurpose()
# FIXME need to add voiceless nasals to test functions
def explode(word):
	""" split the word into it's letters. this makes working with letters made up
	of more than one character (eg. 'll' or 'ng' a whole lot easier """
	#FIXME should \' be treated as a separate letter or combined with the letter
	# it is telling to geminate (eg. r') or completely omited in the output
	#FIXME needs to throw exception if incorrect character found
	exploded = []

	for i in range(len(word)):
		dl = False
		for l in Alphabet.doubled:
			if word[i] == l:
				dl = True

		# test if a letter is a valid doubled letter or is 'ng'
		if i > 0 and dl and exploded[-1] == word[i]:
			exploded[-1] = word[i] + word[i]
		elif i > 0 and (exploded[-1] == 'n' or exploded[-1] == 'ń') and word[i] == 'g':
			exploded[-1] = 'ng'
		else:
			exploded.append(word[i])

	return exploded

def isClassI(base):
	""" word ends in a single prime vowel """
	isClass = False
	if Alphabet.isPrimeVowel(base[-1]) and not Alphabet.isPrimeVowel(base[-2]):
		isClass = True
	return isClass

def isClassII(base):
	""" word ends in 2 prime vowels """
	isClass = False
	if Alphabet.isPrimeVowel(base[-1]) and Alphabet.isPrimeVowel(base[-2]):
		isClass = True
	return isClass

def isClassIII(base):
	""" words that end in 'e', but do not end in 'te' """
	isClass = False
	if base[-1] =='e' and not base[-2] == 't':
		isClass = True
	return isClass

def isClassIV(base):
	""" words that end in 'te' """
	isClass = False
	if base[-1] =='e' and base[-2] == 't':
		isClass = True
	return isClass

def isClassIVa(base):
	""" word ends in a fricitive followed by 'te' """
	isClass = False
	if isClassIV(base) and Alphabet.isFricative(base[-3]):
		isClass = True
	return isClass

def isClassIVb(base):
	""" words that end with a vowel followed by 'te' """
	isClass = False
	if isClassIV(base) and Alphabet.isVowel(base[-3]):
		isClass = True
	return isClass

def isClassIVc(base):
	""" contains a '°' when listed (eg. 'kiircete-°'); also includes bases expanded from the postbase ':(ng)ite-°' (eg. 'nerenrite-°' """
	#TODO incomplete
	isClass = False
	#if isClassIV(base) and isVowel(base[-3]):
		#isClass = True
		#print("Base is a Class IVc word")
	return isClass

def isClassV(base):
	""" nouns only: ends with 1 or 2 vowels followed by 'r' """
	#FIXME: does not check if word is a noun or words marked with '*'
	isClass = False
	if base[-1] == 'r' and Alphabet.isVowel(base[-2]):
		isClass = True
	return isClass

def isClassVI(base):
	""" all words ending in a consonant and that are not Class V """
	isClass = False
	if not Alphabet.isVowel(base[-1]) and not isClassV(base):
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
		print('ERROR: incorrect class!')
		#FIXME, when would this get executed, and should it throw an exception?
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
