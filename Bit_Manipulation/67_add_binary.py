class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a)<len(b):
            a='0'+a
        while len(b)<len(a):
            b='0'+b
        a = [int(i) for i in a]
        b= [int(i) for i in b]
        carry = 0
        res = ''
        for i in range(len(a)-1,-1,-1):
            val = a[i]+b[i]+carry
            if val==3:
                carry = 1
                res='1'+res
            elif val==2:
                carry=1
                res='0'+res
            elif val==1:
                carry=0
                res = '1'+res
            else:
                res='0'+res
        return str(carry)+res if carry else res
if __name__ == '__main__':
    a='110011'
    b='11110'
    ob = Solution()
    ans = ob.addBinary(a,b)
    print(ans)