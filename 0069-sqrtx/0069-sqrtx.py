class Solution:
    def mySqrt(self, x: int) -> int:
        a=1
        i=x

        while a*a<i:
            i//=2
            a+=1 
        if i==1:return 1 
        for t in range(0,i*i+1):
            if t*t==x:
                return t   
            elif t*t>x:
                return t-1
        return 1
