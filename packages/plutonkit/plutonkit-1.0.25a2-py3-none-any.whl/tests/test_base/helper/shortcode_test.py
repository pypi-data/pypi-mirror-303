from plutonkit.helper.template import convert_shortcode
import unittest

class TestShortcode(unittest.TestCase):
    def test_convert_shortcode_valid(self):
        self.assertEqual(convert_shortcode("{{name}}",{"name":"FOO"}), 'FOO')

    def test_convert_shortcode_invalid(self):
        self.assertNotEqual(convert_shortcode("{{name}}",{"name":"FOO"}), 'FO')
