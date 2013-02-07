#!python
#encoding: utf-8
import unittest
import grammar

class ExplodeTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_empty(self):
		self.assertFalse(grammar.Alphabet.isStop(''))
		self.assertFalse(grammar.Alphabet.isADouble(''))
		self.assertFalse(grammar.Alphabet.isConsonant(''))

		self.assertFalse(grammar.Alphabet.isVowel(''))
		self.assertFalse(grammar.Alphabet.isPrimeVowel(''))

		self.assertFalse(grammar.Alphabet.isFricative(''))
		self.assertFalse(grammar.Alphabet.isVoicedFricative(''))
		self.assertFalse(grammar.Alphabet.isVoicelessFricative(''))

		self.assertFalse(grammar.Alphabet.isNasal(''))
		self.assertFalse(grammar.Alphabet.isVoicedNasal(''))
		self.assertFalse(grammar.Alphabet.isVoicelessNasal(''))

	def test_multi(self):
		for charClass in [grammar.Alphabet.stops, grammar.Alphabet.fricatives, grammar.Alphabet.nasals]:
			for c in charClass:
				self.assertFalse(grammar.Alphabet.isStop(c+c))

				self.assertFalse(grammar.Alphabet.isVowel(c+c))
				self.assertFalse(grammar.Alphabet.isPrimeVowel(c+c))

				self.assertFalse(grammar.Alphabet.isNasal(c+c))
				self.assertFalse(grammar.Alphabet.isVoicedNasal(c+c))
				self.assertFalse(grammar.Alphabet.isVoicelessNasal(c+c))

				## Special Cases for fricatives ##

				# some fricatives can be written double, but isADouble() should still return false since no letter that
				# has already been doubled can be doubled again.
				self.assertFalse(grammar.Alphabet.isADouble(c+c))
				self.assertFalse(grammar.Alphabet.isVoicedFricative(c+c))
				if grammar.Alphabet.isADouble(c):
					self.assertTrue(grammar.Alphabet.isFricative(c+c))
					self.assertTrue(grammar.Alphabet.isConsonant(c+c))
					self.assertTrue(grammar.Alphabet.isVoicelessFricative(c+c))
				else:
					self.assertFalse(grammar.Alphabet.isFricative(c+c))
					self.assertFalse(grammar.Alphabet.isConsonant(c+c))
					self.assertFalse(grammar.Alphabet.isVoicelessFricative(c+c))

	def test_triple(self):
		for charClass in [grammar.Alphabet.stops, grammar.Alphabet.fricatives, grammar.Alphabet.nasals]:
			for c in charClass:
				self.assertFalse(grammar.Alphabet.isStop(c+c+c))
				self.assertFalse(grammar.Alphabet.isADouble(c+c+c))
				self.assertFalse(grammar.Alphabet.isConsonant(c+c+c))

				self.assertFalse(grammar.Alphabet.isVowel(c+c+c))
				self.assertFalse(grammar.Alphabet.isPrimeVowel(c+c+c))

				self.assertFalse(grammar.Alphabet.isFricative(c+c+c))
				self.assertFalse(grammar.Alphabet.isVoicedFricative(c+c+c))
				self.assertFalse(grammar.Alphabet.isVoicelessFricative(c+c+c))

				self.assertFalse(grammar.Alphabet.isNasal(c+c+c))
				self.assertFalse(grammar.Alphabet.isVoicedNasal(c+c+c))
				self.assertFalse(grammar.Alphabet.isVoicelessNasal(c+c+c))

	def test_singleIsStop(self):
		for c in grammar.Alphabet.stops:
			self.assertTrue(grammar.Alphabet.isStop(c))
			self.assertFalse(grammar.Alphabet.isADouble(c))
			self.assertTrue(grammar.Alphabet.isConsonant(c))

			self.assertFalse(grammar.Alphabet.isVowel(c))
			self.assertFalse(grammar.Alphabet.isPrimeVowel(c))

			self.assertFalse(grammar.Alphabet.isFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicedFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicelessFricative(c))

			self.assertFalse(grammar.Alphabet.isNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicedNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicelessNasal(c))

	# isFricative() and isNasal() are tested as a part of testing voiceless and voiced versions

	def test_singleIsVoicelessFricative(self):
		for c in grammar.Alphabet.voicelessFricatives:
			self.assertFalse(grammar.Alphabet.isStop(c))
			self.assertFalse(grammar.Alphabet.isADouble(c))
			self.assertTrue(grammar.Alphabet.isConsonant(c))

			self.assertFalse(grammar.Alphabet.isVowel(c))
			self.assertFalse(grammar.Alphabet.isPrimeVowel(c))

			self.assertTrue(grammar.Alphabet.isFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicedFricative(c))
			self.assertTrue(grammar.Alphabet.isVoicelessFricative(c))

			self.assertFalse(grammar.Alphabet.isNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicedNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicelessNasal(c))

	def test_singleIsVoicedFricative(self):
		for c in grammar.Alphabet.voicedFricatives:
			self.assertFalse(grammar.Alphabet.isStop(c))
			# FIXME a voiced fricative could/could not be double. need way to check
			#self.assertFalse(grammar.Alphabet.isADouble(c))
			self.assertTrue(grammar.Alphabet.isConsonant(c))

			self.assertFalse(grammar.Alphabet.isVowel(c))
			self.assertFalse(grammar.Alphabet.isPrimeVowel(c))

			self.assertTrue(grammar.Alphabet.isFricative(c))
			self.assertTrue(grammar.Alphabet.isVoicedFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicelessFricative(c))

			self.assertFalse(grammar.Alphabet.isNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicedNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicelessNasal(c))

	def test_singleIsVoicelessNasals(self):
		for c in grammar.Alphabet.voicelessNasals:
			self.assertFalse(grammar.Alphabet.isStop(c))
			self.assertFalse(grammar.Alphabet.isADouble(c))
			self.assertTrue(grammar.Alphabet.isConsonant(c))

			self.assertFalse(grammar.Alphabet.isVowel(c))
			self.assertFalse(grammar.Alphabet.isPrimeVowel(c))

			self.assertFalse(grammar.Alphabet.isFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicedFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicelessFricative(c))

			self.assertTrue(grammar.Alphabet.isNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicedNasal(c))
			self.assertTrue(grammar.Alphabet.isVoicelessNasal(c))

	def test_singleIsVoicedNasals(self):
		for c in grammar.Alphabet.voicedNasals:
			self.assertFalse(grammar.Alphabet.isStop(c))
			self.assertFalse(grammar.Alphabet.isADouble(c))
			self.assertTrue(grammar.Alphabet.isConsonant(c))

			self.assertFalse(grammar.Alphabet.isVowel(c))
			self.assertFalse(grammar.Alphabet.isPrimeVowel(c))

			self.assertFalse(grammar.Alphabet.isFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicedFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicelessFricative(c))

			self.assertTrue(grammar.Alphabet.isNasal(c))
			self.assertTrue(grammar.Alphabet.isVoicedNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicelessNasal(c))

	def test_singleIsVowel(self):
		for c in grammar.Alphabet.vowels:
			self.assertFalse(grammar.Alphabet.isStop(c))
			self.assertFalse(grammar.Alphabet.isADouble(c))
			self.assertFalse(grammar.Alphabet.isConsonant(c))

			self.assertTrue(grammar.Alphabet.isVowel(c))
			if c == 'e':
				self.assertFalse(grammar.Alphabet.isPrimeVowel(c))
			else:
				self.assertTrue(grammar.Alphabet.isPrimeVowel(c))

			self.assertFalse(grammar.Alphabet.isFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicedFricative(c))
			self.assertFalse(grammar.Alphabet.isVoicelessFricative(c))

			self.assertFalse(grammar.Alphabet.isNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicedNasal(c))
			self.assertFalse(grammar.Alphabet.isVoicelessNasal(c))


if __name__ == '__main__':
	unittest.main()
