import re

from plutonkit.helper.arguments import get_dict_value


class ConditionIdentify:
    def __init__(self, cond: str, arg=None):
        self.cond: str = cond.strip()
        self.arg = arg
        self.valid = False
        self._key = ""
        self._cond = ""
        self._value = ""

        self.__bootload()

    def validStatus(self) -> bool:
        return self.valid

    def validCond(self) -> bool:  # [too-many-return-statements]

        if self.valid:
            _value = get_dict_value(self._value.strip().split("."),self.arg) or self._value.strip()

            key_value_state = get_dict_value(self._key.split("."), self.arg) or self._key
            if self._cond == "!=":
                return str(key_value_state).strip() != str(_value)
            if self._cond == "==":
                return str(key_value_state).strip() == str(_value)
            if self._cond == "<=":

                return int(key_value_state) <= int(_value)
            if self._cond == ">=":

                return int(key_value_state) >= int(_value)

            if self._cond == "<":
                return int(key_value_state) < int(_value)
            if self._cond == ">":

                return int(key_value_state) > int(_value)
        return False

    def __bootload(self):

        find_value = re.findall(r"(.*?)\s{0,}([=]{2}|!\=|<\=|>\=|<|>)", self.cond)
        self.valid = len(find_value) == 1

        if len(find_value) == 1:
            self._key = find_value[0][0]
            self._cond = find_value[0][1]
            value_split = self.cond.split(self._cond)
            self.valid = len(value_split) > 0
            if len(value_split) > 0:
                self._value = value_split[1].replace('"', "").replace("'", "")
