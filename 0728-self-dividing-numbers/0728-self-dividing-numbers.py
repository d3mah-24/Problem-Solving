class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        Result=[]
        for x in range(left,right+1):
            if "0" in str(x):
                continue
            Result.append(x)
            for a in str(x):
                if   x%int(a)!=0 :
                    Result.pop()
                    break  
        return Result