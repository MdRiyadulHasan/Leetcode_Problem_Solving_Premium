class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        while (i<len(intervals) and intervals[i][0]<newInterval[0]):
            i+=1
        intervals.insert(i,newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1]=max(res[-1][1],interval[1])
        return res
if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    ob = Solution()
    ans = ob.insert(intervals,newInterval)
    print(ans)