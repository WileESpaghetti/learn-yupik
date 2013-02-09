#!python
#encoding: utf-8
import unittest
import grammar

class RhythmicLengthTests(unittest.TestCase):
    # TODO might be good to do some permutations of letters and test splitting
    # TODO write some tests that are supposed to fail
    # TODO tests for actual Yup'ik words
    # TODO need to test exploding for words that do not cause gemmination

    def setUp(self):
        self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
        self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']
        tekituq = {'length':[False, True, False], 'word': 'tekituq'}
        pissuqatalliniluni = {'length': [False, True, False, True, False, True, False, False], 'word':'pissuqatalliniluni'}
        miteqatalliniluni = {'length':[False, False,True, False,True,False,True,False], 'word':'mit\'eqatalliniluni'}
        nalluyagucaqunaku = {'length':[False, True, False, True, False,True, False, False],'word':'nalluyagucaqunaku'}
        qayaliqataraqama = {'length':[False,True,False,True,False,True,False,False],'word':'qayaliqataraqama'}
        angyaligataraqama = {'length':[False,False,True,False,True,False,True,False],'word':'angyaliqataraqama'}
        qayaliciqngatuten = {'length':[False,True,False,False,False,True,False], 'word':'qayaliciqngatuten'}
        quyana = {'length':[False,True,False], 'word':'quyana'}
        self.testWords = [tekituq,pissuqatalliniluni,miteqatalliniluni,qayaliqataraqama,nalluyagucaqunaku,angyaligataraqama,qayaliciqngatuten,quyana]

    def test_rhythmicLengthTestWords(self):
        for tw in self.testWords:
            self.assertEqual(tw['length'], grammar.Word.getRhythmicVowelLengthPattern(tw['word']))

if __name__ == '__main__':
    unittest.main()
