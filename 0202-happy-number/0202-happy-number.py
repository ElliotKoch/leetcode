class Solution:
    def isHappy(self, n: int) -> bool:
        # Initialize a check list to check redundant numbers
        check = []
        while n != 1:
            digits = str(n)
            n = 0
            # Sum of the digits of n to the power of 2
            for digit in digits:
                n += int(digit)**2
            # If n was encounter, return False
            if n in check:
                return False
            else:
                check.append(n)
        return True