#!python
#encoding: utf-8
import unittest
import grammar


class ApostrophePurposeTest(unittest.TestCase):
    # TODO might be good to do some permutations of letters and test splitting
    # TODO write some tests that are supposed to fail
    # TODO add more test words

    def setUp(self):
        self.ngTestWords = ["tan'gurraq"]
        self.devoicingTestWords = ["it'gaq", "tek'ni"]
        self.geminationTestWords = ["taq'uq"]
        self.noGeminationTestWords = ["atu'urkaq", "apa'urluq"]
        self.stressTestWords = ["qvaru'rtuq", "melugu'rtuq", "neryartu'rtuq"]
        self.shortenedTestWords = ["qaill'"]

    def testNGTest(self):
        for w in self.ngTestWords:
            self.assertEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_NG_SEPARATOR)

        for c in [self.devoicingTestWords, self.geminationTestWords, self.noGeminationTestWords, self.stressTestWords,
                  self.shortenedTestWords]:
            for w in c:
                self.assertNotEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_NG_SEPARATOR)

    def testDevoicing(self):
        for c in [self.ngTestWords, self.geminationTestWords, self.noGeminationTestWords, self.stressTestWords,
                  self.shortenedTestWords]:
            for w in c:
                self.assertNotEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_PREVENT_DEVOICING)

        for w in self.devoicingTestWords:
            self.assertEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_PREVENT_DEVOICING)

    def testGemination(self):
        for c in [self.ngTestWords, self.devoicingTestWords, self.noGeminationTestWords, self.stressTestWords,
                  self.shortenedTestWords]:
            for w in c:
                    self.assertNotEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_GEMINATION_MARKER)

        for w in self.geminationTestWords:
            self.assertEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_GEMINATION_MARKER)

    def testNoGemination(self):
        for c in [self.ngTestWords, self.devoicingTestWords, self.geminationTestWords, self.stressTestWords,
                  self.shortenedTestWords]:
            for w in c:
                self.assertNotEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_PREVENT_GEMMINATION)

        for w in self.noGeminationTestWords:
            self.assertEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_PREVENT_GEMMINATION)

    def testDistruptStress(self):
        for c in [self.ngTestWords, self.devoicingTestWords, self.geminationTestWords, self.noGeminationTestWords,
                  self.shortenedTestWords]:
            for w in c:
                self.assertNotEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_DISRUPT_STRESS)

        for w in self.stressTestWords:
            self.assertEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_DISRUPT_STRESS)

    def testShortWords(self):
        for c in [self.ngTestWords, self.devoicingTestWords, self.geminationTestWords, self.noGeminationTestWords, self.stressTestWords]:
            for w in c:
                self.assertNotEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_SHORT_WORD)

        for w in self.shortenedTestWords:
            self.assertEqual(grammar.Word.apostrophePurpose(w), grammar.Word.APOS_SHORT_WORD)


if __name__ == '__main__':
    unittest.main()
