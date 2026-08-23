class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        avg=len(num)//2
        if len(num)%2!=0:
            return num[avg]
        else:
            return (num[avg]+num[avg-1])/2
           
            
        