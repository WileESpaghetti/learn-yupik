#!python
#encoding: utf-8
import unittest
import grammar


class ClassDetectionTests(unittest.TestCase):

	def setUp(self):
		self.allButPrime = set(grammar.Alphabet.alphabet) - set(grammar.Alphabet.primeVowels)

	# bases require at least 2 characters to be properly detected
	def test_tooFewCharacters(self):
		self.assertFalse(grammar.Base.isClassI(''))
		self.assertFalse(grammar.Base.isClassII(''))
		self.assertFalse(grammar.Base.isClassIII(''))
		self.assertFalse(grammar.Base.isClassIV(''))
		self.assertFalse(grammar.Base.isClassIVa(''))
		self.assertFalse(grammar.Base.isClassIVb(''))
		self.assertFalse(grammar.Base.isClassIVc(''))
		self.assertFalse(grammar.Base.isClassV(''))
		self.assertFalse(grammar.Base.isClassVI(''))

		for c in grammar.Alphabet.alphabet:
			self.assertFalse(grammar.Base.isClassI(c))
			self.assertFalse(grammar.Base.isClassII(c))
			self.assertFalse(grammar.Base.isClassIII(c))
			self.assertFalse(grammar.Base.isClassIV(c))
			self.assertFalse(grammar.Base.isClassIVa(c))
			self.assertFalse(grammar.Base.isClassIVb(c))
			self.assertFalse(grammar.Base.isClassIVc(c))
			self.assertFalse(grammar.Base.isClassV(c))
			self.assertFalse(grammar.Base.isClassVI(c))

	def test_BaseI(self):
		for p in self.allButPrime:
			for c in grammar.Alphabet.primeVowels:
				self.assertTrue(grammar.Base.isClassI(p + c))

		# Base I words can not end in 2 prime vowels
		for p in grammar.Alphabet.primeVowels:
			for c in grammar.Alphabet.primeVowels:
				self.assertFalse(grammar.Base.isClassI(p + c))

		# Base I words have to end in a prime vowel
		for p in grammar.Alphabet.alphabet:
			for c in self.allButPrime:
				self.assertFalse(grammar.Base.isClassI(p + c))

	def test_BaseII(self):
		for p in grammar.Alphabet.primeVowels:
			for c in grammar.Alphabet.primeVowels:
				self.assertTrue(grammar.Base.isClassII(p + c))

		for p in self.allButPrime:
			for c in grammar.Alphabet.primeVowels:
				self.assertFalse(grammar.Base.isClassII(p + c))

		for p in grammar.Alphabet.alphabet:
			for c in self.allButPrime:
				self.assertFalse(grammar.Base.isClassII(p + c))

	def test_BaseIII(self):
		for p in set(grammar.Alphabet.alphabet) - set(['t']):
			self.assertTrue(grammar.Base.isClassIII(p + 'e'))

		for p in grammar.Alphabet.alphabet:
			for c in set(grammar.Alphabet.alphabet) - set(['e']):
				self.assertFalse(grammar.Base.isClassIII(p + c))

	def test_BaseIV(self):
		self.assertTrue(grammar.Base.isClassIV('te'))

		for p in set(grammar.Alphabet.alphabet) - set(['t']):
			for c in grammar.Alphabet.alphabet:
				self.assertFalse(grammar.Base.isClassIV(p + c))

		for p in grammar.Alphabet.alphabet:
			for c in set(grammar.Alphabet.alphabet) - set(['e']):
				self.assertFalse(grammar.Base.isClassIV(p + c))

	def test_BaseIVa(self):
		for p in grammar.Alphabet.fricatives:
			self.assertTrue(grammar.Base.isClassIVa(p + 'te'))

		# to catagorize as Class IVa it requires 3 characters
		for p in grammar.Alphabet.alphabet:
			for c in grammar.Alphabet.alphabet:
				self.assertFalse(grammar.Base.isClassIVa(p + c))

		for p in set(grammar.Alphabet.alphabet) - set(grammar.Alphabet.fricatives):
			self.assertFalse(grammar.Base.isClassIVa(p + 'te'))

		for i in grammar.Alphabet.alphabet:
			for p in set(grammar.Alphabet.alphabet) - set(['t']):
				for c in grammar.Alphabet.alphabet:
					self.assertFalse(grammar.Base.isClassIVa(i + p + c))

		for i in grammar.Alphabet.alphabet:
			for p in grammar.Alphabet.alphabet:
				for c in set(grammar.Alphabet.alphabet) - set(['e']):
					self.assertFalse(grammar.Base.isClassIVa(i + p + c))

	def test_ClassIVb(self):
		for p in grammar.Alphabet.vowels:
			self.assertTrue(grammar.Base.isClassIVb(p + 'te'))

		# to catagorize as Class IVa it requires 3 characters
		for p in grammar.Alphabet.alphabet:
			for c in grammar.Alphabet.alphabet:
				self.assertFalse(grammar.Base.isClassIVb(p + c))

		for p in set(grammar.Alphabet.alphabet) - set(grammar.Alphabet.vowels):
			self.assertFalse(grammar.Base.isClassIVb(p + 'te'))

		for i in grammar.Alphabet.alphabet:
			for p in set(grammar.Alphabet.alphabet) - set(['t']):
				for c in grammar.Alphabet.alphabet:
					self.assertFalse(grammar.Base.isClassIVb(i + p + c))

		for i in grammar.Alphabet.alphabet:
			for p in grammar.Alphabet.alphabet:
				for c in set(grammar.Alphabet.alphabet) - set(['e']):
					self.assertFalse(grammar.Base.isClassIVb(i + p + c))

	#FIXME IVc not implemented

	#FIXME without noun detection isClassV() will give some false positives
	#def test_ClassV(self):
		#for c in grammar.Alphabet.vowels:
			#self.assertTrue(grammar.Base.isClassV(c + 'r'))

		#for p in set(grammar.Alphabet.alphabet) - set(grammar.Alphabet.vowels):
			#for c in grammar.Alphabet.alphabet:
				#self.assertFalse(grammar.Base.isClassV(p + c))

	# FIXME this will give false positives because it depends on isClassV() which needs noun detection
	#def test_ClassVI(self):
		#for p in grammar.Alphabet.alphabet:
			#for c in grammar.Alphabet.vowels:
				#self.assertFalse(grammar.Base.isClassVI(p + c))

		#for p in grammar.Alphabet.alphabet:
			#for c in grammar.Alphabet.consonants:
				#print(p+c)
				#print(grammar.Base.isClassVI(p+c))
				#if grammar.Base.isClassV(p + c) and False:
					#self.assertFalse(grammar.Base.isClassVI(p + c))
				#else:
					#self.assertTrue(grammar.Base.isClassVI(p + c))

if __name__ == '__main__':
	unittest.main()
