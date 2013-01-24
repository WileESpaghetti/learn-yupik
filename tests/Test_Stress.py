#!python
#encoding: utf-8
import unittest
import grammar

class RhythmicStressTests(unittest.TestCase):
	# TODO might be good to do some permutations of letters and test splitting
	# TODO write some tests that are supposed to fail
	# TODO tests for actual Yup'ik words
	# TODO need to test exploding for words that do not cause gemmination

	def setUp(self):
		self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
		self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']
		angyarpaliyugngayugnarquq = {'stress':[True, False, False,True,False, False,True,False,False], 'word':'angyarpaliyugngayugnarquq'}
		nerciqsugnarquq = {'stress':[True,False,True,False,False], 'word':'nerciqsugnarquq'}
		nerciqsugnarqaa = {'stress':[True,False,True,True,False], 'word':'nerciqsugnarqaa'}
		self.testWords = [angyarpaliyugngayugnarquq,nerciqsugnarqaa, nerciqsugnarquq]

	def test_gemminationWords(self):
		for tw in self.testWords:
			self.assertEqual(tw['stress'],grammar.Word.getStressPattern(tw['word']))

if __name__ == '__main__':
	unittest.main()
