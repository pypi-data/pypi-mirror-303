from typing import List

from plutonkit.framework.analysis.word_distance import WordDistance

VALID_KEY: List[str] = ["env", "script"]
COMMAND_VALID_KEY: List[str] = ["command", "description", "group", "chdir"]


class SchemaCommand:
    def __init__(self, reference_value) -> None:

        self.reference_value = reference_value

    def get_error(self) -> List[str]:

        list_error: List[str] = []
        words_distance = WordDistance(VALID_KEY)
        for key, value in self.reference_value.items():
            distances = words_distance.get_ave_distance(key)
            max_distance = max(distances)
            if max_distance != 1.0:
                list_error.append(
                    f"the `{key}` is invalid,  I assume you are using this command instead `{VALID_KEY[distances.index(max_distance)]}`"
                )
            if key == "script":
                self.__validation_error_in_group(list_error, value)

        return list_error

    def __validation_error_in_group(self, list_error, value):
        command_words_distance = WordDistance(COMMAND_VALID_KEY)
        for _, value1 in value.items():
            for key2, value2 in value1.items():
                sub_distances = command_words_distance.get_ave_distance(key2)
                sub_max_distance = max(sub_distances)
                if sub_max_distance != 1.0:
                    list_error.append(
                        f"the `{key2}` is invalid,  I assume you are using this command instead `{COMMAND_VALID_KEY[sub_distances.index(sub_max_distance)]}`"
                    )
                if key2 == "group":
                    self.__validation_error_in_group(list_error, value2)
