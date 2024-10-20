from plutonkit.helper.arguments import get_arg_cmd_value, get_config,get_dict_value
import unittest

class TestAruments(unittest.TestCase):
    def test_convert_arguments_valid(self):
        self.assertEqual(get_dict_value(["name"],{"name":"FOO"}), 'FOO')

    def test_convert_arguments_invalid(self):
        self.assertNotEqual(get_dict_value(["name"],{"name":"FOO"}), 'FO')
    
    def test_get_config_valid(self):
        self.assertEqual(get_config( {"command":[{"name":"bottle","type":"framework"}]} ), {"framework":"bottle"})

    def test_get_config_invalid(self):
        self.assertNotEqual(get_config( {"command":[{"name":"bottle","type":"framework"}]} ), {"framework":"django"})

    def test_get_arg_cmd_value_valid(self):
        self.assertEqual(get_arg_cmd_value( ["name=1"] ), {"name":"1"})

    def test_get_arg_cmd_value_w_extra_valid(self):
        self.assertEqual(get_arg_cmd_value( ["--help"] ), {'--help': ''})
