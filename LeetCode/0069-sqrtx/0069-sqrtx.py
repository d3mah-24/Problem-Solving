class Solution:
    def mySqrt(self, x: int) -> int:
        r=1
        if x==0:return 0
        for a in range(x):
            if a*a==x:
                r=a
                break
            elif a*a>x:
                r=a-1
                break
        return r