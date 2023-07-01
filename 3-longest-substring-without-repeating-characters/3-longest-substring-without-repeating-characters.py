class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m,i=1,1
        # dvdf
        if len(s)==0: return 0
        if len(s)==1: return 1
        a =[s[0]]
        for b in s[1:]:   
            if b not in a:
                a.append(b)   
            else: 
                a=a[a.index(b)+1:]
                a.append(b) 
            print(a) 
            m=max(m,len(a))
        return m
         