from plutonkit.management.request.ValidateSource import ValidateSource
import unittest

class TestValidateSource(unittest.TestCase):
    def test_valid_request(self):
        arch = ValidateSource("https://raw.githubusercontent.com/fonipts/pluton-lobby/main/blueprint/bottle")
        self.assertEqual(arch.arch_type, "request")

    def test_valid_local(self):
        arch = ValidateSource(".")
        self.assertEqual(arch.arch_type, "local")   

    def test_valid_git(self):
        arch = ValidateSource("https://github.com/fonipts/pluton-lobby.git")
        self.assertEqual(arch.arch_type, "git")
  
    def test_valid_git_w_branch(self):
        arch = ValidateSource("https://github.com/fonipts/pluton-lobby.git/[dev/1.0.2alpha0]/blueprint/django")
        self.assertEqual(arch.arch_type, "git")
