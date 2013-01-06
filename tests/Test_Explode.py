#!python
#encoding: utf-8
import unittest
import grammar

class ExplodeTests(unittest.TestCase):
	# TODO might be good to do some permutations of letters and test splitting
	# TODO write some tests that are supposed to fail
	# TODO tests for actual Yup'ik words
	# TODO need to test exploding for words that do not cause gemmination

	def setUp(self):
		self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
		self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']

	def test_explodeSingleLetters(self):
		for c in grammar.Word.alphabet:
			self.assertEqual(grammar.Base.explode(c),[c])

	def test_explodeDoubleLetters(self):
		for c in grammar.Word.alphabet:
			dl = False
			for l in grammar.Word.doubled:
				if c == l:
					dl = True
			if not dl:
				self.assertEqual(grammar.Base.explode(c + c),[c,c])
			else:
				self.assertEqual(grammar.Base.explode(c + c),[c + c])

	def test_explodeTripleLetters(self):
		for c in grammar.Word.alphabet:
			dl = False
			for l in grammar.Word.doubled:
				if c == l:
					dl = True
			if not dl:
				self.assertEqual(grammar.Base.explode(c + c + c),[c,c,c])
			else:
				self.assertEqual(grammar.Base.explode(c + c + c),[c + c,c])

	def test_explodeFourLetters(self):
		for c in grammar.Word.alphabet:
			dl = False
			for l in grammar.Word.doubled:
				if c == l:
					dl = True
			if not dl:
				self.assertEqual(grammar.Base.explode(c + c + c + c),[c,c,c,c])
			else:
				self.assertEqual(grammar.Base.explode(c + c + c + c),[c + c,c + c])

	def test_explodeFiveLetters(self):
		for c in grammar.Word.alphabet:
			dl = False
			for l in grammar.Word.doubled:
				if c == l:
					dl = True
			if not dl:
				self.assertEqual(grammar.Base.explode(c + c + c + c + c),[c,c,c,c,c])
			else:
				self.assertEqual(grammar.Base.explode(c + c + c + c + c),[c + c,c + c, c])

	def test_explodeAlphabet(self):
		self.assertEqual(grammar.Base.explode(self.alphabet),self.alphExp)
		#self.assertEqual(grammar.Base.explode(''),[''])

if __name__ == '__main__':
	unittest.main()