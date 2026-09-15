class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        max_altitude = 0
        for i in range(len(gain)):
            max_altitude = max(max_altitude, start + gain[i])
            start = start + gain[i]

        return max_altitude

        