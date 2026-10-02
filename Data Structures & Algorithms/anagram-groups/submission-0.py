class Solution:
        

    def normaliseWord(self, word: str) -> list[int]:
        normalised = [0]*26
        for letter in word:
            index = ord(letter) - 97
            normalised[index] += 1
        
        return tuple(normalised)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        Output = []

        for word in strs:
            normalised = self.normaliseWord(word)
            anagramGroups[normalised].append(word)

        return list(anagramGroups.values())

                        
        