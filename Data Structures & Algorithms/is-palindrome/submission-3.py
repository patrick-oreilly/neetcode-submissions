class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (("".join(c for c in s if c.isalnum())).lower()) == (("".join(c for c in s if c.isalnum())).lower())[::-1]
