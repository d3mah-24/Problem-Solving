class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Max=1
        if len(nums)==0:return 0
        nums=sorted(set(nums))
        prev=nums[0]
        Temp=1
        for x in nums[1:]:
            if x-prev==1:
                Temp+=1
            else:
                Temp=1
            prev=x
            Max=max(Max,Temp)
        return Max
            
            
            
            
            