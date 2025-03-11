class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a counter for the removed number and the index pointer
        counter_del_ele = 0
        i = 0
        # Escaping condition is to check if we are at the end of the list
        while nums[i] != '_' and len(nums)>1 and i != len(nums)-1:
            # Ensure that the number after is not the same
            if nums[i] == nums[i+1]:
                # If it is the case we delete it and we add underscore at the end of the list
                nums.pop(i)
                nums.append('_')
                # Increament counter for deleted item
                counter_del_ele += 1
            else:
                # If no duplicate, we increased counter
                i += 1
            
        # return the len of nums minus de number of removed number
        return len(nums)-counter_del_ele
        