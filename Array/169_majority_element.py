def majorityElement(nums):
    n = len(nums)
    from collections import Counter
    dic = Counter(nums)
    for k,v in dic.items():
        if v>n/2:
            return k
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))