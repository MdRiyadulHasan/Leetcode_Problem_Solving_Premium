class Solution:
    def findDuplicate(self, nums) -> int:
        slow = fast = ans =0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        while ans!=slow:
            slow = nums[slow]
            ans = nums[ans]
        return ans
if __name__ == '__main__':
    nums = [1,3,4,2,2]
    ob = Solution()
    ans = ob.findDuplicate(nums)
    print(ans)
