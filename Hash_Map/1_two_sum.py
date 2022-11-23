class Solution:
    def twoSum(self, nums, target: int):
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]
            else:
                hashmap[nums[i]] = i
if __name__ == '__main__':
    nums = [10,2,11,5,3,7,15]
    target = 9
    ob = Solution()
    ans = ob.twoSum(nums,target)
    print(ans)
