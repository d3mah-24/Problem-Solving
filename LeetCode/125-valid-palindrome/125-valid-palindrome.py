class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric="".join([f.lower() for f in s if f.lower() in "abcdefghijklmnopqrstuvwxyz0987654321"])
        return alphanumeric==alphanumeric[::-1]