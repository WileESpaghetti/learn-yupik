#!python
#encoding: utf-8
import unittest
import grammar

class ParenLetterTest(unittest.TestCase):
    # TODO might be good to do some permutations of letters and test splitting
    # TODO write some tests that are supposed to fail
    # TODO tests for actual Yup'ik words

    def setUp(self):
        self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
        self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']

    def test_explodeSingleLetters(self):
        for c in grammar.Alphabet.alphabet:
            self.assertEqual(grammar.Base.explode(c),[c])

    def test_explodeAlphabet(self):
        self.assertEqual(grammar.Base.explode(self.alphabet),self.alphExp)
        #self.assertEqual(grammar.Base.explode(''),[''])

if __name__ == '__main__':
    unittest.main()
