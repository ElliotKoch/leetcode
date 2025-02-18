class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Construct a list for each letter in magazine
        magazine_letters = list(magazine)
        
        # Ensure that every letter in magazine_letters can be used to write ransomNote 
        for letter in ransomNote:
            if letter in magazine_letters:
                magazine_letters.remove(letter) # Remove is removing the first matching element only
            else:
                return False
        return True
