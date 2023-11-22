class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        Result=[]
        for x in range(left,right+1):
            Result.append(x)
            for a in str(x):
                if  a=="0" or x%int(a)!=0 :
                    Result.pop()
                    break  
        return Result