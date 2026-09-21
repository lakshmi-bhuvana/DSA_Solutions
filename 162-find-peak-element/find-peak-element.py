class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_index=0
        for i in range(len(nums)):
            if nums[i]>nums[max_index]:
                max_index=i
        return max_index