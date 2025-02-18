class Solution:
    def isHappy(self, n: int) -> bool:
        check = []
        while n != 1:
            digits = str(n)
            n = 0
            for digit in digits:
                n += int(digit)**2
            if n in check:
                return False
            else:
                check.append(n)
        return True