class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for num in (nums):
            count = 0
            curr = num
            while curr in sett:
                count+=1
                curr+=1 
            if count >= res:
                res = count
        return res
            
        