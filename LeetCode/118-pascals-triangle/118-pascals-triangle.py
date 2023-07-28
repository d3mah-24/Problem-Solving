class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x=[[1]]
        for g in range(1,numRows):
            temp =[]
            for a in range(len(x)-1): 
                temp.append( x[-1][a]+x[-1][a+1])  
            x.append([1,*temp,1])
        return x