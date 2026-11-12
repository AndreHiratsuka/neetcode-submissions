class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s = "".join(c for c in s if c.isalnum())
        for i in range(0, len(s)):
            if s[i] != s[-i-1]:
                return False
        return True