class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for x in strs:
            temp=tuple(sorted(x))
            if  temp in result:
                result[temp].append(x)
            else:
                result[temp] =[x]
        return result.values()
        