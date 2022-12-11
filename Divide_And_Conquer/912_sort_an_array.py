class Solution:
    def sortArray(self, nums):
        def mergeTwosortedArray(L,R,nums):
            i,j,k=0,0,0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    nums[k]=L[i]
                    i+=1
                else:
                    nums[k] = R[j]
                    j+=1
                k+=1
            nums[k:]=L[i:] if i<len(L) else R[j:]

        def mergeSort(nums):
            if len(nums)==1:
                return
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]
            mergeSort(L)
            mergeSort(R)
            mergeTwosortedArray(L,R,nums)
        mergeSort(nums)
        return nums