class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target) < 1:
            return [-1, -1]
        i=nums.index(target)
        return [i,i+nums.count(target)-1 if nums[i+1 if len(nums) > i+1  else i]==target and len(nums)>1 and nums.count(target)>1   else i]
                    