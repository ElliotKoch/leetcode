class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # initialization of two pointers (one fr each list)
        i1 = 0
        i2 = 0
        # Breaking condition is that we reached the end of list nums2
        while i2 < n:
            # In case number in nums1 at index i1 is smaller than in nums2 index i2
            # and that i1 is smaller than m + nb of insert number in nums1
            print(nums1[i1],nums2[i2])
            if nums1[i1] < nums2[i2] and i1 < m:
                # Increase index i1 to compare the next number in nums1
                i1 += 1
            else:
                # If number in nums2 is smaller, we insert it at the position i1 in nums1
                nums1.insert(i1,nums2[i2])
                # Pop one extra 0
                nums1.pop()
                # Increase both pointers
                i2 += 1
                i1 += 1  
                # We insert one number in nums1 so we increased m + 1 
                m +=1     