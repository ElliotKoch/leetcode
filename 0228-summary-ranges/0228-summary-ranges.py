class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        start_range= 0
        end_range = 1
        while start_range < len(nums):
            if start_range + end_range == len(nums):
                if start_range + 1 == start_range + end_range:
                    output.append(str(nums[start_range]))
                    start_range += end_range
                    end_range = 1
                else:
                    output.append(str(nums[start_range]) + "->" + str(nums[start_range + end_range - 1]))
                    start_range += end_range
                    end_range = 1
            elif nums[start_range] + end_range == nums[start_range + end_range]:
                end_range += 1
            elif start_range + 1 == start_range + end_range:
                output.append(str(nums[start_range]))
                start_range += end_range
                end_range = 1
            else:
                output.append(str(nums[start_range]) + "->" + str(nums[start_range + end_range - 1]))
                start_range += end_range
                end_range = 1
        return output
        