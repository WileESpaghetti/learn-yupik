#!python
#encoding: utf-8

vowels = ['a', 'e', 'i', 'u']
primeVowels = ['a', 'i', 'u']

def isVowel(c):
	isV = False
	for v in vowels:
		if c == v:
			isV = True
			break
	return isV

def isPrimeVowel(c):
	isPrime = False
	for v in primeVowels:
		if c == v:
			isPrime = True
			break
	return isPrime
