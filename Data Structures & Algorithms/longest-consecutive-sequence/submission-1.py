class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()

        longest, current = 1,1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            
            if nums[i + 1] - nums[i] == 1:
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1
        
        return longest