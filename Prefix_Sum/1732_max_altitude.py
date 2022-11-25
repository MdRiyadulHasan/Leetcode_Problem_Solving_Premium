class Solution:
    def largestAltitude(self, gain) -> int:
        sum_till = 0
        max_altitude = 0
        for n in gain:
            sum_till+=n
            max_altitude = max(max_altitude, sum_till)
        return max_altitude