class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key = lambda x :x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True