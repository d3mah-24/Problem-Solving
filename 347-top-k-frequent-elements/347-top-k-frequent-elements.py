class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for x in nums:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
        res =[g[0] for g in  sorted(data.items(), key=lambda  v: v[1])[::-1][:k]]

        return res
        
        
        