class Solution:
    def fib(self, n: int) -> int:
        if 0<=n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)