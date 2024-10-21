import unittest
from subdeloc_tools import subtools as st
from tests.constants.subtools import *
from tests.constants.pairsubs import RESULT
import os

class TestSubTools(unittest.TestCase):

    def test_init(self):
        ST = st.SubTools("."+os.sep+"tests"+os.sep+"files"+os.sep+"eng.ass", "."+os.sep+"tests"+os.sep+"files"+os.sep+"jap.ass", "."+os.sep+"tests"+os.sep+"files"+os.sep+"names.json", "."+os.sep+"subdeloc_tools"+os.sep+"samples"+os.sep+"honorifics.json", "output.ass")
        self.assertEqual(ST.main_sub, "."+os.sep+"tests"+os.sep+"files"+os.sep+"eng.ass")
        self.assertEqual(ST.ref_sub, "."+os.sep+"tests"+os.sep+"files"+os.sep+"jap.ass")
        self.assertEqual(ST.honorifics["honorifics"]["san"]["kanjis"][0], "さん")
        self.assertEqual(ST.names["Hello"], "こんにちは")

    def test_honor_array(self):
        ST = st.SubTools("."+os.sep+"tests"+os.sep+"files"+os.sep+"eng.ass", "."+os.sep+"tests"+os.sep+"files"+os.sep+"jap.ass", "."+os.sep+"tests"+os.sep+"files"+os.sep+"names.json", "."+os.sep+"subdeloc_tools"+os.sep+"samples"+os.sep+"honorifics.json", "output.ass")
        self.assertEqual(ST.prepare_honor_array(), HONORIFICS_ARRAY)

    def test_search_honorifics(self):
        ST = st.SubTools("."+os.sep+"tests"+os.sep+"files"+os.sep+"eng.ass", "."+os.sep+"tests"+os.sep+"files"+os.sep+"jap.ass", "."+os.sep+"tests"+os.sep+"files"+os.sep+"names.json", "."+os.sep+"subdeloc_tools"+os.sep+"samples"+os.sep+"honorifics.json", "output.ass")
        s = ST.search_honorifics(RESULT)
        self.assertEqual(s[1]['original'][0]['text'], "World-dono")

if __name__ == "__main__":
    unittest.main()