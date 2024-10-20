from ..logic.ConditionSplit import ConditionSplit


class ContentExtraction:
    def __init__(self, components: str, args=None):
        self.components = components
        self.args = args
        self.get_component = self.__get_component()

    def __get_component(self):
        cond_list = [x for x in self.__get_key_component() if x in ["condition"]]

        if len(cond_list) > 0:
            raw_data = []
            is_valid_value = True
            count_cond = 0
            for row in self.components:
                if row["name"] == "condition":
                    is_valid_value = False
                    cond_valid = ConditionSplit(row["input"][0], self.args)
                    if count_cond == 0 and cond_valid.validCond():
                        is_valid_value = True
                        count_cond += 1
                elif row["name"] == "end":
                    count_cond = 0
                    is_valid_value = False
                    if count_cond == 0:
                        count_cond = 0
                        is_valid_value = True
                else:
                    if is_valid_value:
                        raw_data.append(row)
            return raw_data

        return self.components

    def __get_key_component(self):
        keys: str = []
        for component in self.components:
            keys.append(component["name"])
        return keys

    def get_content(self) -> str:
        content = ""
        return content
