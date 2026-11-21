class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        for i in range(len(s)-1, 0, -1):
            if s[i] == ' ':
                return int(len(s)-1-i)
        return 1