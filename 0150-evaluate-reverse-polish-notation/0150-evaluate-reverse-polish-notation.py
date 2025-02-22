class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initiate a list containing the arithmetic operations and a pointer 
        operations = ['+','-','*','/']
        operation_pointer = 0
        # Complexity of O(n) because we go through the tokens list once
        while operation_pointer < len(tokens):
            # If the pointer points toward an arithmetic operation
            if tokens[operation_pointer] in operations:
                # we take the two previous number and apply the operation
                if tokens[operation_pointer] == '+':
                    res = int(tokens[operation_pointer-2]) +  int(tokens[operation_pointer-1])
                elif tokens[operation_pointer] == '-':
                    res = int(tokens[operation_pointer-2]) -  int(tokens[operation_pointer-1])
                elif tokens[operation_pointer] == '*':
                    res = int(tokens[operation_pointer-2]) *  int(tokens[operation_pointer-1])
                elif tokens[operation_pointer] == '/':
                    res = int(tokens[operation_pointer-2]) /  int(tokens[operation_pointer-1])
                # We update the tokens list by removing the numbers and by adding the result of the operation
                tokens[operation_pointer-2] = res
                tokens.pop(operation_pointer)
                tokens.pop(operation_pointer-1)
                # Move the pointer toward the end (-2 (pop) + 1 = -1)
                operation_pointer -= 1
            else:
                operation_pointer += 1
        return int(tokens[0])

        