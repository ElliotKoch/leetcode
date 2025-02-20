class Solution:
    def reverseVowels(self, s: str) -> str:
        # Initialize a list of vowels and a list containing each letter of s
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        letters = [letter for letter in s]
        # Create a list that contain the index in s of the vowels
        stack =[[i,letters[i]] for i in range(len(letters)) if letters[i] in vowels]
        # Reverse the position of the vowels in letters 
        for i in range(len(stack)):
            letters[stack[len(stack)-1-i][0]] = stack[i][1]
        # Join letters to output s with Reverse Vowels
        return "".join(letters)


        