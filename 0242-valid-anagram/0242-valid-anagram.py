class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Decompose the string into a list
        s = list(s)
        t = list(t)
        # Go through the first word and remove the used letter in the second word
        for c in s:
            if c in t:
                t.remove(c)
            else:
                return False
        # If the second word is not empty (more letter than in the first one)
        if t:
            return False
        else:
            return True        