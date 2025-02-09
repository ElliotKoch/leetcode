class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers and their indices: {num:index}
        nums_dict = {}
        for i, num in enumerate(nums):
            # Complement is the number needed to reach the target
            complement = target - num
            if complement in nums_dict:
                # Return indices of the numbers
                return [i,nums_dict[complement]]
            else:
                # Store the current number's index
                nums_dict[num] = i