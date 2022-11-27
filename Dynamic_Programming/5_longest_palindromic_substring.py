class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        reslen = 0
        for i in range(len(s)):
            # string size is odd 
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            # string size even
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
if __name__ == '__main__':
    s = 'babad'
    ob =Solution()
    ans = ob.longestPalindrome(s)
    print(ans)