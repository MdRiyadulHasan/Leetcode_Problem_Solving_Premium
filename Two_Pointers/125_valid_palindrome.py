class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l = l+1
            while l<r and not s[r].isalnum():
                r = r-1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    ob = Solution()
    ans = ob.isPalindrome(s)
    print(ans)