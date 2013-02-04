#!python
#encoding: utf-8
import unittest
import grammar

class ExplodeTests(unittest.TestCase):

	def setUp(self):
		self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
		self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']

	def test_emptyIsStop(self):
		self.assertFalse(grammar.Alphabet.isStop(''))

	def test_singleIsStop(self):
		for c in grammar.Alphabet.stops:
			self.assertTrue(grammar.Alphabet.isStop(c))
		for c in grammar.Alphabet.fricatives:
			self.assertFalse(grammar.Alphabet.isStop(c))
		for c in grammar.Alphabet.nasals:
			self.assertFalse(grammar.Alphabet.isStop(c))
		for c in grammar.Alphabet.vowels:
			self.assertFalse(grammar.Alphabet.isStop(c))

	def test_doubleIsStop(self):
		for c in grammar.Alphabet.alphabet:
			self.assertFalse(grammar.Alphabet.isStop(c+c))

	def test_emptyIsFricative(self):
		self.assertFalse(grammar.Alphabet.isFricative(''))

	def test_singleIsFricative(self):
		for c in grammar.Alphabet.stops:
			self.assertFalse(grammar.Alphabet.isFricative(c))
		for c in grammar.Alphabet.fricatives:
			self.assertTrue(grammar.Alphabet.isFricative(c))
		for c in grammar.Alphabet.nasals:
			self.assertFalse(grammar.Alphabet.isFricative(c))
		for c in grammar.Alphabet.vowels:
			self.assertFalse(grammar.Alphabet.isFricative(c))

	def test_doubleIsFricative(self):
		for c in grammar.Alphabet.alphabet:
			# some fricatives can be written double to indicate voicelessness
			if grammar.Alphabet.isADouble(c):
				self.assertTrue(grammar.Alphabet.isFricative(c+c))
			else:
				self.assertFalse(grammar.Alphabet.isFricative(c+c))

	# fricatives need to test one more letter because some fricatives can be doubled
	def test_tripleIsFricative(self):
		for c in grammar.Alphabet.alphabet:
			self.assertFalse(grammar.Alphabet.isFricative(c+c+c))

	def test_emptyIsVoicelessFricative(self):
		self.assertFalse(grammar.Alphabet.isVoicelessFricative(''))

	def test_singleIsVoicelessFricative(self):
		for c in grammar.Alphabet.voicelessFricatives:
			self.assertTrue(grammar.Alphabet.isFricative(c))
		for c in grammar.Alphabet.voicelessFricatives:
			self.assertTrue(grammar.Alphabet.isVoicelessFricative(c))
		for c in grammar.Alphabet.voicelessFricatives:
			self.assertFalse(grammar.Alphabet.isVoicedFricative(c))

if __name__ == '__main__':
	unittest.main()
