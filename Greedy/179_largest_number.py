from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
        def compare(a,b):
            if a+b>b+a:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(''.join(nums)))
if __name__ == '__main__':
    nums = [3,30,34,5,9]
    ob = Solution()
    ans = ob.largestNumber(nums)
    print(ans)