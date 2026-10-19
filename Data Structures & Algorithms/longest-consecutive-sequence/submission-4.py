class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return l
        
        num_set = set(nums)
        longest, current = 1,1

        for num in nums:
            if num - 1 in num_set:
                continue
            
            val = num + 1
            while val in num_set:
                current += 1
                if longest < current:
                    longest = current
                val += 1
            current = 1
            
        return longest
            
