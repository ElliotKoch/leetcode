class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Sorts the list
        nums.sort()
        # Iterate through the num two by two
        for i in range(0, len(nums), 2):
            # In case the unique number is the last one
            if i == len(nums)-1:
                return nums[i]
            # Check that the next number is different
            elif nums[i] != nums[i+1]:
                return nums[i]
        


        