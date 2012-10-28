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
import Vowel, Consonant

def isClassI(base):
	isClass = False
	if Vowel.isPrimeVowel(base[-1]) and not Vowel.isPrimeVowel(base[-2]):
		isClass = True
	return isClass

def isClassII(base):
	isClass = False
	if Vowel.isPrimeVowel(base[-1]) and Vowel.isPrimeVowel(base[-2]):
		isClass = True
	return isClass

def isClassIII(base):
	isClass = False
	if base[-1] =='e' and not base[-2] == 't':
		isClass = True
	return isClass

def isClassIV(base):
	isClass = False
	if base[-1] =='e' and base[-2] == 't':
		isClass = True
	return isClass

def isClassIVa(base):
	isClass = False
	if isClassIV(base) and Consonant.isFricative(base[-3]):
		isClass = True
	return isClass

def isClassIVb(base):
	isClass = False
	if isClassIV(base) and Vowel.isVowel(base[-3]):
		isClass = True
	return isClass

def isClassIVc(base):
	isClass = False
	#if isClassIV(base) and isVowel(base[-3]):
		#isClass = True
		#print("Base is a Class IVc word")
	return isClass

def isClassV(base):
	#FIXME: does not check if word is a noun or words marked with '*'
	isClass = False
	if base[-1] == 'r' and Vowel.isVowel(base[-2]):
		isClass = True
	return isClass

def isClassVI(base):
	isClass = False
	if not Vowel.isVowel(base[-1]) and not isClassV(base):
		isClass = True
	return isClass

def debugClasses(w):
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
