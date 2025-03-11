class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer for the position of the next unique number to be placed in the list nums
        unique_nb = 1
        # Iterate through the list nums
        for i in range(1, len(nums)):
            # In case we have a unique number i
            if nums[i] != nums[i - 1]:
                # Place it at the unique_nb position and increment the pointer by 1 
                nums[unique_nb] = nums[i]
                unique_nb += 1
        return unique_nb # Correspond to the first unique numbers in the list nums