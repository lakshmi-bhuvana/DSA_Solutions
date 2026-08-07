class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=sum(nums)

        for i in range(len(nums)):
            pivot=nums[i]
            right_sum-=pivot
            if left_sum==right_sum:
                return i

            left_sum+=pivot
            

            
                
        return -1
        