class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        Result=0
        for a in hours:
            if a>=target:
                Result+=1
        return Result