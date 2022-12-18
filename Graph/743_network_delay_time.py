from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times, n, k) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        min_heap = [(0,k)]
        shortest_path = {}
        while min_heap:
            w,v=heapq.heappop(min_heap)
            if v not in shortest_path:
                shortest_path[v]=w
                for v_i,w_i in graph[v]:
                    heapq.heappush(min_heap,(w+w_i,v_i))
        if len(shortest_path)==n:
            return max(shortest_path.values())
        else:
            return -1
if __name__ == '__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    ob = Solution()
    ans = ob.networkDelayTime(times,n,k)
    print(ans)