class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni=set(nums)

        if len(uni)!=len(nums):
            return True
        else:
            return False