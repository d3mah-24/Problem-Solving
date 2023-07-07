class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max_Value,Temp=-10**4,0
        for x in nums:
            Temp=max(x,Temp+x)
            Max_Value=max(Max_Value,Temp)
        return Max_Value
            
            
            