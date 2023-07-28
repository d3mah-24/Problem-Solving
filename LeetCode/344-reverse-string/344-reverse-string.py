class Solution:
    def reverseString(self, s: List[str]) -> None:
        d=len(s)-1
        for x in range(d,d//2,-1):
            s[x],s[d-x]= s[d-x],s[x] 
        