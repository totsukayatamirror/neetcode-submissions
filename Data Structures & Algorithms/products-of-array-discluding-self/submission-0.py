class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0;
        j = i+1;
        while(i < len(nums)):
            running_tot = nums[j]
            while(j != len(nums)-1):
                j+=1
                if j == i:
                   j = i 
                else:
                    running_tot *=nums[j]
                    
                
            output.append(running_tot)
            i +=1
            j = 0
        return output



        



