class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        Result=0
        for a in set(nums):
            count=nums.count(a)-1
            temp=((count+1)*count)//2
            Result+=temp
        return Result