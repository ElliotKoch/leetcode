class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initiate two pointers for each word with the merged string
        word1_pointer = 0
        word2_pointer = 0
        merged_string = ""
        # Go through each word
        while word1_pointer < len(word1) or word2_pointer < len(word2):
            # Check that there is a letter of the word to add in the merged string
            if word1_pointer < len(word1):
                merged_string += word1[word1_pointer]
                word1_pointer += 1
            if word2_pointer < len(word2):
                merged_string += word2[word2_pointer]
                word2_pointer += 1
        # Return the merged string
        return merged_string
