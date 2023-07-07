class Solution:
    def isValid(self, s: str) -> bool:
        data={"(":")","{":"}","[":"]"}
        store=[] 
        for a in s:
            if a in "{[(":
                store.append(a)
                continue
            elif not store or data[store[-1]]!=a:
                return False
            store.pop()
        return not store
            