class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=sorted(strs)
        l,r=s[0],s[-1]
        res=""
        for x in range(len(min(strs,key=len))):
            if l[x]!=r[x]:
                return res
            res+=r[x]
        return res
        
        