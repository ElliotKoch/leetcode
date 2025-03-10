class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Initialize a Flag when the mountan is decreasing
        decrease_flag = False
        # Go though all the number starting with the second one
        for i in range(1,len(arr)):
            # If we are increasing the mountain
            if not decrease_flag:
                # Increase the mountain
                if arr[i-1] < arr[i]:
                    continue
                # Mountain is decreasing but not at the first step    
                elif i > 1 and arr[i-1] > arr[i]: 
                    decrease_flag = True
                # either arr is decreasing only or not strickly inc/dec
                else:
                    return False
            # If the mountain is strickly decreasing, we continue
            elif arr[i-1] > arr[i]:
                continue
            else:
                return False
        # Verify that it's not one element in the list
        if decrease_flag:
            return True
        else:
            return False
                

        