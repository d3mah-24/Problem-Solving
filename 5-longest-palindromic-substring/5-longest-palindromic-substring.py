class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ""

        for i, a in enumerate(s):
            if a in s[i+1:]:
                j = s[i+1:].index(a)+i+1
                for v in range(s[i+1:].count(a)):
                    st = s[i:j+1]
                    j += s[j+1:].find(a) +1
                    if st == st[::-1]:
                        m = max(m, st, key=lambda xo: len(xo))
        if m=="":return s[0]
        return m

                