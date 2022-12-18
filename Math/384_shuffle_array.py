import random
class Solution:
    def __init__(self, nums):
        self.arr=nums
        self.original = nums[:]       
    def reset(self):
        return self.original
    def shuffle(self):
        new_arr = self.arr
        n=len(new_arr)
        for i in range(n):
            a = random.randint(0,n-1)
            b=random.randint(0,n-1)
            new_arr[a],new_arr[b]=new_arr[b],new_arr[a]
        return new_arr