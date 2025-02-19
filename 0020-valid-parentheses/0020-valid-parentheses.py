class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize stack with a default value to cater cases of alone closed parenthese
        stack = [0]
        for parenthese in s:
            # open parentheses are push in the stack
            if parenthese in ['{','[','(']:
                stack.append(parenthese)
            # Make sure that the last pushed open parenthese correspond to the closed one to pop it     
            elif parenthese == '}' and stack[-1] == '{':
                stack.pop()
            elif parenthese == ')' and stack[-1] == '(':
                stack.pop()
            elif parenthese == ']' and stack[-1] == '[':
                stack.pop()
            # If no match, return False because of miss writting in s
            else:
                return False
        # If stack is empty (only default value) means that all the open parentheses were correctly closed
        if len(stack) == 1:
            return True
        else:
            return False
        