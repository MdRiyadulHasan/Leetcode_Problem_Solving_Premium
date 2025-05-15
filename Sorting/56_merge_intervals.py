class Solution:
   def merge(intervals):
        result =[]
        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if not result or result[-1][1]<interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    ob = Solution()
    ans = ob.merge(intervals)
    print(ans)