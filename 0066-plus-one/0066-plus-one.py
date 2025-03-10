class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Initiate an index starting from last digit
        index = len(digits)-1
        # add one algo
        while True:
            # Store the result of the last digit + 1 in a variable
            sum_result = digits[index] + 1
            # Check that result is equal to 10 and that it's the first digit
            if sum_result == 10 and index == 0:
                # In that case we put 0 the digit at 'index and add a "1" in the list at the first position 
                digits[index] = 0
                digits.insert(0,1)
                return digits
            # In case the result is just equal to ten, we replace the digit with 0 and decrease the index
            elif sum_result == 10:
                digits[index] = 0
                index -= 1

            else:
                # Just modify the digit with the result of the addition
                digits[index] = sum_result
                return digits


        