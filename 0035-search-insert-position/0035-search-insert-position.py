class Solution:
    def searchInsert(self, nums: List[int], c: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==c:
                return mid
            elif nums[mid]>c:
                right=mid-1       
            else:
                left=mid+1
        return left