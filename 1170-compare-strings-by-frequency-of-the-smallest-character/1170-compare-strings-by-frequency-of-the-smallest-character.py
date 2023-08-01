class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        a=sorted(d.count(min(d)) for d in words )
        b=[d.count(min(d)) for d in queries]
        res=[]
        l=len(a)
        for c in b:
            left,mid,right=0,len(a)//2,len(a)-1
            temp=l-bisect.bisect(a,c)
            # while left<=right:
            #     mid=left+(right-left)//2
            #     if a[mid]==c:
            #         temp=len(a)-mid
            #     elif c>a[mid]:
            #         right=mid-1 
            #     else:
            #         left=mid+1 
            res.append(temp)
            
        return res