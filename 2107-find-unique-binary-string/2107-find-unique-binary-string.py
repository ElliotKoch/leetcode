class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Convert the binary string to base 10 numbers
        hex_nums = [int(num,2) for num in nums] 
        # Check the numbers (base 10) between 0 and 2^n
        for num in range(2**len(nums)):
            # For any number that is not in nums
            if num not in hex_nums:
                # Fomat is used to convert the number in a binary string of the desired size
                return f'{num:0{len(nums)}b}'
            else:
                continue



            

        