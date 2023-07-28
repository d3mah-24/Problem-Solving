class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r, l =  1, 1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i] *= l                
            l *= nums[i]
            res[-1-i] *= r            
            r *= nums[-1-i]
        return res