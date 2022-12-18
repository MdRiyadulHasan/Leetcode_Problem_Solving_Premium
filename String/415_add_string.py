class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            result = 0
            for n in num:
                result = result*10 + ord(n)-ord('0')
            return result
        return str(str2int(num1)+str2int(num2))
if __name__ == '__main__':
     num1 = "456"
     num2 = "77"
     ob = Solution()
     ans = ob.addStrings(num1,num2)
     print(ans)