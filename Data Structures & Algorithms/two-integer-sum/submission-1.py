class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for x,y in enumerate(nums):
            need = target - y
            if need in seen:
                return [seen[need], x]
            seen[y] = x
        
            
        