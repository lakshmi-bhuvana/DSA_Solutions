class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen={}
        n=len(nums)
        res=[]

        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        
        for num in seen:
            if seen[num]>(n//3):
                res.append(num)
        return res
                