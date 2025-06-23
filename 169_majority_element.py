class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bar = len(nums) / 2
        aboveCount = {}

        for i in range(len(nums)):
            if nums[i] not in aboveCount:
                aboveCount[nums[i]] = 1
            else:
                aboveCount[nums[i]] += 1
            if aboveCount[nums[i]] > bar:
                return nums[i]
        return
