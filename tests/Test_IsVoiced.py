#!python
#encoding: utf-8
import unittest
import grammar

class IsVoicedTests(unittest.TestCase):
    # TODO might be good to do some permutations of letters and test splitting
    # TODO write some tests that are supposed to fail
    # TODO tests for actual Yup'ik words
    # TODO need to test exploding for words that do not cause gemmination

    def setUp(self):
        self.alphabet = '\'acegggiklllmnngpqrrrssstuvvvwy'
        self.alphExp = ['\'','a','c','e','gg','g','i','k','ll','l','m','n','ng','p','q','rr','r','ss','s','t','u','vv','v','w','y']

    def test_singleVoicedFricative(self):
        for c in grammar.Alphabet.voicedFricatives:
            if c != 's' and c != 'r':
                self.assertTrue(grammar.Word.isVoiced(c,0))
            else:
                self.assertFalse(grammar.Word.isVoiced(c,0))

    def test_singleVoicelessFricative(self):
        for c in grammar.Alphabet.voicelessFricatives:
            self.assertFalse(grammar.Word.isVoiced(c,0))

    def test_singleVoicedNasal(self):
        for c in grammar.Alphabet.voicedNasals:
            self.assertTrue(grammar.Word.isVoiced(c,0))

#FIXME currently fails due to explode not processing the unicode chars correctly
    def test_singleVoicelessNasal(self):
        for c in grammar.Alphabet.voicelessNasals:
            self.assertFalse(grammar.Word.isVoiced(c,0))

#FIXME need test to make sure other letters don't cause devoicing
    def test_afterVoicelessFricative(self):
        for f in grammar.Alphabet.voicelessFricatives:
            for c in grammar.Alphabet.voicedFricatives:
                self.assertFalse(grammar.Word.isVoiced(f+c, 1))

#FIXME need test to make sure other letters don't cause devoicing
    def test_afterStop(self):
        for s in grammar.Alphabet.stops:
            for c in grammar.Alphabet.voicedFricatives:
                self.assertFalse(grammar.Word.isVoiced(s+c, 1))

#FIXME need test to make sure other letters don't cause devoicing
#FIXME need to test boundries
    def test_beforeStop(self):
        for c in grammar.Alphabet.voicedFricatives:
            for s in grammar.Alphabet.stops:
                print(c+s)
                self.assertFalse(grammar.Word.isVoiced(c+s, 0))

#FIXME need test to make sure other letters don't cause devoicing
    def test_nAfterVoicelessFricative(self):
        for f in grammar.Alphabet.voicelessFricatives:
            for n in grammar.Alphabet.voicedNasals:
                self.assertFalse(grammar.Word.isVoiced(f+n, 1))

#FIXME need test to make sure other letters don't cause devoicing
    def test_nAfterStop(self):
        for s in grammar.Alphabet.stops:
            for n in grammar.Alphabet.voicedNasals:
                self.assertFalse(grammar.Word.isVoiced(s+n, 1))

#FIXME need test to make sure other letters don't cause devoicing
    def test_nBeforeStop(self):
        for n in grammar.Alphabet.voicedNasals:
            for s in grammar.Alphabet.stops:
                self.assertTrue(grammar.Word.isVoiced(n+s, 0))
if __name__ == '__main__':
    unittest.main()
