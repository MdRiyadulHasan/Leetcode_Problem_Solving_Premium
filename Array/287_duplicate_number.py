def findDuplicate( nums) -> int:
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
        
nums = [1,3,4,2,2]
print(findDuplicate(nums))
