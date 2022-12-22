class Solution:
    def addToArrayForm(self, num, k: int):
        a = ''
        for n in num:
            a+=str(n)
        ans = int(a)+k
        ans = [int(i) for i in str(ans)]
        return ans