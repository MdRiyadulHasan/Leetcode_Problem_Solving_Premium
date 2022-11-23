class Solution:
    def isPalindrome(self, x: int) -> bool:
        rem = 0
        num = x
        sum = 0
        while x>0:
            rem = x%10
            sum=sum*10+rem
            x=x//10
        return sum == num
