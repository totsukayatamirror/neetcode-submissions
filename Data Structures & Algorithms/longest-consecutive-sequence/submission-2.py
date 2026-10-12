class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for num in nums:
            streak = 0
            current = num

            while current in sett:
                streak +=1 
                current+=1 
            res = max(streak, res) 
        return res       