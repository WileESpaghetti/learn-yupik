#!python
#encoding: utf-8
import unittest
import grammar

class SyllableTest(unittest.TestCase):
	# TODO might be good to do some permutations of letters and test splitting
	# TODO write some tests that are supposed to fail
	# TODO tests for actual Yup'ik words

	def setUp(self):
		self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
		self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']
		arnaq = {'word':'arnaq','syllables':[['a','r'],['n','a','q']]}
		nuna = {'word':'nuna','syllables':[['n','u'],['n','a']]}
		talliq = {'word':'talliq','syllables':[['t','a'],['ll','i','q']]}
		angun = {'word':'angun','syllables':[['a'],['ng','u','n']]}
		neruq = {'word':'ner\'uq','syllables':[['n','e','r'],['\'','u','q']]}

		# \' used to divide words instead of indicate gemination[
		# FIXME not sure if need to ignore \' not used for gemination or do can'/get like in yeg pg. 12
		#canget = {'word':'can\'get','syllables':[['c','a','n'],['g','e','t']]}
		#itgaq = {'word':'it\'gaq','syllables':[['i','t'],['g','a','q']]}

		# long words
		elaturraq = {'word':'elaturraq','syllables':[['e'],['l','a'],['t','u'],['rr','a','q']]}
		angyalingaicugnarquq = {'word':'angyalingaicugnarquq', 'syllables':[['a','ng'],['y','a'],['l','i'],['ng','a','i'],['c','u','g'],['n','a','r'],['q','u','q']]}
		miteqatartuq = {'word':'mit\'eqatartuq', 'syllables':[['m','i','t'],['\'','e'],['q','a'],['t','a','r'],['t','u','q']]}
		#self.testWords = [arnaq, nuna,talliq, angun,neruq,canget,itgaq,elaturraq]
		self.testWords = [arnaq, nuna,talliq, angun,neruq,elaturraq,angyalingaicugnarquq,miteqatartuq]

	def test_getSyllables(self):
		for w in self.testWords:
			self.assertEqual(grammar.Word.getSyllables(w['word'],), w['syllables'])

if __name__ == '__main__':
	unittest.main()
