def LongestConsecutive(nums):
    num_set = set(nums)
    maxStreak = 0
    for n in num_set:
        if n-1 not in num_set:
            currentStreak = 1
            currentNum=n
            while currentNum+1 in num_set:
                currentStreak+=1
                currentNum+=1
            maxStreak = max(maxStreak, currentStreak)
    return maxStreak
            
nums =[100,4,200,1,3,2]
print(LongestConsecutive(nums))