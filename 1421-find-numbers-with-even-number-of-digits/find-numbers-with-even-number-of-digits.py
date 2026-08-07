class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count=0
        for num in nums:
            digits=0
            temp=num
            if temp==0:
                digit=1
            else:
                while temp!=0:
                    temp=temp//10
                    digits+=1
            if digits%2==0:
                count+=1
        return count


            