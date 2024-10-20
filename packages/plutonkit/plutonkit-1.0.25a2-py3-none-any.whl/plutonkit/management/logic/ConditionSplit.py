import re

from .ConditionIdentify import ConditionIdentify


class ConditionSplit:
    def __init__(self, cond: str, arg):
        self.cond: str = cond.strip()
        self.list_eq = []
        self.list_or = []
        self.arg = arg
        self.condCnt = 0
        self.validCnt = 0
        self.isValid = True
        self.__bootload()

    def validCond(self):
        return self.isValid

    def __countValid(self, list_cond, count_cond):
        cnt = 0
        for val in list_cond:
            if val:
                cnt += 1
        return cnt == count_cond

    def __bootload(self):
        tokens = re.split(r"([&]{2}|[\|]{2})", self.cond)
        types = "&&"
        for key, val in enumerate(tokens):
            mod_val = key % 2
            if mod_val == 0:
                if types == "&&":
                    self.list_eq.append(ConditionIdentify(val, self.arg).validCond())
                if types == "||":
                    self.list_or.append(ConditionIdentify(val, self.arg).validCond())
            if mod_val == 1:
                types = val
        cond_list_eq = self.__countValid(self.list_eq, len(self.list_eq))

        if cond_list_eq is False:
            cond_list_or = self.__countValid(self.list_or, 1)
            self.isValid = cond_list_or
