class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    ob = Solution()
    ans = ob.merge(intervals)
    print(ans)