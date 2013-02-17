#!python
#encoding: utf-8
import unittest
import grammar


class ClassDetectionTests(unittest.TestCase):

    def setUp(self):
        self.allButPrime = set(grammar.Alphabet.alphabet) - set(grammar.Alphabet.primeVowels)

    # bases require at least 2 characters to be properly detected
    def test_tooFewCharacters(self):
        self.assertFalse(grammar.Base.isClassI(''))
        self.assertFalse(grammar.Base.isClassII(''))
        self.assertFalse(grammar.Base.isClassIII(''))
        self.assertFalse(grammar.Base.isClassIV(''))
        self.assertFalse(grammar.Base.isClassIVa(''))
        self.assertFalse(grammar.Base.isClassIVb(''))
        self.assertFalse(grammar.Base.isClassIVc(''))
        self.assertFalse(grammar.Base.isClassV(''))
        self.assertFalse(grammar.Base.isClassVI(''))

        for c in grammar.Alphabet.alphabet:
            self.assertFalse(grammar.Base.isClassI(c))
            self.assertFalse(grammar.Base.isClassII(c))
            self.assertFalse(grammar.Base.isClassIII(c))
            self.assertFalse(grammar.Base.isClassIV(c))
            self.assertFalse(grammar.Base.isClassIVa(c))
            self.assertFalse(grammar.Base.isClassIVb(c))
            self.assertFalse(grammar.Base.isClassIVc(c))
            self.assertFalse(grammar.Base.isClassV(c))
            self.assertFalse(grammar.Base.isClassVI(c))

    def test_BaseI(self):
        for p in self.allButPrime:
            for c in grammar.Alphabet.primeVowels:
                self.assertTrue(grammar.Base.isClassI(p + c))

        # Base I words can not end in 2 prime vowels
        for p in grammar.Alphabet.primeVowels:
            for c in grammar.Alphabet.primeVowels:
                self.assertFalse(grammar.Base.isClassI(p + c))

        # Base I words have to end in a prime vowel
        for p in grammar.Alphabet.alphabet:
            for c in self.allButPrime:
                self.assertFalse(grammar.Base.isClassI(p + c))

    def test_BaseII(self):
        for p in grammar.Alphabet.primeVowels:
            for c in grammar.Alphabet.primeVowels:
                self.assertTrue(grammar.Base.isClassII(p + c))

        for p in self.allButPrime:
            for c in grammar.Alphabet.primeVowels:
                self.assertFalse(grammar.Base.isClassII(p + c))

        for p in grammar.Alphabet.alphabet:
            for c in self.allButPrime:
                self.assertFalse(grammar.Base.isClassII(p + c))

if __name__ == '__main__':
    unittest.main()
