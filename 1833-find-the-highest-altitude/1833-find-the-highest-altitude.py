class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initiate two variables for the current and max altitude
        curr_altitude = 0
        max_altitude = 0
        # Iterate through the gain to modify the altitude 
        for x in gain:
            curr_altitude += x
            # If the current altitude is bigger than the previous max altitude --> update the max altitude
            if curr_altitude > max_altitude:
                max_altitude = curr_altitude
            else:
                continue
        return max_altitude
        