def jumpGame(nums):
    maxReachable = 0
    for i in range(len(nums)):
        if i>maxReachable:
            return False
        maxReachable = max(maxReachable, i+nums[i])
    return True
     
nums = [3,2,1,0,4]
print(jumpGame(nums))