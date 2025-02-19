class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the smallest word to avoid IndexError
        smallest_word = min(strs, key=len)
        common_prefix = ""
        # Iterate through each letter of the smallest word in every word of strs
        for letter in smallest_word:
            flag = True
            for word in strs:
                # If the letter is not the same in one word, we stop searching for a common prefix
                if letter != word[len(common_prefix)]:
                    flag = False
                    break
            # If the letter is common to all the word, we add it in the common prefix
            if flag:
                common_prefix += letter
            else:
                break
        return common_prefix

        