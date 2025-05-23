def HouseRobber(nums):
    n = len(nums)
    if n==1:
        return nums[0]
    dp = [0]*n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2, n):
        dp[i]=max(dp[i-1], nums[i]+dp[i-2])
    return dp[-1]
nums = [2,7,9,3,1]
print(HouseRobber(nums))