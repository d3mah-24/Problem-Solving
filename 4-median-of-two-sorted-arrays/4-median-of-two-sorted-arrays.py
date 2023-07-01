class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=sorted(nums1+nums2)
        
        if len(a)%2==0:
            return (a[len(a)//2-1]+a[len(a)//2])/2
        else:
            return a[len(a)//2]