#!python
#encoding: utf-8
import unittest
import grammar

class SyllableTest(unittest.TestCase):
	# TODO might be good to do some permutations of letters and test splitting
	# TODO write some tests that are supposed to fail
	# TODO tests for actual Yup'ik words
	# TODO add more test words
		#te/ki/tuq
		#pi/ssu/qa/ta/lli/ni/lu/ni
		#mit/'e/qa/ta/lli/ni/lu/ni
		#ang/yar/pa/li/yug/nga/yug/nar/quq
		#ner/ciq/sug/nar/quq

	def setUp(self):
		self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
		self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']
		arnaq = {'word':'arnaq','syllables':[['a','r'],['n','a','q']], 'count':2}
		nuna = {'word':'nuna','syllables':[['n','u'],['n','a']], 'count':2}
		talliq = {'word':'talliq','syllables':[['t','a'],['ll','i','q']], 'count':2}
		angun = {'word':'angun','syllables':[['a'],['ng','u','n']], 'count':2}
		neruq = {'word':'ner\'uq','syllables':[['n','e','r'],['\'','u','q']], 'count':2}

		# \' used to divide words instead of indicate gemination[
		# FIXME not sure if need to ignore \' not used for gemination or do can'/get like in yeg pg. 12
		#canget = {'word':'can\'get','syllables':[['c','a','n'],['g','e','t']], 'count':2}
		#itgaq = {'word':'it\'gaq','syllables':[['i','t'],['g','a','q']], 'count':2}

		# long words
		elaturraq = {'word':'elaturraq','syllables':[['e'],['l','a'],['t','u'],['rr','a','q']], 'count':4}
		angyalingaicugnarquq = {'word':'angyalingaicugnarquq', 'syllables':[['a','ng'],['y','a'],['l','i'],['ng','a','i'],['c','u','g'],['n','a','r'],['q','u','q']], 'count':7}
		miteqatartuq = {'word':'mit\'eqatartuq', 'syllables':[['m','i','t'],['\'','e'],['q','a'],['t','a','r'],['t','u','q']], 'count':5}
		#self.testWords = [arnaq, nuna,talliq, angun,neruq,canget,itgaq,elaturraq]
		self.testWords = [arnaq, nuna,talliq, angun,neruq,elaturraq,angyalingaicugnarquq,miteqatartuq]

	def test_getSyllables(self):
		for w in self.testWords:
			self.assertEqual(grammar.Word.getSyllables(w['word'],), w['syllables'])

	def test_syllableCount(self):
		for i in self.testWords:
			self.assertEqual(i['count'], grammar.Word.syllableCount(i['word']))

	# FIXME need to work out how []'s are handled and test that those work
	def test_matchZeroLength(self):
		self.assertFalse(grammar.Word.syllableMatches('','C'))
		self.assertFalse(grammar.Word.syllableMatches('','V'))

	def test_lmatchZeroLength(self):
		self.assertFalse(grammar.Word.lSyllableMatches('','C'))
		self.assertFalse(grammar.Word.lSyllableMatches('','V'))

	def test_matchSingleVowel(self):
		for i in grammar.Alphabet.vowels:
			self.assertTrue(grammar.Word.syllableMatches(i,'V'))
			self.assertFalse(grammar.Word.syllableMatches(i,'C'))

	def test_matchSingleConsonant(self):
		for i in grammar.Alphabet.consonants:
			self.assertTrue(grammar.Word.syllableMatches(i,'C'))
			self.assertFalse(grammar.Word.syllableMatches(i,'V'))

	def test_lmatchSingleVowel(self):
		for i in grammar.Alphabet.vowels:
			self.assertTrue(grammar.Word.lSyllableMatches(i,'V'))
			self.assertFalse(grammar.Word.lSyllableMatches(i,'C'))

	def test_matchSingleConsonant(self):
		for i in grammar.Alphabet.consonants:
			self.assertTrue(grammar.Word.lSyllableMatches(i,'C'))
			self.assertFalse(grammar.Word.lSyllableMatches(i,'V'))

if __name__ == '__main__':
	unittest.main()
