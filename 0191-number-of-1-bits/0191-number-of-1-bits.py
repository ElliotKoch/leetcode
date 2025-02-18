class Solution:
    def hammingWeight(self, n: int) -> int:
        # Count the number of 1 in the binary of n without the first 2 digits (0n)
        return bin(n)[2:].count("1")
         
        