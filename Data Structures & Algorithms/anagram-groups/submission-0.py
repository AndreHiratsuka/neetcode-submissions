from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            # New frequency count for this string
            lista = [0] * 26

            for letter in string:
                index = ord(letter) - ord('a')
                lista[index] += 1

            key = tuple(lista)

            # Add the string to its anagram group
            if key not in result:
                result[key] = []

            result[key].append(string)

        return list(result.values())