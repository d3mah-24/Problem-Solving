class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        x=[1]
        for g in range(rowIndex):
            temp =[]
            for a in range(len(x)-1): 
                temp.append( x[a]+x[a+1])  
            x=[1,*temp,1]
        return x
        
        