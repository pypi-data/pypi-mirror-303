from plutonkit.management.template.TheShortCutWord import TheShortCutWord

import unittest

class TestShortCut(unittest.TestCase):
    def test_valid_recursive_UC_replace(self):
        templt = TheShortCutWord("{{name|ucfirst|replace(@,1)}}", {"name": "TEST@"})
        self.assertEqual(templt.get_convert(), "Test1")

    def test_valid_UC(self):
        templt = TheShortCutWord("{{name|ucfirst}}", {"name": "TEST"})
        self.assertEqual(templt.get_convert(), "Test")

    def test_valid_lower(self):
        templt = TheShortCutWord("{{name|lower}}", {"name": "TEST"})
        self.assertEqual(templt.get_convert(), "test")

    def test_valid_upper(self):
        templt = TheShortCutWord("{{name|upper}}", {"name": "test"})
        self.assertEqual(templt.get_convert(), "TEST")        

    def test_valid_replace(self):
        templt = TheShortCutWord("{{name|replace(@,1)}}", {"name": "TEST@"})
        self.assertEqual(templt.get_convert(), "TEST1")

    def test_valid_join_space(self):
        templt = TheShortCutWord("{{name|join_space(-)}}", {"name": "TEST join space"})
        self.assertEqual(templt.get_convert(), "TEST-join-space")

    def test_valid_if(self):
        templt = TheShortCutWord("{{name|if(@,1)}}", {"name": "@"})
        self.assertEqual(templt.get_convert(), "1")

