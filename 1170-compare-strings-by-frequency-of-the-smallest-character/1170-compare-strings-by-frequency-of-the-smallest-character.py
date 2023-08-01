class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        a=sorted(d.count(min(d)) for d in words )
        b=[d.count(min(d)) for d in queries]
        res=[]
        l=len(a)
        for c in b:  
            res.append(l-bisect.bisect(a,c))
        return res