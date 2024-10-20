import math
from typing import List


class WordDistance:
    def __init__(self, valid_words) -> None:
        self.valid_words = valid_words

    def get_ave_distance(self, word) -> List[float]:
        list_ave_word = []
        for lookup in self.valid_words:
            list_ave_word.append(
                (
                    self.__word_distance(lookup, word) / len(word) +
                    self.__word_distance(lookup, word) / len(lookup)
                ) /
                2
            )
        return list_ave_word

    def __word_distance(self, ref_word, verify_word):
        indx_cnt = 0
        valid_count = 0
        repeate_count = len(ref_word) / len(verify_word)

        split_ref_word = [*ref_word]
        split_verify_word = [
            *(verify_word * math.ceil(repeate_count))[0: len(ref_word)]
        ]

        for vw in split_ref_word:
            valid_bool = False
            if indx_cnt < len(split_ref_word):

                val_ref_word = vw
                val_verify_word = split_verify_word[indx_cnt]
                if val_ref_word == val_verify_word:
                    valid_count += 1
                    valid_bool = True
            if valid_bool:
                indx_cnt += 1

        return valid_count
