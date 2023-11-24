class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # a=[0]*(n*2)
        # a[::2]=nums[:n]
        # a[1::2]=nums[n:]
        # return  a
        Result=[]
        for a,b in zip(nums[:n],nums[n:]):
            Result.append(a)
            Result.append(b)
        return Result