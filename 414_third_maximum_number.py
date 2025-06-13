class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = []
        for n in nums:
            if n not in unique_nums:
                unique_nums.append(n)

        for i in range(len(unique_nums)):
            swapped = False
            for j in range(len(unique_nums) - i - 1):
                if unique_nums[j] < unique_nums[j + 1]:
                    unique_nums[j], unique_nums[j + 1] = (
                        unique_nums[j + 1],
                        unique_nums[j],
                    )
                    swapped = True
            if not swapped:
                break
        if len(unique_nums) < 3:
            return unique_nums[0]
        return unique_nums[2]
