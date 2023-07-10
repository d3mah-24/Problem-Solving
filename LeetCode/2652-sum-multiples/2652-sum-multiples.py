class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result=0
        for x in range(1,n+1):
            if not all([x%3,x%5,x%7]):
                result+=x
        return result