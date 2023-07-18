class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in numbers:
                if target-x in numbers :
                    if target-x!=x:
                        return  [numbers.index(x)+1,numbers.index(target-x)+1] 
                    else:
                        i=numbers.index(x)+1
                        return  [i,numbers[i:].index( x)+1+i] 