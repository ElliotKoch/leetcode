class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define a variable for s without punctuations
        s_no_punct = ""
        # Filter s with isalpha to retrieve only alphabetical and number characters
        for c in s:
            if c.isalpha() or (ord(c) > 47 and ord(c) < 58):
                s_no_punct += c.lower()
        # Check that it is a palindrome
        if s_no_punct == s_no_punct[::-1]:
            return True
        else:
            return False