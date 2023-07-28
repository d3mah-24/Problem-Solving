class NumArray:

    def __init__(self, nums: List[int]):
        self.n=[0]
        for x in  nums :
            self.n.append(self.n[-1]+x)
    def sumRange(self, left: int, right: int) -> int:
        return self.n[right+1]-self.n[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)