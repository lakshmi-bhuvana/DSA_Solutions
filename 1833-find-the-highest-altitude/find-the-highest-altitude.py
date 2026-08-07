class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum=0
        max_alt=0

        for num in gain:
            prefix_sum+=num
            max_alt=max(prefix_sum,max_alt)

        return max_alt
