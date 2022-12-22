from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        n1 = len(s)
        n2=len(p)
        count_p = Counter(p)
        count_s = Counter(s[:n2-1])
        l=0
        res = []
        for r in range(n2-1,n1):
            count_s[s[r]]+=1
            if count_p==count_s:
                res.append(l)
            count_s[s[l]]-=1
            l+=1
        return res