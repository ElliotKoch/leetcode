class Solution:
    def findGCD(self, nums: List[int]) -> int:

        # Find the minimum and maximum number in the list
        min_num = min(nums)
        max_num = max(nums)

        # Verify that the mod of a divisor is equal to 0 for both min and max number
        gcd = 0
        for x in range(1,max_num+1):
            if min_num % x == 0 and max_num % x == 0:
                gcd = x
            else:
                continue
        return gcd
        