#!python
#encoding: utf-8
import unittest
import grammar

class AutoGemminationTests(unittest.TestCase):
    # TODO might be good to do some permutations of letters and test splitting
    # TODO write some tests that are supposed to fail
    # TODO tests for actual Yup'ik words
    # TODO need to test exploding for words that do not cause gemmination

    def setUp(self):
        self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
        self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']
        aciani = {'gem':[False,True,False, False, False, False], 'word':'aciani'}
        nuniini = {'gem':[False,False,True, False, False, False,False], 'word':'nuniini'}
        tekiituq = {'gem':[False,False,True, False, False, False,False,False], 'word':'tekiituq'}
        tekituq = {'gem':[False,False,False, False, False,False,False], 'word':'tekituq'}
        tumemi = {'gem':[False,False,False, False, True, False], 'word':'tumemi'}
        self.testWords = [aciani,nuniini,tekiituq, tekituq, tumemi]

    def test_gemminationWords(self):
        for tw in self.testWords:
            self.assertEqual(tw['gem'],grammar.Word.getAutoGemminationPattern(tw['word']))

if __name__ == '__main__':
    unittest.main()
