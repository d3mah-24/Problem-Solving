class Solution:
    def isPowerOfFour(self, n: int) -> bool: 
        while n:
            if n==1:
                return True
            if n==0:
                return False
            n=n/4
            
        