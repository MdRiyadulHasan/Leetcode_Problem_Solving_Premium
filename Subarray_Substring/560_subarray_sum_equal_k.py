def subarraySum(nums,k):
    dic = {
        0:1
    }
    currentSum = 0
    count = 0
    for n in nums:
        currentSum+=n
        diff = currentSum-k
        if diff in dic:
            count+=dic[diff]
        dic[currentSum]=dic.get(currentSum,0)+1
    return count
nums = [1, 2, 3, -2, 5, -3, 1]
k = 5
print(subarraySum(nums,k))