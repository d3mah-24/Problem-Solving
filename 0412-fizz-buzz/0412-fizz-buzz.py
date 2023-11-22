class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Result=[]
        for x in range(1,n+1):
            if x%3==0 and x%5==0:
                Result.append("FizzBuzz")
            elif x%3==0  :
                Result.append("Fizz")
            elif  x%5==0:
                Result.append("Buzz")
            else:
                Result.append(str(x))
        return Result