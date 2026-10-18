class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def normalize(word: str) -> list[int]:
            letters = [0]*26
            for c in word:
                val = ord(c) - 97
                letters[val] += 1
            return letters
        
        return normalize(s) == normalize(t)
        