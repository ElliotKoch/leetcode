class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initiate two pointers with their flag for zeroes and non zeroes numbers
        flag_zero = False
        zero_index = 0
        flag_non_zero = False
        non_zero_index = 0

        # Iterate through the nums with the two pointers, when one reaches the end, it stops
        while zero_index < len(nums) and non_zero_index < len(nums):

            # Check the number at the position of each pointer
            if nums[zero_index] == 0 and not flag_zero:
                flag_zero = True
            elif nums[non_zero_index] != 0 and not flag_non_zero and non_zero_index > zero_index:
                flag_non_zero = True
            elif not flag_non_zero and not flag_zero:
                zero_index += 1 
                non_zero_index += 1 
            elif not flag_non_zero:
                non_zero_index += 1 
            elif not flag_zero and flag_non_zero:
                zero_index += 1

            # When a zero is before a non zero, their position is swaped
            if flag_zero and flag_non_zero:
                # Flags are reset
                flag_zero = False
                flag_non_zero = False
                nums[zero_index] = nums[non_zero_index]
                nums[non_zero_index] = 0
                # Move the pointers
                zero_index += 1
                non_zero_index += 1 

        # Time Complexity of O(n) and Space Complexity of O(1)


          
            





        