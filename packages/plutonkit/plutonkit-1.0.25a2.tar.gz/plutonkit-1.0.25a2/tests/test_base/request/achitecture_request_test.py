from plutonkit.management.request.ArchitectureRequest import ArchitectureRequest
import unittest
import os
from plutonkit.config import ARCHITECTURE_DETAILS_FILE 



class TestArchitectureRequest(unittest.TestCase):
    def test_valid_request(self):
        arch = ArchitectureRequest("https://raw.githubusercontent.com/fonipts/pluton-lobby/main/blueprint/bottle",os.getcwd())
        self.assertTrue(arch.isValidReq)

    def test_invalid_request(self):
        arch = ArchitectureRequest("https://raw.githubusercontent.com/fonipts/pluton-lobby/main/blueprint/bottle_err",os.getcwd())
        self.assertFalse(arch.isValidReq)

    def test_valid_request_getfiles(self):
        arch = ArchitectureRequest("https://raw.githubusercontent.com/fonipts/pluton-lobby/main/blueprint/bottle",os.getcwd())
        self.assertTrue(arch.getFiles(ARCHITECTURE_DETAILS_FILE)["is_valid"])

    def test_invalid_request_getfiles(self):
        arch = ArchitectureRequest("https://raw.githubusercontent.com/fonipts/pluton-lobby/main/blueprint/bottle_err",os.getcwd())
        self.assertFalse(arch.getFiles(ARCHITECTURE_DETAILS_FILE)["is_valid"])

    def test_valid_local(self):
        arch = ArchitectureRequest("tests/raw/yaml",os.getcwd())
        self.assertTrue(arch.isValidReq)

    def test_invalid_local(self):
        arch = ArchitectureRequest("tests/raw/tpl",os.getcwd())
        self.assertFalse(arch.isValidReq)

    def test_valid_request_getBlob(self):
        arch = ArchitectureRequest("https://raw.githubusercontent.com/fonipts/pluton-lobby/main/blueprint/bottle",os.getcwd())
        self.assertEqual(arch.getBlob(ARCHITECTURE_DETAILS_FILE),[ARCHITECTURE_DETAILS_FILE])

    def test_valid_local_getBlob(self):
        arch = ArchitectureRequest("tests/raw/yaml",os.getcwd())
        self.assertEqual(arch.getBlob({"file":ARCHITECTURE_DETAILS_FILE}),[{"file":ARCHITECTURE_DETAILS_FILE}])
