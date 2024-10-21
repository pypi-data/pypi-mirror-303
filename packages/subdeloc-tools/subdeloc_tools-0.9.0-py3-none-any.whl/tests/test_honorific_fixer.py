import unittest
from subdeloc_tools.modules import honorific_fixer
from tests.constants.pairsubs import RESULT
import os

class TestHonorificFixer(unittest.TestCase):
    def setUp(self):
        self.eng_file = "."+os.sep+"tests"+os.sep+"files"+os.sep+"eng.ass"
        self.jap_file = "."+os.sep+"tests"+os.sep+"files"+os.sep+"jap.ass"

    def test_prepare_edit_dict(self):
        result = honorific_fixer.prepare_edit_dict(RESULT)
        self.assertEqual(result, {'0': 'Hello', '1': 'Sir World'})

if __name__ == "__main__":
    unittest.main()