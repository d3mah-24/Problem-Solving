class Solution:
    def isPalindrome(self, x: int) -> bool:
        data=[]
        if x<0:return False
        while x>0:
            data.append(x%10)
            x=x//10
        return data==data[::-1]