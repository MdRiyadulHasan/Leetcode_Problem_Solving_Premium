def MaximumSum(nums):
    maxSum = nums[0]
    currentSum=0
    for n in nums:
        currentSum+=n
        maxSum= max(maxSum, currentSum)
        if currentSum<0:
            currentSum=0
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(MaximumSum(nums))