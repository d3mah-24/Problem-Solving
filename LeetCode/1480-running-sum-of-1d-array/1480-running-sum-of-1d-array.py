class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev=0
        for n in range(len(nums)):
            nums[n]+=prev
            prev=nums[n]
        return nums
    
        
            
        
        