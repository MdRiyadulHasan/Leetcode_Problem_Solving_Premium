def twoSum(nums, target):
    dic = {}
    for i, n in enumerate(nums):
        diff = target-n 
        if diff in dic:
            return [dic[diff], i]
        dic[n] =i
   
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))