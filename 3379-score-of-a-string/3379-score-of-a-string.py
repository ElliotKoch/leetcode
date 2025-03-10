class Solution:
    def scoreOfString(self, s: str) -> int:
        # Initialize result
        res = 0
        # Go through each charac of the string s
        for i in range(0,len(s)-1):
            # abosulte value of the ASCI value of the two charac (pair)
            res += abs(ord(s[i]) - ord(s[i+1])) 
        return res