class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for j,x in enumerate(numbers,1):
            if target-x in numbers :
                if target-x!=x:
                    return  [j,numbers.index(target-x)+1] 
                else:
                    return  [j,numbers[j:].index( x)+1+j] 