import unittest
from subdeloc_tools.modules import pairsubs
from tests.constants.pairsubs import *
import os

class TestPairSubs(unittest.TestCase):
    def setUp(self):
        self.eng_file = "."+os.sep+"tests"+os.sep+"files"+os.sep+"eng.ass"
        self.jap_file = "."+os.sep+"tests"+os.sep+"files"+os.sep+"jap.ass"

    def test_pair_files(self):
        result = pairsubs.pair_files(self.eng_file, self.jap_file)
        self.assertEqual(result, RESULT)

    def test_sanitize_string(self):
        result = pairsubs.sanitize_string("{\\pos(212,77)\\fscx50}Foo{\\fscx100}")
        self.assertEqual(result, "Foo")

if __name__ == "__main__":
    unittest.main()