class Solution:
    def numIdenticalPairs(self, nums) -> int:
        my_count = 0
        my_dict = {}
        for n in nums:
            if n in my_dict:
                my_count+=my_dict[n]
                my_dict[n]+=1
            else:
                my_dict[n] = 1
        return my_count
if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    ob = Solution()
    ans = ob.numIdenticalPairs(nums)
    print(ans)