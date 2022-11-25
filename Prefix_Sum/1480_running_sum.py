class Solution:
    def runningSum(self, nums):
        running_sum = []
        sum_till = 0
        for n in nums:
            sum_till+=n
            running_sum.append(sum_till)
        return running_sum