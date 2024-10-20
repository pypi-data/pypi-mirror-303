from plutonkit.framework.analysis.word_distance import WordDistance 
import unittest
from typing import List 


VALID_KEY: List[str] = ["environment", "script"] 


class TestWordDistance(unittest.TestCase):
    def test_valid_word_script(self):
        words_distance = WordDistance(VALID_KEY)
        distances = words_distance.get_ave_distance("script")
        max_distance = max(distances) 
        self.assertEqual(max_distance, 1.0)

    def test_invalid_word_script(self):
        words_distance = WordDistance(VALID_KEY)
        distances = words_distance.get_ave_distance("scripts")
        max_distance = max(distances) 
        self.assertNotEqual(max_distance, 1.0)
    