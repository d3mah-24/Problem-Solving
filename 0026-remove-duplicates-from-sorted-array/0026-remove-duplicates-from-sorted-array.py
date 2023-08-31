class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = set(nums) 
        nums[:] = sorted(l)
        return len(l)
            