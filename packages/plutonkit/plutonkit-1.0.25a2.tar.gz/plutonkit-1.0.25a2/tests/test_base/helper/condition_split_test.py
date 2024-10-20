from plutonkit.management.logic.ConditionSplit import ConditionSplit
import unittest

class TestConditionSplit(unittest.TestCase):
    def test_condition_valid(self):
        cond = ConditionSplit('        choices.database == "postgres" && choices.redis == "local"', {'choices': {'database': 'postgres','redis': 'local'}})

        self.assertTrue(cond.validCond())

    def test_condition_invalid(self):
        cond = ConditionSplit('        choices.database == "mysql" ||choices.redis == "test"', {'choices': {'database': 'postgres','redis': 'local'}})

        self.assertFalse(cond.validCond())
