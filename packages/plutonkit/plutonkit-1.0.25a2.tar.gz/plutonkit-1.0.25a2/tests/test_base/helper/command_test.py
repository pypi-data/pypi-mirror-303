from plutonkit.helper.command import clean_command_split
import unittest

class TestCommand(unittest.TestCase):

    def test_validate_clean_command_split(self):
        self.assertEqual(clean_command_split("echo 1"), ["echo", "1"])

    def test_validate_clean_command_split_qoute(self):
        self.assertEqual(clean_command_split("echo  'hello\t'"), ["echo", "'hello\t'"])

