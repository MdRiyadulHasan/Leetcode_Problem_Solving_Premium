class NumArray:

    def __init__(self, nums):
        self.res = []
        sum_till = 0
        for n in nums:
            sum_till+=n
            self.res.append(sum_till)
            
    def sumRange(self, left: int, right: int) -> int:
        if left!=0 :
            return self.res[right] - self.res[left-1]
        else:
            return self.res[right]