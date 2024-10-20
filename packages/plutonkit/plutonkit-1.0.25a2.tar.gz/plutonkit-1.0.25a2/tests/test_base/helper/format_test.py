from plutonkit.helper.format import git_name
import unittest

class TestFormat(unittest.TestCase):
    def test_name_fist_slash(self):
        self.assertEqual(git_name("/name"), 'name')

    def test_name_fist_slash_end(self):
        self.assertEqual(git_name("name/"), 'name')
 
    def test_name_fist_slash_both(self):
        self.assertEqual(git_name("/name/"), 'name')

    def test_name_middle_slash_both(self):
        self.assertEqual(git_name("/default/name/"), 'default/name')
