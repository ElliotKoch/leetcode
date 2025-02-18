class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Verify that x reversed is equal to x
        if  str(x) == str(x)[::-1]:
            return True
        else:
            return False 
        