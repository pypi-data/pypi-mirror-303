from plutonkit.management.logic.ConditionIdentify import ConditionIdentify
import unittest

class TestConditionIdentify(unittest.TestCase):
    def test_condition_invalid_status(self):
        cond = ConditionIdentify('        choices.database = "postgres"', {'choices': {'database': 'postgres'}})

        self.assertFalse(cond.validStatus())
        self.assertFalse(cond.validCond())

    def test_condition_valid(self):
        cond = ConditionIdentify('        choices.database == "postgres"', {'choices': {'database': 'postgres'}})

        self.assertTrue(cond.validCond())

    def test_condition_w_dict_valid(self):
        cond = ConditionIdentify('        choices.database == choices.local', {'choices': {'database': 'postgres','local': 'postgres'}})

        self.assertTrue(cond.validCond())

    def test_condition_w_dict_invalid(self):
        cond = ConditionIdentify('        choices.database == choices.local', {'choices': {'database': 'postgres','local': 'postgresss'}})

        self.assertFalse(cond.validCond())

    def test_condition_noteq_invalid(self):
        cond = ConditionIdentify('        choices.database != "mysql"', {'choices': {'database': 'postgres'}})

        self.assertTrue(cond.validCond())

    def test_condition_valid_greater(self):
        cond = ConditionIdentify('num.one < num.two', {'num': {'one': 1, 'two': 2}})

        self.assertTrue(cond.validCond())

    def test_condition_valid_less(self):
        cond = ConditionIdentify('num.two > num.one', {'num': {'one': 1, 'two': 2}})

        self.assertTrue(cond.validCond())    

    def test_condition_valid_greater_than(self):
        cond = ConditionIdentify('num.one <= num.two', {'num': {'one': 1, 'two': 2}})

        self.assertTrue(cond.validCond())

    def test_condition_valid_less_than(self):
        cond = ConditionIdentify('num.two >= num.one', {'num': {'one': 1, 'two': 2}})

        self.assertTrue(cond.validCond())    
