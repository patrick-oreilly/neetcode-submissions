class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        out = ("".join(c for c in s if c.isalnum())).lower()

        print(out, out[::-1])
        return out == out[::-1]
