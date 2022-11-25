class Solution:
    def minMeetingRooms(self, intervals) -> int:
        rooms = 0
        if not intervals:
            return 0
        starts = sorted([n[0] for n in intervals])
        ends = sorted([n[1] for n in intervals])
        endsp = 0
        for i in range(len(starts)):
            if starts[i]>=ends[endsp]:
                endsp+=1
            else:
                rooms+=1
        return rooms
if __name__ =='__main__':
    intervals = [[1,10],[3,19],
    [2,7],[10,20],[11,30],[8,12]]
    ob= Solution()
    ans = ob.minMeetingRooms(intervals)
    print(ans)