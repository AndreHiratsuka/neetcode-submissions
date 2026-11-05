class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for chara in t:
            if index < len(s) and chara == s[index]:
                index += 1
        if index == len(s):
            return True
        return False