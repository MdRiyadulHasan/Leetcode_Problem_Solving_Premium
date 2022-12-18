import heapq
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        min_heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heapq.heappush(min_heap, matrix[row][col])
        for _ in range(k-1):
            heapq.heappop(min_heap)
        
        return min_heap[0]
if __name__ =='__main__':
    matrix = [[1,5,9],[8,10,12],[9,13,15]]
    ob = Solution()
    k=7
    ans = ob.kthSmallest(matrix,k)
    print(ans)