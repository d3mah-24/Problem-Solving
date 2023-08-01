class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words=sorted(d.count(min(d)) for d in words )
        queries=[d.count(min(d)) for d in queries]
        res=[]
        l=len(words)
        for c in queries:  
            res.append(l-bisect.bisect(words,c))
        return res