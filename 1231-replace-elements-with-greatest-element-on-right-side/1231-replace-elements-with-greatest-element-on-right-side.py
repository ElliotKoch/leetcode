class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = max(arr)
        # For loop to go through the number of arr
        for i in range(len(arr)):
            # Last number is always -1
            if i == len(arr)-1:
                arr[i] = -1
            elif arr[i] == max_num:
                # Find the max number (on the right) and replace it with number of index i
                max_num = max(arr[i+1:])
                arr[i] = max_num
            # max num is stil the same as the previsous iteration
            else:
                arr[i] = max_num
        return arr

        