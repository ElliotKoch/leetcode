class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the index k
        k = 0
        # Go through the list to replace all the val number  
        for i in range(len(nums)):
            if nums[i] != val:
                # Replace at the index k the non val number such that val number are removed if encounter
                nums[k] = nums[i]
                k += 1
        return k
        