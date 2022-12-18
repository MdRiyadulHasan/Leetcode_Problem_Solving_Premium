class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i] = 0
        return [1]+digits
if __name__ =='__main__':
    digits = [9,9,9,9]
    ob = Solution()
    ans = ob.plusOne(digits)
    print(ans)